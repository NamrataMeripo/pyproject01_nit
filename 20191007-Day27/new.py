class Car (object):

    def __init__(self):
        print("I am in Car instance")
      
    
    def drive(self) :
        print("I am driving self")

    def stop(self):
        print("I will stop")


class Benz(Car) :
    def __init__(self):
        Car.__init__(self)

c1 = Car()
c1.drive ()

b = Benz ()
b.drive ()
b.stop ()