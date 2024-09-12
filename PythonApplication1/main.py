from multiprocessing import connection
from sqlite3 import Cursor
from uu import decode

from Models.ORG_DTO import ORG_DTO
from Models.Equipment_DTO import Equipment_DTO
from Models.Actuator_DTO import Actuator_DTO


from Services.ConnectionMaker import ConnectionMaker
from Repository.EntitiesRepo import EntitiesRepo



def GetEntities():
    connectionMaker = ConnectionMaker()
    enttitiesRepo = EntitiesRepo(connectionMaker)
    
    organizations = []
    equipment = []
    actuators = []
    
    organizations = enttitiesRepo.GetOrganizations()
    equipment = enttitiesRepo.GetEquipment()
    actuators = enttitiesRepo.GetActuators()
          

        
    for actuator in actuators:
        actuatorDTO = Actuator_DTO(Id=actuator.Id, ActuatorName=actuator.ActuatorName, ActuatorState=actuator.ActuatorState, SignalDate=actuator.SignalDate, EquipmentID=actuator.EquipmentID)
        print(f"Equipment ID: {actuatorDTO.Id} Name: {actuatorDTO.ActuatorName} State: {actuatorDTO.ActuatorState}")
        
    for equip in equipment:
        equipmentDTO = Equipment_DTO(Id=equip.Id, EquipmentName=equip.EquipmentName, OrgID=equip.OrgID, Actuators=actuators)
        print(f"Equipment ID: {equipmentDTO.Id} Name: {equipmentDTO.EquipmentName}")
        
    for org in organizations:
        organization = ORG_DTO(ORG_id=org.ORG_id, ORG_name=org.ORG_name, Equipment=equipment)
        print(f"Organization ID: {organization.ORG_id} Name: {organization.ORG_name} Equipment {organization.Equipment}")
    


def main():
    # ConnectToDB()
    GetEntities()
    
    
if __name__ == "__main__":
    main()
    