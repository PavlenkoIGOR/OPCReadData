from argparse import OPTIONAL
from dataclasses import dataclass
from typing import List, Optional
from Models.Actuator_DTO import Actuator_DTO

@dataclass
class Equipment_DTO:
    Id : int
    EquipmentName : str
    OrgID : int
    Actuators: Optional[List[Actuator_DTO]] = None

    def __post_init__(self):
        if self.Actuators is None:
            self.Actuators = []



