from typing import List, Dict
from pydantic import BaseModel


class NetworkStatus(BaseModel):
    connection: str
    latency_ms: float
    interface: str


class RealtimeMonitoring(BaseModel):
    internalTemperature_C: float
    outputPower_kW: float
    powerFactor: float
    relayStatus: str
    chargingSessionStatus: str
    outputVoltage_V: float
    outputCurrent_A: float
    networkStatus: NetworkStatus
    activeAlarms: List[str]


class Identification(BaseModel):
    brand: str
    model: str
    serialNumber: str
    chargerType: str
    supportedConnectors: List[str]
    nominalPower_kW: float


class TechnicalSpecifications(BaseModel):
    maxVoltage_V: float
    maxCurrent_A: float
    communicationProtocols: List[str]


class Maintenance(BaseModel):
    installationDate: str
    lastMaintenance: str
    nextScheduledMaintenance: str
    maintenanceResponsible: str


class Location(BaseModel):
    address: str
    gpsCoordinates: Dict[str, float]
    zone: str


class WarrantyStatus(BaseModel):
    isValid: bool
    expiresOn: str


class LegalAndCertifications(BaseModel):
    certifications: List[str]
    warrantyStatus: WarrantyStatus


class StaticData(BaseModel):
    identification: Identification
    technicalSpecifications: TechnicalSpecifications
    maintenance: Maintenance
    location: Location
    legalAndCertifications: LegalAndCertifications


class ChargerData(BaseModel):
    id: str
    staticData: StaticData
    realtimeMonitoring: RealtimeMonitoring
