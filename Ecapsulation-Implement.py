class Computer: 

    def __init__(self): 
        self.__maxprice = 900 
    
    def sell(self): 
        print("Selling Price: {}".format(self.__maxprice)) 

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()  # Output: Selling Price: 900

# Attempt to change the price directly (won't work due to name mangling)
c.__maxprice = 1000
c.sell()  # Still outputs: Selling Price: 900

# Proper way to change the price using setter
c.setMaxPrice(1000)
c.sell()  # Output: Selling Price: 1000
