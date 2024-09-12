import sys
import os
sys.path.append(r"D:\VSProjects\Python\PythonApplication1\PythonApplication1")
from main import EntitiesRepo
from main import ConnectionMaker

from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

@app.route('/home')
def hellYear():
    connectionMaker = ConnectionMaker()
    entities = EntitiesRepo(connectionMaker)

    organizations = []
    organizations = entities.GetOrganizations()
    # return organizations
    return jsonify(organizations)
    # return render_template('Home.html', organizations=organizations)

    
if __name__ == "__main__":
    app.run(debug = True)

