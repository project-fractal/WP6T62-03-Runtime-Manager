from ..objects.received_info import Received_info
from .action_manager import Action_Manager

class Action_dispatcher:

    # TODO where are the paths of the two configuration files stored?

    # constructor
    def __init__(self):
        pass


    @staticmethod
    def dispatch(received_info):
        print("[Action_dispatcher] - received is_load_balancing:", received_info.is_load_balancing, " id_flow:", received_info.id_flow, " payload:", received_info.payload, flush=True)

        manager = Action_Manager()
 
        exec_type = manager.choose_exec(received_info)
        exec_type.execute()