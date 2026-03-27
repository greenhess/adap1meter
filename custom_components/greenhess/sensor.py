import logging
import re
import aiohttp
import async_timeout
rom datetime import datetime, timedelta

from homeassistant.util import dt as dt_util

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
        lang = hass.config.language
        raw_name = sensor_config.get(lang) or sensor_config.get("en") or sensor_key.replace("_", " ").capitalize()
        unique_id = f"{url}_{product_type}_{sensor_key}"
        sensors.append(
            Ada12Sensor(
                coordinator=coordinator,
                product_type=product_type,
                sensor_key=sensor_key,
                sensor_config=sensor_config,
                unique_id=unique_id,
                prefix=prefix,
                name=f"{prefix} {raw_name}", 
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
        self._attributes = {"icon": sensor_config["icon"]}
        self._attributes["uid"] = unique_id  #extra sor az attributes-ba

        # Power factor is unitless but numeric; mark as measurement so HA graphs it as a curve.
        if sensor_key in ("power_factor", "power_factor_l1", "power_factor_l2", "power_factor_l3"):
            self._attributes["state_class"] = "measurement"

        # Serial number is informational; mark as diagnostic to avoid chart clutter.
        if sensor_key == "meter_serial_number":
            self._attributes["entity_category"] = "diagnostic"

        # Timestamp: expose as HA timestamp device_class (state conversion happens in state()).
        if sensor_key == "timestamp":
            self._attributes["device_class"] = "timestamp"

        # Energy panelhez szükséges beállítás 
        if "GAS_total" in sensor_key:
            self._attributes["device_class"] = "gas"
            self._attributes["state_class"] = "total_increasing"
            self._attributes["unit_of_measurement"] = "m³"
        elif "WATER_total" in sensor_key:
            self._attributes["device_class"] = "water"
            self._attributes["state_class"] = "total_increasing"
            self._attributes["unit_of_measurement"] = "m³"
        elif sensor_key in self.ENERGY_SENSORS:
            self._attributes["device_class"] = "energy"
            self._attributes["state_class"] = "total_increasing"
            self._attributes["unit_of_measurement"] = "kWh"
        elif sensor_config["unit"]:
            self._attributes["unit_of_measurement"] = sensor_config["unit"]

    def _parse_device_timestamp_local(self, value: str) -> str | None:
        """Parse device timestamp like 'YYMMDDHHmmssW' as local time and return ISO string."""
        if not isinstance(value, str):
            return None

        # Extract YYMMDDHHmmss, ignore trailing suffix like 'W'
        m = re.match(r"^(\d{12})", value)
        if not m:
            return None

        try:
            naive_local = datetime.strptime(m.group(1), "%y%m%d%H%M%S")
        except ValueError:
            return None

        aware_local = naive_local.replace(tzinfo=dt_util.DEFAULT_TIME_ZONE)
        return aware_local.isoformat()

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return self._unique_id

    @property
    def state(self):
        data = self.coordinator.data or {}

        # --- PLUGIN KEZELÉS ---
        if self._sensor_key.startswith("plugin_"):
            # pl. plugin_GAS_total_01 -> GAS_total_01
            real_key = self._sensor_key.replace("plugin_", "")
            plugins = data.get("plugins", {})
            # Belépünk a plugins -> GAS_total_01 -> value szintig
            return plugins.get(real_key, {}).get("value")
        
        # Sima kulcsok (fő szint)
        raw = data.get(self._sensor_key, 0 if self._sensor_config.get("unit") else "")

        if self._sensor_key == "timestamp":
            parsed = self._parse_device_timestamp_local(raw)
            if parsed is not None:
                return parsed

            # If parsing fails, keep raw and mark diagnostic to reduce chart noise.
            self._attributes["entity_category"] = "diagnostic"
            return raw

        return raw

    @property
    def extra_state_attributes(self):
        return self._attributes
