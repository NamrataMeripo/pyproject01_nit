class parrot :
    
    def fly(self) :
        print("Parrot can fly")
    
    def swim(self) :
        print("parrot cant swim")

class penguin ():

    def fly(self) :
        print("Penguin cant fly")
    
    def swim(self):
        print("Penguin can swim")
    

#common interface

def flying(bird) :
    bird.fly ()

def swimming(bird):
    bird.swim ()

# Instantiate objects 

blu = parrot ()
peggy = penguin ()

# Passing the objects
flying(blu)
flying(peggy)

swimming(blu)
swimming(peggy)



# Example 2
class Animal :
    
    def __init__(self, name):
        self.name = name

    def talk(self) :
        print(self.name, "Welcome to Animal kingdom")

class cat(Animal) :

    def talk(self) :
        print(self.name,"Meow !")
    
class dog(Animal) :
    def talk (self) :
        print(self.name,"Woof !")

a = Animal("Lion")
a.talk ()

b= cat("Missy")
b.talk ()

c=dog ("Rodder")
c.talk ()


#Example 3