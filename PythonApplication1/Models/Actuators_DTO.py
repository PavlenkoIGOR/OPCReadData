from dataclasses import dataclass
from xmlrpc.client import DateTime

@dataclass
class Actuators_DTO:
    Id : int
    ActuatorName : str
    ActuatorState : str
    SignalDate : DateTime
    EquipmentID : int




