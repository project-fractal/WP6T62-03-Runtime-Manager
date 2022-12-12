from abc import ABC, abstractmethod
from typing import List

class Strategy(ABC):

    @abstractmethod
    def do_algorithm(self, *args):
        pass