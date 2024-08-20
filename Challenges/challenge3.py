# Sort stocks
from abc import ABC, abstractmethod


class Asset(ABC):
    def __init__(self, price):
        self.price = price
    
    @abstractmethod
    def __str__(self):
        pass


class Stock(Asset):
    def __init__(self, ticker, price, company):
        super().__init__(price)
        self.ticker = ticker
        self.company = company
    
    def __str__(self):
        return f'{self.ticker}: {self.company} -- ${self.price}'
    
    def __lt__(self, other):
        return self.price < other.price


class Bond(Asset):
    def __init__(self, price, description, duration, yieldamt):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.yieldamt = yieldamt

    def __str__(self):
        return (f'{self.description} :' +
                f'{self.duration}yr : '
                f'${self.price} : {self.yieldamt}'
                )

    def __lt__(self, other):
        return self.yieldamt < other.yieldamt