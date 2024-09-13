import sys
import os
sys.path.append(r"D:\VSProjects\Python\PythonApplication1\PythonApplication1")
from Repository.EntitiesRepo import EntitiesRepo
from Services.ConnectionMaker import ConnectionMaker
from typing import List, Optional
from flask import Flask, render_template
from flask import jsonify

from Models.ORG_DTO import ORG_DTO
from Models.Equipment_DTO import Equipment_DTO
from Models.Actuator_DTO import Actuator_DTO

app = Flask(__name__)

@app.route('/')
def hellYear():
    connectionMaker = ConnectionMaker()
    entities = EntitiesRepo(connectionMaker)

    organizations : List[ORG_DTO] = [] 
    equipment : List[Equipment_DTO] = []
    actuators : List[Actuator_DTO] = []
    
    organizations = entities.GetOrganizations() or []
    equipment = entities.GetEquipment() or []
    actuators = entities.GetActuators() or []
    
    
    #can be improved by using a dictionary
    for equip in equipment:
        for actuator in actuators:
            if actuator.Id == equip.Id:
                equip.Actuators.append(actuator)

    for org in organizations:
        for equip in equipment:
            if equip.OrgID == org.ORG_id:
                org.Equipment.append(equip)
    
    # return organizations
    # return jsonify(organizations) #âîçâðàò â ôîðìàòå JSON
    return render_template('Home.html', organizations=organizations, equipment=equipment, actuators=actuators)

    
if __name__ == "__main__":
    app.run(debug = True)

