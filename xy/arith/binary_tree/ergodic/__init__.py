from abc import ABC, abstractmethod


class Ergodic(ABC):
    @abstractmethod
    def depth_first_ergodic(self, array):
        pass

    @abstractmethod
    def breadth_first_ergodic(self, array):
        pass


