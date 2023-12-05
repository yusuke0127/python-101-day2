class Bags:
    def __init__(self):
        self.unpacked = False
        self.color = "black"
        
    def is_unpacked(self):
        return self.unpacked
    
    def unpack(self):
        self.unpacked = True


chanel = Bags() #=> creates an instance of the class Car
print(chanel.unpacked)
print(chanel.is_unpacked())
print(chanel.unpack())
print(chanel.is_unpacked())
type(chanel)   #=> __main__.Car