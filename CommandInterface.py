from abc import ABC, abstractmethod


class CommandInterface(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
