"""Product configuration for ADA family devices."""

# Product definitions with their supported sensors
# ignored entries pziot-e02: username, password, wifi_ssid, local_ip, os_version, mac_address, cosem_logical_device_name,
# ignored entries ada one: username, password, os_version, local_ip, cosem_logical_device_name, client_id, current_tariff, timestamp
PRODUCT_CONFIGS = {
    "ada12": {
        "name": "ADA P1 Meter / ADA P1 Bridge",
        "description": "Full-featured smart meter with all sensors",
        "host": "okosvillanyora.local / adabridge.local",
        "default_port": 8989,
        "sensors": {
        # Összesített energia
        "active_import_energy_total": {
            "unit": "kWh",
            "hu": "Összes importált energia",
            "en" : "Total Imported Energy",
            "icon": "mdi:transmission-tower-import"
        },
        "active_export_energy_total": {
            "unit": "kWh",
            "hu": "Összes exportált energia",
            "en" : "Total Exported Energy",
            "icon": "mdi:transmission-tower-export"
        },
        "total_active_energy": {
            "unit": "kWh",
            "hu": "Összes aktív energia",
            "en" : "Total Active Energy",
            "icon": "mdi:lightning-bolt"
        },

        # Tarifa szerinti bontás
        "active_import_energy_tariff_1": {
            "unit": "kWh",
            "hu": "Importált energia tarifa 1",
            "en" : "Imported Energy Tariff 1",
            "icon": "mdi:counter"
        },
        "active_import_energy_tariff_2": {
            "unit": "kWh",
            "hu": "Importált energia tarifa 2",
            "en" : "Imported Energy Tariff 2",
            "icon": "mdi:counter"
        },
        "active_import_energy_tariff_3": {
            "unit": "kWh",
            "hu": "Importált energia tarifa 3",
            "en" : "Imported Energy Tariff 3",
            "icon": "mdi:counter"
        },
        "active_import_energy_tariff_4": {
            "unit": "kWh",
            "hu": "Importált energia tarifa 4",
            "en" : "Imported Energy Tariff 4",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_1": {
            "unit": "kWh",
            "hu": "Exportált energia tarifa 1",
            "en" : "Exported Energy Tariff 1",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_2": {
            "unit": "kWh",
            "hu": "Exportált energia tarifa 2",
            "en" : "Exported Energy Tariff 2",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_3": {
            "unit": "kWh",
            "hu": "Exportált energia tarifa 3",
            "en" : "Exported Energy Tariff 3",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_4": {
            "unit": "kWh",
            "hu": "Exportált energia tarifa 4",
            "en" : "Exported Energy Tariff 4",
            "icon": "mdi:counter"
        },

        # Reaktív energia (kVArh)
        "reactive_import_energy": {
            "unit": "kVArh",
            "hu": "Reaktív importált energia",
            "en" : "Reactive Imported Energy",
            "icon": "mdi:sine-wave"
        },
        "reactive_export_energy": {
            "unit": "kVArh",
            "hu": "Reaktív exportált energia",
            "en" : "Reactive Exported Energy",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qi": {
            "unit": "kVArh",
            "hu": "Reaktív energia QI",
            "en" : "Reactive Energy QI",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qii": {
            "unit": "kVArh",
            "hu": "Reaktív energia QII",
            "en" : "Reactive Energy QII",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qiii": {
            "unit": "kVArh",
            "hu": "Reaktív energia QIII",
            "en" : "Reactive Energy QIII",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qiv": {
            "unit": "kVArh",
            "hu": "Reaktív energia QIV",
            "en" : "Reactive Energy QIV",
            "icon": "mdi:sine-wave"
        },

        # Pillanatnyi teljesítmény
        "instantaneous_power_import": {
            "unit": "kW",
            "hu": "Pillanatnyi importált teljesítmény",
            "en" : "Instantaneous Imported Power",
            "icon": "mdi:flash"
        },
        "instantaneous_power_export": {
            "unit": "kW",
            "hu": "Pillanatnyi exportált teljesítmény",
            "en" : "Instantaneous Exported Power",
            "icon": "mdi:flash"
        },
        "instantaneous_power_import_l1": {
            "unit": "kW",
            "hu": "Importált teljesítmény L1",
            "en" : "Instantaneous Imported Power L1",
            "icon": "mdi:flash"
        },
        "instantaneous_power_import_l2": {
            "unit": "kW",
            "hu": "Importált teljesítmény L2",
            "en" : "Instantaneous Imported Power L2",
            "icon": "mdi:flash"
        },
        "instantaneous_power_import_l3": {
            "unit": "kW",
            "hu": "Importált teljesítmény L3",
            "en" : "Instantaneous Imported Power L3",
            "icon": "mdi:flash"
        },
        "instantaneous_power_export_l1": {
            "unit": "kW",
            "hu": "Exportált teljesítmény L1",
            "en" : "Instantaneous Exported Power L1",
            "icon": "mdi:flash"
        },
        "instantaneous_power_export_l2": {
            "unit": "kW",
            "hu": "Exportált teljesítmény L2",
            "en" : "Instantaneous Exported Power L2",
            "icon": "mdi:flash"
        },
        "instantaneous_power_export_l3": {
            "unit": "kW",
            "hu": "Exportált teljesítmény L3",
            "en" : "Instantaneous Exported Power L3",
            "icon": "mdi:flash"
        },

        # Pillanatnyi reaktív teljesítmény
        "instantaneous_reactive_power_qi": {
            "unit": "kVAr",
            "hu": "Reaktív teljesítmény QI",
            "en" : "Instantaneous Reactive Power QI",
            "icon": "mdi:sine-wave"
        },
        "instantaneous_reactive_power_qii": {
            "unit": "kVAr",
            "hu": "Reaktív teljesítmény QII",
            "en" : "Instantaneous Reactive Power QII",
            "icon": "mdi:sine-wave"
        },
        "instantaneous_reactive_power_qiii": {
            "unit": "kVAr",
            "hu": "Reaktív teljesítmény QIII",
            "en" : "Instantaneous Reactive Power QIII",
            "icon": "mdi:sine-wave"
        },
        "instantaneous_reactive_power_qiv": {
            "unit": "kVAr",
            "hu": "Reaktív teljesítmény QIV",
            "en" : "Instantaneous Reactive Power QIV",
            "icon": "mdi:sine-wave"
        },

        # Feszültségek
        "voltage_phase_l1": {
            "unit": "V",
            "hu": "Feszültség L1",
            "en" : "Voltage Phase 1 (L1)",
            "icon": "mdi:flash"
        },
        "voltage_phase_l2": {
            "unit": "V",
            "hu": "Feszültség L2",
            "en" : "Voltage Phase 2 (L2)",
            "icon": "mdi:flash"
        },
        "voltage_phase_l3": {
            "unit": "V",
            "hu": "Feszültség L3",
            "en" : "Voltage Phase 3 (L3)",
            "icon": "mdi:flash"
        },

        # Áramerősségek
        "current_phase_l1": {
            "unit": "A",
            "hu": "Áramerősség L1",
            "en" : "Current Phase 1 (L1)",
            "icon": "mdi:current-ac"
        },
        "current_phase_l2": {
            "unit": "A",
            "hu": "Áramerősség L2",
            "en" : "Current Phase 2 (L2)",
            "icon": "mdi:current-ac"
        },
        "current_phase_l3": {
            "unit": "A",
            "hu": "Áramerősség L3",
            "en" : "Current Phase 3 (L3)",
            "icon": "mdi:current-ac"
        },
        "current_phase_Bl1": {
            "unit": "A",
            "hu": "Áramerősség Bl1",
            "en" : "Current Phase 1 (calculated) (L1)",
            "icon": "mdi:current-ac"
        },
        "current_phase_Bl2": {
            "unit": "A",
            "hu": "Áramerősség Bl2",
            "en" : "Current Phase 2 (calculated) (L2)",
            "icon": "mdi:current-ac"
        },
        "current_phase_Bl3": {
            "unit": "A",
            "hu": "Áramerősség Bl3",
            "en" : "Current Phase 3 (calculated) (L3)",
            "icon": "mdi:current-ac"
        },

        # Frekvencia
        "frequency": {
            "unit": "Hz",
            "hu": "Hálózati frekvencia",
            "en" : "Frequency",
            "icon": "mdi:sine-wave"
        },

        # Teljesítménytényező
        "power_factor": {
            "unit": "",
            "hu": "Teljesítménytényező",
            "en" : "Power Factor",
            "icon": "mdi:cosine-wave"
        },
        "power_factor_l1": {
            "unit": "",
            "hu": "Teljesítménytényező L1",
            "en" : "Power Factor (L1)",
            "icon": "mdi:cosine-wave"
        },
        "power_factor_l2": {
            "unit": "",
            "hu": "Teljesítménytényező L2",
            "en" : "Power Factor (L2)",
            "icon": "mdi:cosine-wave"
        },
        "power_factor_l3": {
            "unit": "",
            "hu": "Teljesítménytényező L3",
            "en" : "Power Factor (3)",
            "icon": "mdi:cosine-wave"
        },

        # Egyéb
        "meter_serial_number": {
            "unit": "",
            "hu": "Mérő sorozatszáma",
            "en" : "Meter Serial Number",
            "icon": "mdi:identifier"
        },
        "circuit_breaker_status": {
            "unit": "",
            "hu": "Kismegszakító állapot",
            "en" : "Circuit Breaker Status",
            "icon": "mdi:toggle-switch"
        },
        "current_tariff": {
            "unit": "",
            "hu": "Aktív tarifa",
            "en" : "Current Tariff",
            "icon": "mdi:calendar"
        },
        "timestamp": {
            "unit": "",
            "hu": "Időbélyeg",
            "en" : "Timestamp",
            "icon": "mdi:clock-outline"
        },

        # --- PLUGINS (Gáz) ---
        "plugin_GAS_valve_01": {
            "unit": "",
            "hu": "Gáz érték",
            "en": "Gas value",
            "icon": "mdi:clock"
        },
        "plugin_GAS_type_01": {
            "unit": "",
            "hu": "Gáz tipus",
            "en": "Gas type",
            "icon": "mdi:fire"
        },
        "plugin_GAS_total_01": {
            "unit": "m³",
            "hu": "Gázmérő állása",
            "en": "Gas Meter Total",
            "icon": "mdi:fire"
        },
        "plugin_GAS_timestamp_01": {
            "unit": "",
            "hu": "Gázmérő időbélyeg",
            "en": "Gas Meter Timestamp",
            "icon": "mdi:fire"
        },
        "plugin_GAS_serial_01": {
            "unit": "",
            "hu": "Gázmérő sorozatszám",
            "en": "Gas Meter Serial",
            "icon": "mdi:fire"
        },
        # --- PLUGINS (Viz) ---
        "plugin_WATER_type_02": {
            "unit": "m³",
            "hu": "Vízmérő tipus",
            "en": "Water Meter type",
            "icon": "mdi:water"
        },
        "plugin_WATER_total_02": {
            "unit": "m³",
            "hu": "Vízmérő állása",
            "en": "Water Meter Total",
            "icon": "mdi:water"
        },
        "plugin_WATER_timestamp_02": {
            "unit": "",
            "hu": "Vízmérő időbélyeg",
            "en": "Water Meter Timestamp",
            "icon": "mdi:water"
        },
        "plugin_WATER_serial_02": {
            "unit": "",
            "hu": "Vízmérő sorozatszám",
            "en": "Water Meter Serial",
            "icon": "mdi:water"
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
                "hu": "Összes importált energia",
                "en" : "Total Imported Energy",
            "icon": "mdi:transmission-tower-import"
            },
            "active_export_energy_total": {
                "unit": "kWh",
                "hu": "Összes exportált energia",
                "en" : "Total Exported Energy",
            "icon": "mdi:transmission-tower-export"
            },
            "total_active_energy": {
                "unit": "kWh",
                "hu": "Összes aktív energia",
                "en" : "Total Active Energy",
            "icon": "mdi:transmission-tower-import"
            },
            "power_factor": {
                "unit": "",
                "hu": "Teljesítménytényező",
                "en" : "Power Factor",
            "icon": "mdi:cosine-wave"
            },
            "power_factor_l1": {
                "unit": "",
                "hu": "Teljesítménytényező (L1)",
                "en" : "Power Factor (L1)",
            "icon": "mdi:cosine-wave"
            },
            "power_factor_l2": {
                "unit": "",
                "hu": "Teljesítménytényező (L2)",
                "en" : "Power Factor (L2)",
            "icon": "mdi:cosine-wave"
            },
            "power_factor_l3": {
                "unit": "",
                "hu": "Teljesítménytényező (L3)",
                "en" : "Power Factor (L3)",
            "icon": "mdi:cosine-wave"
            },
            "voltage_phase_l1": {
                "unit": "V",
                "hu": "Fázis 1 (L1) feszültség",
                "en" : "Voltage Phase 1 (L1)",
            "icon": "mdi:flash"
            },
            "voltage_phase_l2": {
                "unit": "V",
                "hu": "Fázis 2 (L2) feszültség",
                "en" : "Voltage Phase 2 (L2)",
            "icon": "mdi:flash"
            },
            "voltage_phase_l3": {
                "unit": "V",
                "hu": "Fázis 3 (L3) feszültség",
                "en" : "Voltage Phase 3 (L3)",
            "icon": "mdi:flash"
            },
            "current_phase_l1": {
                "unit": "A",
                "hu": "Fázis 1 (L1) áramerősség",
                "en" : "Current Phase 1 (L1)",
            "icon": "mdi:current-ac"
            },
            "current_phase_Bl1": {
                "unit": "A",
                "hu": "Fázis 1 (L1) kalkulált áramerősség",
                "en" : "Current Phase 1 (calculated) (L1)",
            "icon": "mdi:current-ac"
            },
            "current_phase_l2": {
                "unit": "A",
                "hu": "Fázis 2 (L2) áramerősség",
                "en" : "Current Phase 2 (L2)",
            "icon": "mdi:current-ac"
            },
            "current_phase_Bl2": {
                "unit": "A",
                "hu": "Fázis 2 (L2) kalkulált áramerősség",
                "en" : "Current Phase 2 (calculated) (L2)",
            "icon": "mdi:current-ac"
            },
            "current_phase_l3": {
                "unit": "A",
                "hu": "Fázis 3 (L3) áramerősség",
                "en" : "Current Phase 3 (L3)",
            "icon": "mdi:current-ac"
            },
            "current_phase_Bl3": {
                "unit": "A",
                "hu": "Fázis 3 (L3) kalkulált áramerősség",
                "en" : "Current Phase 3 (calculated) (L3)",
            "icon": "mdi:current-ac"
            },
            "instantaneous_power_import": {
                "unit": "kW",
                "hu": "Pillanatnyi importált teljesítmény",
                "en" : "Instantaneous Imported Power",
            "icon": "mdi:flash"
            },
            "instantaneous_power_export": {
                "unit": "kW",
                "hu": "Pillanatnyi exportált teljesítmény",
                "en" : "Instantaneous Exported Power",
            "icon": "mdi:flash"
            },
            "meter_serial_number": {
                "unit": "",
                "hu": "Mérő sorozatszáma",
                "en" : "Meter Serial Number",
            "icon": "mdi:identifier"
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
                "hu": "Összes importált energia",
                "en" : "Total Imported Energy",
            "icon": "mdi:transmission-tower-import"
            },
            "voltage_l1": {
                "unit": "V",
                "hu": "Fázis 1 (L1) feszültség",
                "en" : "Voltage Phase 1 (L1)",
            "icon": "mdi:flash"
            },
            "current_phase_l1": {
                "unit": "A",
                "hu": "Fázis 1 (L1) áramerősség",
                "en" : "Current Phase 1 (L1)",
            "icon": "mdi:current-ac"
            },
            "calculated_current_phase_l1": {
                "unit": "A",
                "hu": "Fázis 1 (L1) kalkulált áramerősség",
                "en" : "Current Phase 1 (calculated) (L1)",
            "icon": "mdi:current-ac"
            },
            "calculated_power_phase_l1": {
                "unit": "kW",
                "hu": "Számított teljesítmény L1",
                "en" : "Power Phase 1 (calculated) (L1)",
            "icon": "mdi:flash"
            },
            "power_factor_l1": {
                "unit": "",
                "hu": "Teljesítménytényező (L1)",
                "en" : "Power Factor (L1)",
            "icon": "mdi:cosine-wave"
            },
            "active_power_import": {
                "unit": "kW",
                "hu": "Importált teljesítmény",
                "en" : "Active Power Import",
            "icon": "mdi:flash"
            },
            "reactive_power_qi": {
                "unit": "kVAr",
                "hu": "Reaktív teljesítmény QI (induktív)",
                "en" : "Reactive Power QI (inductive)",
            "icon": "mdi:sine-wave"
            },
            "frequency": {
                "unit": "Hz",
                "hu": "Frekvencia",
                "en" : "Frequency",
            "icon": "mdi:waveform"
            },
            "meter_serial_number": {
                "unit": "",
                "hu": "Mérő sorozatszáma",
                "en" : "Meter Serial Number",
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
