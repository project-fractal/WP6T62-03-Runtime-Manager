'''
This is the entry point for components to contact the Runtime Manager via MQTT
by publishing a json to the topic "component_msg"
'''

from runtime_manager.receiver import Receiver
from runtime_manager.utility.file_reader import File_Reader 
from runtime_manager.utility.paths import Paths
import paho.mqtt.client as mqtt #   pip3 install paho-mqtt
import json

#   The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    #   Subscribing in on_connect() means that if we lose the connection and
    #   reconnect then subscriptions will be renewed.
    client.subscribe(json.loads((File_Reader.read_file(Paths.COMM.value)))['mqtt']['topic'])

#   The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    receiver = Receiver()
    receiver.mqtt(msg=msg)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(json.loads((File_Reader.read_file(Paths.COMM.value)))['mqtt']['host'], 
    json.loads((File_Reader.read_file(Paths.COMM.value)))['mqtt']['port'], 
    json.loads((File_Reader.read_file(Paths.COMM.value)))['mqtt']['keepalive'])

if __name__ == '__main__':
    client.loop_forever()