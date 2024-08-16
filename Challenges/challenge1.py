#  Represent stock as a class


class Stock:
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company
    
    def get_description(self):
        return f'{self.ticker}: {self.company} -- ${self.price}'