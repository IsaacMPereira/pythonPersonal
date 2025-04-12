from abc import ABC, abstractmethod

__all__ = ['Vehicle']

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def notabs(self):
        print("Not abs method")