from abc import ABC, abstractmethod

class Executioner(ABC):

    @abstractmethod
    def execute(self):
        pass