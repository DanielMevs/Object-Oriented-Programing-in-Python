# Convert classes to data classes
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Asset(ABC):
    price: float

    @abstractmethod
    def __lt__(self, other):
        pass


@dataclass
class Stock(Asset):
    ticker: str
    company: str

    def __lt__(self, other):
        return self.price < other.price
    

@dataclass
class Bond(Asset):
    description: str
    duration: int
    yieldamt: float

    def __lt__(self, other):
        return self.yieldamt < other.yieldamt