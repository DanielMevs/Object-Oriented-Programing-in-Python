class Item:
    def __init__(self, item_type, price):
        self.item_type = item_type
        self._price = price

    @property
    def price(self):
        return self._price

class Cake(Item):
    def __init__(self, flavor, price, slices):
        super().__init__("cake", price)
        self.flavor = flavor
        self.slices = slices
        self.slices_remaining = slices

    def sell(self, count): 
        if(count <= 0):
            return "Cannot sell zero or negative slices!"
        elif(self.slices_remaining - count < 0):
            return f"Cannot sell more slices than we have ({self.slices_remaining})!"
        else:
            self.slices_remaining -= count
            return f"This cake has {self.slices_remaining} slices remaining."

    def __eq__(self, other) -> bool:
        return self.slices_remaining * (self.price / self.slices) == other.slices_remaining * (other.price / other.slices)
    
    def __gt__(self, other) -> bool:
        return self.slices_remaining * (self.price / self.slices) > other.slices_remaining * (other.price / other.slices)
    
    def __lt__(self, other) -> bool:
        return self.slices_remaining * (self.price / self.slices) < other.slices_remaining * (other.price / other.slices)
    


spice_cake = Cake("spice", 18, 8)
chocolate_cake = Cake("chocolate", 24, 6)

spice_cake.sell(3)
chocolate_cake.sell(4)
