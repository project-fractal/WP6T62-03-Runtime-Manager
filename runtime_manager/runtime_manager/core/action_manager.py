from .logic.exec_factory import Exec_Factory
from ..utility.file_reader import File_Reader
from ..utility.request_maker import Request_Maker
from ..objects.received_info import Received_info
from ..utility.paths import Paths
import json

class Action_Manager: 

    factory = Exec_Factory

    def __init__(self, lb_id = None):
        self.factory = Exec_Factory()
    #  _lb_id is protected, hence it can only be accessed through the getters and setters defined below
        self._lb_id = lb_id 


    def __is_load_balancing__(self):
        print("[Action_Manager] - calling the Load Balancer for info", flush=True)
        lb_flag = False

        #   call Load Balancer with POST request
        lb_info = json.loads(File_Reader.read_file(Paths.LOAD_BALANCER.value))
        res = json.loads(Request_Maker.make_request(lb_info['protocol'], lb_info['ip'], lb_info['port'], lb_info['endpoint']))
        
        print("[Action_Manager] - Load Balancer returned node ID:", res['id_node'], flush=True)

        if res['id_node'] is not None:
            self._lb_id= res['id_node']    
            lb_flag = True
        
        return lb_flag  #   False: not load balancing, we can execute at home
                        #   True: load balancing, we must execute on different node


    def choose_exec(self, received_info): 
    #   Short-circuit evaluation: this conditional statement does not call is_load_balancing if is_lb is True
        if (received_info.is_load_balancing or not self.__is_load_balancing__()): #   in questo caso entriamo se possiamo eseguire a casa/ is_load_balacing ritorna False
            return self.factory.create("home", received_info.id_flow, received_info.payload)
        else:
            return self.factory.create("lb", str(self._lb_id), received_info) # if we are in this case, then necessarily _lb_id has a valid value
        

    @property
    def lb_id(self):
        print("Getting the value of _lb_id ...")
        return self._lb_id

    @lb_id.setter
    def lb_id(self, value):
        print("Setting the value of _lb_id ...")
        self._lb_id = value

