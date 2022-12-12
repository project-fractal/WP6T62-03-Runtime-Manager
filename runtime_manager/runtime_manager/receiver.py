from .core.action_dispatcher import Action_dispatcher
from .objects.received_info import Received_info
from flask import request
from flask_restful import Resource
import json


class Receiver(Resource):

    def __init__(self):
        pass

    def post(self):
        print("\n\n[rm_api -> Receiver] - received POST request", flush=True)
        received = Received_info()
        req = request.get_json()
        received.is_load_balancing = req['is_load_balancing']
        received.payload = req['payload']
        received.id_flow = req['id_flow']
        self.__run__(received)
        return 200  # return 200 OK code

    def mqtt(self, msg):
        print("\n\n[rm_mqtt -> Receiver] - triggered by MQTT", flush=True)
        try:
            msg_s = json.loads(msg.payload.decode("utf-8"))
            print("msg_s= ", msg_s)
            received = Received_info()
            received.id_flow = msg_s['id_flow']  
            received.payload = msg_s['payload'] 
            self.__run__(received)
        except json.decoder.JSONDecodeError:
            print("[rm_mqtt -> Receiver] - error decoding json message", flush=True)

    def __run__(self, received_info):
        print("[Receiver] - sending message to Action_dispatcher", flush=True)
        Action_dispatcher.dispatch(received_info)




