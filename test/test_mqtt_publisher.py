import paho.mqtt.client as paho
import json

broker= #broker ip here
port= #broker port here

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
    
client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection
msg = {"id_flow": "1", "payload": "0x03abcdefghil"}
ret= client1.publish('component_msg', json.dumps(msg))     #   publish
