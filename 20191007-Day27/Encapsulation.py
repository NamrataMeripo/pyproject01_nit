class computer :  # Class creation
    
    def __init__(self): 
        self.__maxprice = 900   # private attribute

    def sell(self) :
        print("Selling price : {} ".format(self.__maxprice)) #private

    def setmaxprice (self,price) :
        self.__maxprice = price  #private

c = computer ()
c.sell ()

#  change of price
c.__maxprice = 1000
c.sell ()

# using setter function
c.setmaxprice(1000)
c.sell ()

c.setmaxprice (5000)
c.sell ()

