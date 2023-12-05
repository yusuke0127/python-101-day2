# Define Furnitures and its attributes
# Define Orders and its attributes
# Define a method to add a Furniture to an Order
# Define a method to recover the total price of the order

class Furniture:
    def __init__(self, name, price, weight) -> None:
        self.name = name
        self.price = price
        self.weight = weight
        
class Order:
    def __init__(self, country, zip_code) -> None:
        self.country = country
        self.zip_code = zip_code
        self.furnitures = []
    
    def add_furniture(self, furniture):
        self.furnitures.append(furniture)
        
    def total_price(self):
        total_price = 0
        for furniture in self.furnitures:
            total_price += furniture.price
        return total_price
    
    
o = Order('Belgium', 1000)
o.add_furniture(Furniture('TEKI', 42.00, 9.00))
print(o.furnitures)
o.add_furniture(Furniture('GAMLARED', 108.50, 13.00))
print(o.furnitures)

# Final Price
print(o.total_price())  # 150.50
    