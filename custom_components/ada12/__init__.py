import logging
import aiohttp
import async_timeout
from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
import voluptuous as vol
from homeassistant.const import CONF_NAME
from homeassistant.helpers import config_validation as cv

_LOGGER = logging.getLogger(__name__)
_LOGGER.info("ADA P1 Meter integráció indul")

DOMAIN = "ada12"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the ADA12 component."""
    hass.data.setdefault(DOMAIN, {})
    return True

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry):
    """Set up Ada12 from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    # Config adatok
    config_data = {**config_entry.data, **config_entry.options}
    host = config_data.get("host", "okosvillanyora.local")
    port = config_data.get("port", 8989)

    _LOGGER.info(f"ADA12 configured with host {host} and port {port}")

    # Coordinator létrehozása
    coordinator = Ada12DataUpdateCoordinator(hass, host, port)
    await coordinator.async_config_entry_first_refresh()
    
    # Platform betöltése
    hass.data[DOMAIN][config_entry.entry_id] = coordinator
    
    # Sensor platform betöltése
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(config_entry, "sensor")
    )
    
    return True

async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry):
    """Unload a config entry."""
    await hass.config_entries.async_forward_entry_unload(config_entry, "sensor")
    hass.data[DOMAIN].pop(config_entry.entry_id)
    return True

class Ada12DataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching ADA12 data."""
    
    def __init__(self, hass, host, port):
        """Initialize."""
        super().__init__(
            hass,
            _LOGGER,
            name="ADA12",
            update_interval=timedelta(seconds=60)
        )
        self.host = host
        self.port = port
        self.data = {}

    async def _async_update_data(self):
        """Fetch data from ADA12."""
        url = f"http://{self.host}:{self.port}/json"
        try:
            async with aiohttp.ClientSession() as session:
                async with async_timeout.timeout(10):
                    async with session.get(url) as response:
                        self.data = await response.json()
                        return self.data
        except Exception as e:
            _LOGGER.error(f"Error fetching data: {e}")
            raise UpdateFailed(f"Error communicating with API: {e}")
