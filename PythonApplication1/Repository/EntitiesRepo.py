import psycopg2
from Models.ORG_DTO import ORG_DTO
from Models.Equipment_DTO import Equipment_DTO
from Models.Actuator_DTO import Actuator_DTO
from Services.ConnectionMaker import ConnectionMaker

class EntitiesRepo:
    
    def __init__(self, connectionMaker):
        self.connectionMaker = connectionMaker

    def GetOrganizations(self):
        
        connectionDB = self.connectionMaker.MakeConnection()
        fetched_organizations = []
        organizations = []
        
        if connectionDB:
             with connectionDB.cursor() as cursor:
                  cursor.execute("select * from \"Organizations\"")
                  fetched_organizations = cursor.fetchall()
             connectionDB.close() #закрытие соединения
             
             for item in fetched_organizations:
                 OrgDto = ORG_DTO(ORG_id = item[0], ORG_name = item[1])
                 organizations.append(OrgDto)
                 
             return organizations
        else:
            return None
        
        
    def GetEquipment(self):
        
        connectionDB = self.connectionMaker.MakeConnection()
        
        fetched_equipment = []
        equipment = []
        
        if connectionDB:
             with connectionDB.cursor() as cursor:
                  cursor.execute("select * from \"Equipment\"")
                  fetched_equipment = cursor.fetchall()
             connectionDB.close() #закрытие соединения
             
             for item in fetched_equipment:
                 equipmentDto = Equipment_DTO(Id = item[0], EquipmentName = item[1], OrgID=item[2])
                 equipment.append(equipmentDto)
                 
             return equipment
        else:
            return None
        

    def GetActuators(self):
        
        connectionDB = self.connectionMaker.MakeConnection()
        
        fetched_actuators = []
        actuators = []
        
        if connectionDB:
             with connectionDB.cursor() as cursor:
                  cursor.execute("select * from \"Actuators\"")
                  fetched_actuators = cursor.fetchall()
             connectionDB.close() #закрытие соединения
             
             for item in fetched_actuators:
                 actuatorDto = Actuator_DTO(Id = item[0],  ActuatorName = item[1], ActuatorState = item[2], SignalDate = item[3], EquipmentID=item[4])
                 actuators.append(actuatorDto)
                 
             return actuators
        else:
            return None

