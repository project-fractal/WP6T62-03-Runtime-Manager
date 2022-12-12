from .home_executioner import Home_Executioner
from .lb_executioner import LB_Executioner

class Exec_Factory:

    #constructor
    def __init__(self):
        pass

    def create(self, type, *args):

        types = {
            "home" : Home_Executioner,
            "lb" : LB_Executioner
        }   
        return types[type](*args)

