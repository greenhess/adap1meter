import logging
from homeassistant.components.sensor import (
    SensorEntity,
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.const import (
    ENERGY_KILO_WATT_HOUR,
    ELECTRIC_POTENTIAL_VOLT,
    ELECTRIC_CURRENT_AMPERE,
    FREQUENCY_HERTZ,
    POWER_KILO_WATT,
    REACTIVE_POWER,
)
from . import DOMAIN

_LOGGER = logging.getLogger(__name__)

SENSOR_TYPES = {
    "active_import_energy_total": {
        "name": "Összes importált energia",
        "unit": ENERGY_KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "icon": "mdi:flash"
    },
    "active_import_energy_tariff_1": {
        "name": "Importált energia tarifa 1",
        "unit": ENERGY_KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "icon": "mdi:flash"
    },
    "active_import_energy_tariff_2": {
        "name": "Importált energia tarifa 2",
        "unit": ENERGY_KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "icon": "mdi:flash"
    },
    "active_import_energy_tariff_3": {
        "name": "Importált energia tarifa 3",
        "unit": ENERGY_KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "icon": "mdi:flash"
    },
    "active_import_energy_tariff_4": {
        "name": "Importált energia tarifa 4",
        "unit": ENERGY_KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "icon": "mdi:flash"
    },
    "active_export_energy_total": {
        "name": "Összes exportált energia",
        "unit": ENERGY_KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "icon": "mdi:flash-outline"
    },
    "active_export_energy_tariff_1": {
        "name": "Exportált energia tarifa 1",
        "unit": ENERGY_KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "icon": "mdi:flash-outline"
    },
    "active_export_energy_tariff_2": {
        "name": "Exportált energia tarifa 2",
        "unit": ENERGY_KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "icon": "mdi:flash-outline"
    },
    "reactive_import_energy": {
        "name": "Reaktív importált energia",
        "unit": "kVArh",
        "device_class": None,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "icon": "mdi:circle-expand"
    },
    "reactive_export_energy": {
        "name": "Reaktív exportált energia",
        "unit": "kVArh",
        "device_class": None,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "icon": "mdi:circle-shrink"
    },
    "reactive_energy_qi": {
        "name": "Reaktív energia Qi",
        "unit": "kVArh",
        "device_class": None,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "icon": "mdi:alpha-q-circle"
    },
    "reactive_energy_qiv": {
        "name": "Reaktív energia Qiv",
        "unit": "kVArh",
        "device_class": None,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "icon": "mdi:alpha-q-circle-outline"
    },
    "voltage_phase_l1": {
        "name": "Fázis 1 (L1) feszültség",
        "unit": ELECTRIC_POTENTIAL_VOLT,
        "device_class": SensorDeviceClass.VOLTAGE,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:lightning-bolt"
    },
    "voltage_phase_l2": {
        "name": "Fázis 2 (L2) feszültség",
        "unit": ELECTRIC_POTENTIAL_VOLT,
        "device_class": SensorDeviceClass.VOLTAGE,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:lightning-bolt"
    },
    "voltage_phase_l3": {
        "name": "Fázis 3 (L3) feszültség",
        "unit": ELECTRIC_POTENTIAL_VOLT,
        "device_class": SensorDeviceClass.VOLTAGE,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:lightning-bolt"
    },
    "current_phase_l1": {
        "name": "Fázis 1 (L1) áramerősség",
        "unit": ELECTRIC_CURRENT_AMPERE,
        "device_class": SensorDeviceClass.CURRENT,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:current-ac"
    },
    "current_phase_l2": {
        "name": "Fázis 2 (L2) áramerősség",
        "unit": ELECTRIC_CURRENT_AMPERE,
        "device_class": SensorDeviceClass.CURRENT,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:current-ac"
    },
    "current_phase_l3": {
        "name": "Fázis 3 (L3) áramerősség",
        "unit": ELECTRIC_CURRENT_AMPERE,
        "device_class": SensorDeviceClass.CURRENT,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:current-ac"
    },
    "power_factor": {
        "name": "Teljesítménytényező",
        "unit": None,
        "device_class": SensorDeviceClass.POWER_FACTOR,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:cosine-wave"
    },
    "power_factor_l1": {
        "name": "Teljesítménytényező L1",
        "unit": None,
        "device_class": SensorDeviceClass.POWER_FACTOR,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:cosine-wave"
    },
    "frequency": {
        "name": "Frekvencia",
        "unit": FREQUENCY_HERTZ,
        "device_class": SensorDeviceClass.FREQUENCY,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:sine-wave"
    },
    "instantaneous_power_import": {
        "name": "Pillanatnyi importált teljesítmény",
        "unit": POWER_KILO_WATT,
        "device_class": SensorDeviceClass.POWER,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:flash"
    },
    "instantaneous_power_export": {
        "name": "Pillanatnyi exportált teljesítmény",
        "unit": POWER_KILO_WATT,
        "device_class": SensorDeviceClass.POWER,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:flash-outline"
    },
    "instantaneous_reactive_power_qi": {
        "name": "Pillanatnyi reaktív teljesítmény Qi",
        "unit": "kVAr",
        "device_class": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:alpha-q-circle"
    },
    "instantaneous_reactive_power_qii": {
        "name": "Pillanatnyi reaktív teljesítmény Qii",
        "unit": "kVAr",
        "device_class": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:alpha-q-circle"
    },
    "instantaneous_reactive_power_qiii": {
        "name": "Pillanatnyi reaktív teljesítmény Qiii",
        "unit": "kVAr",
        "device_class": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:alpha-q-circle"
    },
    "instantaneous_reactive_power_qiv": {
        "name": "Pillanatnyi reaktív teljesítmény Qiv",
        "unit": "kVAr",
        "device_class": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:alpha-q-circle-outline"
    },
    "current_limit_l1": {
        "name": "Áramkorlát L1",
        "unit": ELECTRIC_CURRENT_AMPERE,
        "device_class": SensorDeviceClass.CURRENT,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:current-limit"
    },
    "current_limit_l2": {
        "name": "Áramkorlát L2",
        "unit": ELECTRIC_CURRENT_AMPERE,
        "device_class": SensorDeviceClass.CURRENT,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:current-limit"
    },
    "current_limit_l3": {
        "name": "Áramkorlát L3",
        "unit": ELECTRIC_CURRENT_AMPERE,
        "device_class": SensorDeviceClass.CURRENT,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:current-limit"
    },
    "limiter_threshold": {
        "name": "Korlátozó küszöb",
        "unit": ELECTRIC_CURRENT_AMPERE,
        "device_class": SensorDeviceClass.CURRENT,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:current-limit"
    },
    "circuit_breaker_status": {
        "name": "Környezetvédelmi kapcsoló állapota",
        "unit": None,
        "device_class": None,
        "state_class": None,
        "icon": "mdi:electric-switch"
    },
    "meter_serial_number": {
        "name": "Mérő sorozatszáma",
        "unit": None,
        "device_class": None,
        "state_class": None,
        "icon": "mdi:barcode"
    }
}

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up ADA12 sensors."""
    coordinator = hass.data[DOMAIN][config_entry.entry_id]
    
    entities = []
    for sensor_type in SENSOR_TYPES:
        entities.append(Ada12Sensor(coordinator, sensor_type, config_entry.entry_id))
    
    async_add_entities(entities, True)

class Ada12Sensor(SensorEntity):
    """Representation of an ADA12 sensor."""
    
    def __init__(self, coordinator, sensor_type, entry_id):
        """Initialize the sensor."""
        self._coordinator = coordinator
        self._sensor_type = sensor_type
        self._entry_id = entry_id
        
        sensor_info = SENSOR_TYPES[sensor_type]
        self._attr_name = sensor_info["name"]
        self._attr_native_unit_of_measurement = sensor_info["unit"]
        self._attr_device_class = sensor_info.get("device_class")
        self._attr_state_class = sensor_info.get("state_class")
        self._attr_icon = sensor_info.get("icon")
        self._attr_unique_id = f"{entry_id}_{sensor_type}"
        self._attr_has_entity_name = True
        
    @property
    def native_value(self):
        """Return the state of the sensor."""
        return self._coordinator.data.get(self._sensor_type)
        
    @property
    def available(self):
        """Return if entity is available."""
        return self._coordinator.last_update_success
        
    @property
    def device_info(self):
        """Return device info."""
        return {
            "identifiers": {(DOMAIN, self._entry_id)},
            "name": "ADA12 P1 Meter",
            "manufacturer": "ADA",
            "model": "P1 Meter"
        }
        
    async def async_added_to_hass(self):
        """When entity is added to hass."""
        await super().async_added_to_hass()
        self.async_on_remove(
            self._coordinator.async_add_listener(
                self.async_write_ha_state
            )
        )
