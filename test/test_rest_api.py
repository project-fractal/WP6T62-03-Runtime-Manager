import json
import flask
import random

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# ------------ TEST NODES 1, 2, 3 -----------------------------

@app.route('/nodo1', methods=['POST'])
def nodo1():
    qualcosa = json.loads("{\"nodo1_res\":\"something\"}")
    return qualcosa

@app.route('/nodo2', methods=['POST'])
def nodo2():
    qualcosa = json.loads("{\"nodo2_res\":\"something\"}")
    return qualcosa

@app.route('/nodo3', methods=['POST'])
def nodo3():
    qualcosa = json.loads("{\"nodo3_res\":\"something\"}")
    return qualcosa


# ------------ TEST COMPONENTS 1, 2, 3 -------------------------

@app.route('/endpoint1', methods=['GET','POST'])
def endpoint1():
    qualcosa = json.loads("{\"endpoint1_res\":\"something\"}")
    return qualcosa

@app.route('/endpoint2', methods=['GET','POST'])
def endpoint2():
    qualcosa = json.loads("{\"endpoint2_res\":\"something\"}")
    return qualcosa
    
    
# ------------ TEST LOAD BALANCER -----------------------------

@app.route('/LB/id_node', methods=['GET'])
def load_balancer():
    id_node = random.choice([1, 2, 3, None])
    qualcosajson = {"id_node":id_node}
    print(type(qualcosajson))
    return qualcosajson
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)