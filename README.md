# **Runtime Manager**

The Runtime Manager coordinates and manages task scheduling and load balancing operations between modules in one or more FRACTAL nodes at runtime. It performs the scheduling of various operations which are entirely configurable. In addition, it provides load balancing capabilities using the interface with the Load Balancer component, sending the task execution to a different node.  

---

**PRE-REQUISITES**

The Runtime Manager has been developed in Python 3.10.4 and the following list of modules are necessary for its execution:

* Flask 2.1.2
* Flask-RESTful 0.3.9
* Eclipse Paho MQTT Python 1.6.1
* Multipledispatch 0.6.0

Before proceding with the launch of the application and the tests, please cd to the folder containing the file *requirements.txt* and install all the required modules with the following command:    
```
 pip install -r requirements.txt
```
---

**LAUNCH**

The Runtime Manager has two possibile entry points, which serve different purposes:

1. By launching *rm_mqtt.py* you are providing a general way for components to access this Runtime Manager's functionalities.

2. By launching *rm_api.py* you are providing a way for Runtime Managers installed on different nodes to contact this RM module for load balancing situations.
---

**TEST PROCEDURE**

Modify the configuration files inside the folder *config_files* to reflect your needs for the connection details and the data flows. Inside the folder *test*, launch the script *test_rest_api.py*. It will simulate the behaviour of the nodes and the components the Runtime Manager will communicate with.

**MQTT TEST**

This is a test procedure for the MQTT interface. 

1. Launch *rm_mqtt.py* from the folder *runtime_manager*, in order to subscribe to the topic indicated in the configuration file.

2. Launch the script *test_mqtt_publisher.py* to publish a test message on the topic where the Runtime Manager is subscribed.

**REST API TEST**

This is a test procedure for the REST Api interface.

1. Launch *rm_api.py* in order to expose the REST service according to the instructions inside the dedicated configuration file.

2. Use an application such as Postman [https://www.postman.com/downloads/] to simulate a POST request to the Runtime Manager with a JSON of this form:
```
{
    "id_flow": "1",
    "is_load_balancing": true,
    "payload": "0x03abcdefghil"
}
```

---

**ABOUT THE CONFIGURATION FILES**

The five configuration files included inside the directory *config_files* are the following:
* **comm.conf** (containing the configuration for the connection to the mqtt broker, the rest endpoint where the Runtime Manager is exposed, and the path to the log file)
* **components.conf** (containing the information regarding all the components with which the Runtime Manager will communicate)
* **flows.conf** (containing all the flows the Runtime Manager will execute, along with the components it must contact; the latter must correspond to those configured in *components.conf*)
* **load_balancer.conf** (this file contains the configuration the Runtime Manager will use to contact the Load Balancer, when needed)
* **nodes.conf** (containing the information regarding all the nodes the Runtime Manager may have to contact for load balancing purposes)

Except for the file *flows.conf*, the info are in JSON format and the values can be modified accordingly. 

The file containing the data flow information is structured based on the following keywords:

* **TO** - specifies the name of the component and the endpoint to contact
* **POST**/**GET** - the method for the REST request. If the request is a POST, the elements following the keyword are the content of the body.

Each instruction is to be written on a separate line; each data flow process begins with a number associated to it, and ends with a blank line.
