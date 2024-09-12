from ast import Import
from dataclasses import dataclass
from typing import List, Optional
from Models.Equipment_DTO import Equipment_DTO

@dataclass
class ORG_DTO:
    
    ORG_id : int
    ORG_name : str
    Equipment: Optional[List[Equipment_DTO]] = None

    def __post_init__(self):
        if self.Equipment is None:
            self.Equipment = []  # Инициализация пустого списка