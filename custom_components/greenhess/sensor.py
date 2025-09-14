import logging
import aiohttp
import async_timeout
from datetime import timedelta

from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)

from .product_config import get_product_sensors, get_product_name

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(seconds=10)


async def async_setup_entry(hass, config_entry, async_add_entities):
    config_data = {**config_entry.data, **config_entry.options}
    prefix = config_data.get("prefix", "")
    product_type = config_data.get("product_type", "ada12")

    # ------------------------
    # URL logika
    # ------------------------
    url = config_data.get("url")
    if not url:
        host = config_data.get("host", "okosvillanyora.local")
        port = config_data.get("port", 8989)
        url = f"http://{host}:{port}/json"

    product_sensors = get_product_sensors(product_type)
    product_name = get_product_name(product_type)

    async def async_update_data():
        try:
            async with aiohttp.ClientSession() as session:
                async with async_timeout.timeout(10):
                    async with session.get(url) as response:
                        return await response.json()
        except Exception as err:
            raise UpdateFailed(f"Error fetching data from {url}: {err}") from err

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=f"{prefix} {product_name} coordinator",
        update_method=async_update_data,
        update_interval=SCAN_INTERVAL,
    )

    await coordinator.async_config_entry_first_refresh()

    sensors = []
    for sensor_key, sensor_config in product_sensors.items():
        unique_id = f"{url}_{product_type}_{sensor_key}"
        sensors.append(
            Ada12Sensor(
                coordinator=coordinator,
                product_type=product_type,
                sensor_key=sensor_key,
                sensor_config=sensor_config,
                unique_id=unique_id,
                prefix=prefix,
                name=f"{prefix} {product_name} {sensor_config['friendly_name']}",
                device_id=device_id,
            )
        )

    async_add_entities(sensors)


class Ada12Sensor(CoordinatorEntity, Entity):
    ENERGY_SENSORS = ["active_import_energy_total", "active_export_energy_total"]

    def __init__(self, coordinator, product_type, sensor_key, sensor_config, unique_id, prefix, name):
        super().__init__(coordinator)
        self._product_type = product_type
        self._sensor_key = sensor_key
        self._sensor_config = sensor_config
        self._unique_id = unique_id
        self._prefix = prefix
        self._name = name
        self._device_id = device_id 
        self._attributes = {"icon": sensor_config["icon"]}
        self._attributes["uid"] = unique_id  #extra sor az attributes-ba

        # Energy panelhez szükséges beállítás  
        if sensor_key in self.ENERGY_SENSORS:
            self._attributes["device_class"] = "energy"
            self._attributes["state_class"] = "total_increasing"
            self._attributes["unit_of_measurement"] = "kWh"
        elif sensor_config["unit"]:
            self._attributes["unit_of_measurement"] = sensor_config["unit"]

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return self._unique_id

    @property
    def device_info(self):
        return {
            "identifiers": {(self._device_id,)},  
            "name": self._name,
            "manufacturer": "ADA",
            "model": self._product_type,
        }      
            
    @property
    def state(self):
        data = self.coordinator.data or {}
        return data.get(self._sensor_key, 0 if self._sensor_config["unit"] else "")

    @property
    def extra_state_attributes(self):
        return self._attributes
