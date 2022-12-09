from abc import ABC, abstractmethod

class AbstractBoard(ABC):
    def __init__(self, length =4, width=4): # accept width and length in constructor
        self.length: int = length
        self.width: int = width

    @abstractmethod
    def get_length(self):
        pass

    @abstractmethod
    def get_width(self):
        pass

class TableTop(AbstractBoard):
    def get_length(self):
        return self.length

    def get_width(self):
        return self.width


