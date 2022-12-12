from .executioner import Executioner
from .home_strategy import Home_Strategy
from .context import Context

class Home_Executioner(Executioner, Home_Strategy):

    context = Context

    #constructor
    def __init__(self, id_flow=None, payload=None):
        self.context = Context(Home_Strategy())
        self.id_flow = id_flow
        self.payload = payload

    def execute(self):
        print("[Home_Executioner] - executing action here")
        print("[Home_Executioner] - the ID of the flow to be executed is " + str(self.id_flow))
        print("[Home_Executioner] - payload is " + str(self.payload))
        self.context.do_logic(self.id_flow, self.payload)