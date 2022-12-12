from .strategy import Strategy

class Context():

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        #   The Context maintains a reference to one of the Strategy objects. The
        #   Context does not know the concrete class of a strategy. It should work
        #   with all strategies via the Strategy interface.

        return self._strategy

    @strategy.setter    #   allows replacing a Strategy object at runtime.
    def strategy(self, strategy: Strategy) -> None:

        self._strategy = strategy

    def do_logic(self, *args) -> None:
        self._strategy.do_algorithm(*args)
