import random
from typing import List

from src.models.mock_models import ChargerData


def generate_mock_data(count: int = 12) -> List[ChargerData]:
    statuses = ["charging", "available", "offline", "maintenance"]
    brands = ["ABB", "Tesla", "ChargePoint", "EVBox"]
    models = ["Terra 54", "Supercharger V3", "Express 250", "Troniq 50"]
    connectors = [["CCS", "CHAdeMO"], ["Type 2", "CCS"]]
    powers = [22, 50, 150, 250]
    voltages = [400, 500, 800]
    currents = [32, 125, 200]

    data = []

    for i in range(count):
        status = statuses[i % len(statuses)]
        is_charging = status == "charging"
        is_offline = status == "offline"
        is_maintenance = status == "maintenance"

        nominal_power = powers[i % len(powers)]
        max_current = currents[i % len(currents)]

        charger = ChargerData(
            id=f"charger-{str(i + 1).zfill(3)}",
            staticData={
                "identification": {
                    "brand": brands[i % len(brands)],
                    "model": models[i % len(models)],
                    "serialNumber": f"SN{random.randint(1000000000, 9999999999)}",
                    "chargerType": "DC Fast" if i % 3 == 0 else "AC Level 2",
                    "supportedConnectors": connectors[i % 2],
                    "nominalPower_kW": nominal_power
                },
                "technicalSpecifications": {
                    "maxVoltage_V": voltages[i % len(voltages)],
                    "maxCurrent_A": max_current,
                    "communicationProtocols": ["OCPP 1.6", "Modbus", "Ethernet", "WiFi"]
                },
                "maintenance": {
                    "installationDate": "2023-04-15",
                    "lastMaintenance": "2024-12-01",
                    "nextScheduledMaintenance": "2025-06-01",
                    "maintenanceResponsible": "Ing. Laura Gómez"
                },
                "location": {
                    "address": f"Estación {i + 1}, Zona Industrial",
                    "gpsCoordinates": {
                        "latitude": 19.432608 + (random.random() - 0.5) * 0.1,
                        "longitude": -99.133209 + (random.random() - 0.5) * 0.1
                    },
                    "zone": f"Zona {chr(65 + (i % 4))}"
                },
                "legalAndCertifications": {
                    "certifications": ["NOM-EM-005", "CE", "UL"],
                    "warrantyStatus": {
                        "isValid": True,
                        "expiresOn": "2026-04-15"
                    }
                }
            },
            realtimeMonitoring={
                "internalTemperature_C": 25 + random.random() * 30,
                "outputPower_kW": random.random() * nominal_power if is_charging else 0,
                "powerFactor": 0.95 + random.random() * 0.05,
                "relayStatus": "OFF" if is_offline else "ON",
                "chargingSessionStatus": status,
                "outputVoltage_V": 380 + random.random() * 40,
                "outputCurrent_A": random.random() * max_current if is_charging else 0,
                "networkStatus": {
                    "connection": "offline" if is_offline else "online",
                    "latency_ms": 80 + random.random() * 100,
                    "interface": "Ethernet" if i % 2 == 0 else "WiFi"
                },
                "activeAlarms": ["Temperatura alta"] if is_maintenance else []
            }
        )

        data.append(charger)

    return data
