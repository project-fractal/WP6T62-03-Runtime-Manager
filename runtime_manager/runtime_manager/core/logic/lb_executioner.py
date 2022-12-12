from .executioner import Executioner
from .lb_strategy import LB_Strategy
from .context import Context

class LB_Executioner(Executioner, LB_Strategy):

    context = Context
    
    #constructor
    def __init__(self, lb_id, received_info):
        self.context = Context(LB_Strategy())
        self.lb_id = lb_id
        self.received_info = received_info

    def execute(self):
        print("[LB_Executioner] - executing action on different node")
        print("[LB_Executioner] - the ID of the node is " + str(self.lb_id))
        self.context.do_logic(self.lb_id, self.received_info)

