"""Product configuration for ADA family devices."""

# Product definitions with their supported sensors
# ignored entries pziot-e02: username, password, wifi_ssid, local_ip, os_version, mac_address, cosem_logical_device_name,
# ignored entries ada one: username, password, os_version, local_ip, cosem_logical_device_name, client_id, current_tariff, timestamp
PRODUCT_CONFIGS = {
    "ada12": {
        "name": "ADA P1 Meter",
        "description": "Full-featured smart meter with all sensors",
        "host": "okosvillanyora.local",
        "default_port": 8989,
        "sensors": {
        # Összesített energia
        "active_import_energy_total": {
            "unit": "kWh",
            "friendly_name": "Összes importált energia",
            "icon": "mdi:transmission-tower-import"
            "state_class": "total_increasing"
        },
        "active_export_energy_total": {
            "unit": "kWh",
            "friendly_name": "Összes exportált energia",
            "icon": "mdi:transmission-tower-export"
            "state_class": "total_increasing"
        },
        "total_active_energy": {
            "unit": "kWh",
            "friendly_name": "Összes aktív energia",
            "icon": "mdi:lightning-bolt"
            "state_class": "total_increasing"
        },

        # Tarifa szerinti bontás
        "active_import_energy_tariff_1": {
            "unit": "kWh",
            "friendly_name": "Importált energia tarifa 1",
            "icon": "mdi:counter"
        },
        "active_import_energy_tariff_2": {
            "unit": "kWh",
            "friendly_name": "Importált energia tarifa 2",
            "icon": "mdi:counter"
        },
        "active_import_energy_tariff_3": {
            "unit": "kWh",
            "friendly_name": "Importált energia tarifa 3",
            "icon": "mdi:counter"
        },
        "active_import_energy_tariff_4": {
            "unit": "kWh",
            "friendly_name": "Importált energia tarifa 4",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_1": {
            "unit": "kWh",
            "friendly_name": "Exportált energia tarifa 1",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_2": {
            "unit": "kWh",
            "friendly_name": "Exportált energia tarifa 2",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_3": {
            "unit": "kWh",
            "friendly_name": "Exportált energia tarifa 3",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_4": {
            "unit": "kWh",
            "friendly_name": "Exportált energia tarifa 4",
            "icon": "mdi:counter"
        },

        # Reaktív energia (kVArh)
        "reactive_import_energy": {
            "unit": "kVArh",
            "friendly_name": "Reaktív importált energia",
            "icon": "mdi:sine-wave"
        },
        "reactive_export_energy": {
            "unit": "kVArh",
            "friendly_name": "Reaktív exportált energia",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qi": {
            "unit": "kVArh",
            "friendly_name": "Reaktív energia QI",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qii": {
            "unit": "kVArh",
            "friendly_name": "Reaktív energia QII",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qiii": {
            "unit": "kVArh",
            "friendly_name": "Reaktív energia QIII",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qiv": {
            "unit": "kVArh",
            "friendly_name": "Reaktív energia QIV",
            "icon": "mdi:sine-wave"
        },

        # Pillanatnyi teljesítmény
        "instantaneous_power_import": {
            "unit": "kW",
            "friendly_name": "Pillanatnyi importált teljesítmény",
            "icon": "mdi:flash",
            "state_class": "measurement"
        },
        "instantaneous_power_export": {
            "unit": "kW",
            "friendly_name": "Pillanatnyi exportált teljesítmény",
            "icon": "mdi:flash",
            "state_class": "measurement"
        },
        "instantaneous_power_import_l1": {
            "unit": "kW",
            "friendly_name": "Importált teljesítmény L1",
            "icon": "mdi:flash"
        },
        "instantaneous_power_import_l2": {
            "unit": "kW",
            "friendly_name": "Importált teljesítmény L2",
            "icon": "mdi:flash"
        },
        "instantaneous_power_import_l3": {
            "unit": "kW",
            "friendly_name": "Importált teljesítmény L3",
            "icon": "mdi:flash"
        },
        "instantaneous_power_export_l1": {
            "unit": "kW",
            "friendly_name": "Exportált teljesítmény L1",
            "icon": "mdi:flash"
        },
        "instantaneous_power_export_l2": {
            "unit": "kW",
            "friendly_name": "Exportált teljesítmény L2",
            "icon": "mdi:flash"
        },
        "instantaneous_power_export_l3": {
            "unit": "kW",
            "friendly_name": "Exportált teljesítmény L3",
            "icon": "mdi:flash"
        },

        # Pillanatnyi reaktív teljesítmény
        "instantaneous_reactive_power_qi": {
            "unit": "kVAr",
            "friendly_name": "Reaktív teljesítmény QI",
            "icon": "mdi:sine-wave"
        },
        "instantaneous_reactive_power_qii": {
            "unit": "kVAr",
            "friendly_name": "Reaktív teljesítmény QII",
            "icon": "mdi:sine-wave"
        },
        "instantaneous_reactive_power_qiii": {
            "unit": "kVAr",
            "friendly_name": "Reaktív teljesítmény QIII",
            "icon": "mdi:sine-wave"
        },
        "instantaneous_reactive_power_qiv": {
            "unit": "kVAr",
            "friendly_name": "Reaktív teljesítmény QIV",
            "icon": "mdi:sine-wave"
        },

        # Feszültségek
        "voltage_phase_l1": {
            "unit": "V",
            "friendly_name": "Feszültség L1",
            "icon": "mdi:flash"
        },
        "voltage_phase_l2": {
            "unit": "V",
            "friendly_name": "Feszültség L2",
            "icon": "mdi:flash"
        },
        "voltage_phase_l3": {
            "unit": "V",
            "friendly_name": "Feszültség L3",
            "icon": "mdi:flash"
        },

        # Áramerősségek
        "current_phase_l1": {
            "unit": "A",
            "friendly_name": "Áramerősség L1",
            "icon": "mdi:current-ac"
        },
        "current_phase_l2": {
            "unit": "A",
            "friendly_name": "Áramerősség L2",
            "icon": "mdi:current-ac"
        },
        "current_phase_l3": {
            "unit": "A",
            "friendly_name": "Áramerősség L3",
            "icon": "mdi:current-ac"
        },
        "current_phase_Bl1": {
            "unit": "A",
            "friendly_name": "Áramerősség Bl1",
            "icon": "mdi:current-ac"
        },
        "current_phase_Bl2": {
            "unit": "A",
            "friendly_name": "Áramerősség Bl2",
            "icon": "mdi:current-ac"
        },
        "current_phase_Bl3": {
            "unit": "A",
            "friendly_name": "Áramerősség Bl3",
            "icon": "mdi:current-ac"
        },

        # Frekvencia
        "frequency": {
            "unit": "Hz",
            "friendly_name": "Hálózati frekvencia",
            "icon": "mdi:sine-wave"
        },

        # Teljesítménytényező
        "power_factor": {
            "unit": "",
            "friendly_name": "Teljesítménytényező",
            "icon": "mdi:cosine-wave"
        },
        "power_factor_l1": {
            "unit": "",
            "friendly_name": "Teljesítménytényező L1",
            "icon": "mdi:cosine-wave"
        },
        "power_factor_l2": {
            "unit": "",
            "friendly_name": "Teljesítménytényező L2",
            "icon": "mdi:cosine-wave"
        },
        "power_factor_l3": {
            "unit": "",
            "friendly_name": "Teljesítménytényező L3",
            "icon": "mdi:cosine-wave"
        },

        # Egyéb
        "meter_serial_number": {
            "unit": "",
            "friendly_name": "Mérő sorozatszáma",
            "icon": "mdi:identifier"
        },
        "circuit_breaker_status": {
            "unit": "",
            "friendly_name": "Kismegszakító állapot",
            "icon": "mdi:toggle-switch"
        },
        "current_tariff": {
            "unit": "",
            "friendly_name": "Aktív tarifa",
            "icon": "mdi:calendar"
        },
        "timestamp": {
            "unit": "",
            "friendly_name": "Időbélyeg",
            "icon": "mdi:clock-outline"
        }
    }
    },
    "adaone": {
        "name": "ADA One",
        "description": "Basic meter with essential sensors only",
        "host": "adaone.local",
        "default_port": 80,
        "sensors": {
            "active_import_energy_total": {
                "unit": "kWh",
                "friendly_name": "Összes importált energia",
                "icon": "mdi:transmission-tower-import",
                "state_class": "total_increasing"
            },
            "active_export_energy_total": {
                "unit": "kWh",
                "friendly_name": "Összes exportált energia",
                "icon": "mdi:transmission-tower-export",
                "state_class": "total_increasing"
            },
            "total_active_energy": {
                "unit": "kWh",
                "friendly_name": "Összes aktív energia",
                "icon": "mdi:transmission-tower-import",
                "state_class": "total_increasing"
            },
            "power_factor": {
                "unit": "",
                "friendly_name": "Teljesítménytényező",
                "icon": "mdi:cosine-wave"
            },
            "power_factor_l1": {
                "unit": "",
                "friendly_name": "Teljesítménytényező (L1)",
                "icon": "mdi:cosine-wave"
            },
            "power_factor_l2": {
                "unit": "",
                "friendly_name": "Teljesítménytényező (L2)",
                "icon": "mdi:cosine-wave"
            },
            "power_factor_l3": {
                "unit": "",
                "friendly_name": "Teljesítménytényező (L3)",
                "icon": "mdi:cosine-wave"
            },
            "voltage_phase_l1": {
                "unit": "V",
                "friendly_name": "Fázis 1 (L1) feszültség",
                "icon": "mdi:flash"
            },
            "voltage_phase_l2": {
                "unit": "V",
                "friendly_name": "Fázis 2 (L2) feszültség",
                "icon": "mdi:flash"
            },
            "voltage_phase_l3": {
                "unit": "V",
                "friendly_name": "Fázis 3 (L3) feszültség",
                "icon": "mdi:flash"
            },
            "current_phase_l1": {
                "unit": "A",
                "friendly_name": "Fázis 1 (L1) áramerősség",
                "icon": "mdi:current-ac"
            },
            "current_phase_Bl1": {
                "unit": "A",
                "friendly_name": "Fázis 1 (L1) kalkulált áramerősség",
                "icon": "mdi:current-ac"
            },
            "current_phase_l2": {
                "unit": "A",
                "friendly_name": "Fázis 2 (L2) áramerősség",
                "icon": "mdi:current-ac"
            },
            "current_phase_Bl2": {
                "unit": "A",
                "friendly_name": "Fázis 2 (L2) kalkulált áramerősség",
                "icon": "mdi:current-ac"
            },
            "current_phase_l3": {
                "unit": "A",
                "friendly_name": "Fázis 3 (L3) áramerősség",
                "icon": "mdi:current-ac"
            },
            "current_phase_Bl3": {
                "unit": "A",
                "friendly_name": "Fázis 3 (L3) kalkulált áramerősség",
                "icon": "mdi:current-ac"
            },
            "instantaneous_power_import": {
                "unit": "kW",
                "friendly_name": "Pillanatnyi importált teljesítmény",
                "icon": "mdi:flash",
                "state_class": "measurement"
            },
            "instantaneous_power_export": {
                "unit": "kW",
                "friendly_name": "Pillanatnyi exportált teljesítmény",
                "icon": "mdi:flash",
                "state_class": "measurement"
            },
            "meter_serial_number": {
                "unit": "",
                "friendly_name": "Mérő sorozatszáma",
                "icon": "mdi:identifier"
            }
        }
    },
    "adabridge": {
        "name": "ADA Bridge",
        "description": "Compact meter with minimal sensors",
        "host": "adabridge.local",
        "default_port": 80,
        "sensors": {
            "active_import_energy_total": {
                "unit": "kWh",
                "friendly_name": "Összes importált energia",
                "icon": "mdi:transmission-tower-import",
                "state_class": "total_increasing"
            },
            "voltage_phase_l1": {
                "unit": "V",
                "friendly_name": "Fázis 1 (L1) feszültség",
                "icon": "mdi:flash"
            },
            "current_phase_l1": {
                "unit": "A",
                "friendly_name": "Fázis 1 (L1) áramerősség",
                "icon": "mdi:current-ac"
            },
            "instantaneous_power_import": {
                "unit": "kW",
                "friendly_name": "Pillanatnyi importált teljesítmény",
                "icon": "mdi:flash"
                "state_class": "measurement"
            }
        }
    },
    "adapziote02": {
        "name": "ADA PZIOT-E02",
        "description": "Compact meter with minimal sensors",
        "host": "pziot-e02.local",
        "default_port": 80,
        "sensors": {
            "active_energy_import_total": {
                "unit": "kWh",
                "friendly_name": "Összes importált energia",
                "icon": "mdi:transmission-tower-import"
                "state_class": "total_increasing"
            },
            "voltage_l1": {
                "unit": "V",
                "friendly_name": "Fázis 1 (L1) feszültség",
                "icon": "mdi:flash"
            },
            "current_phase_l1": {
                "unit": "A",
                "friendly_name": "Fázis 1 (L1) áramerősség",
                "icon": "mdi:current-ac"
            },
            "calculated_current_phase_l1": {
                "unit": "A",
                "friendly_name": "Fázis 1 (L1) kalkulált áramerősség",
                "icon": "mdi:current-ac"
            },
            "calculated_power_phase_l1": {
                "unit": "kW",
                "friendly_name": "Számított teljesítmény L1",
                "icon": "mdi:flash"
            },
            "power_factor_l1": {
                "unit": "",
                "friendly_name": "Teljesítménytényező (L1)",
                "icon": "mdi:cosine-wave"
            },
            "active_power_import": {
                "unit": "kW",
                "friendly_name": "Importált teljesítmény",
                "icon": "mdi:flash"
            },
            "reactive_power_qi": {
                "unit": "kVAr",
                "friendly_name": "Reaktív teljesítmény QI (induktív)",
                "icon": "mdi:sine-wave"
            },
            "frequency": {
                "unit": "Hz",
                "friendly_name": "Frekvencia",
                "icon": "mdi:waveform"
            },
            "meter_serial_number": {
                "unit": "",
                "friendly_name": "Mérő sorozatszáma",
                "icon": "mdi:identifier"
            }
        }
}
}

def get_product_list():
    """Return list of available products for dropdown."""
    return [(key, config["name"]) for key, config in PRODUCT_CONFIGS.items()]

def get_product_sensors(product_type):
    """Return sensors configuration for a specific product."""
    return PRODUCT_CONFIGS.get(product_type, {}).get("sensors", {})

def get_product_name(product_type):
    """Return the display name for a product type."""
    return PRODUCT_CONFIGS.get(product_type, {}).get("name", product_type)
