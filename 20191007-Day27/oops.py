# Example 1
'''
class Bird ():
    pass
abc = Bird ()
'''
'''
# Example 2
class Bird () :  # Creating class 

    species = " Birdrace"  # creating class attribute

    def __init__(self, name, age): # creating instance attribute
        self.name = name
        self.age = age


flybird = Bird("Parrot",10)
print(flybird.__class__.species)
print(flybird.name,flybird.age)


# Example 3

class Flowers () : # Creating class

    species = "Plants race"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    

fragrance = Flowers("Bluebonnets",4)
print(fragrance.__class__.species)
print(fragrance.name,fragrance.age)

'''

'''
# Example 4 Instance methods

class Bird () :

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sing(self,song):
        return "{} singing {}" .format(self.name,song)
    def dance(self) :
        return "{} is now dancing ".format(self.name)
    

abird1 = Bird("Parrot",3)
print(abird1.sing("Hoooohaaaaaaaa......"))
print(abird1.dance())
'''

########### Inheritance
# Example 5 - Parent class and child class
'''
        # Parent class
class Bird () :
    def __init__(self,name,age):
        print("Bird is ready")
    def whoisthis(self) :
        print("Bird")
    def swim (self) :
        print("Swim faster")
    
       # Child class
class Penguin(Bird) :
    def __init__(self, name, age):
        super().__init__(name, age)
        print("Penguin is ready")

    def whoisthis(self):
        print("Penguin")

    def swim(self):
        super().swim()

peggy = Penguin ("Parrot",5)
peggy.swim ()
peggy.whoisthis()

'''

'''
# Super function 
class Person () :
    
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    def printname(self) :
        print(self.firstname,self.lastname)
    
aperson = Person('Guido','Rossum')
aperson.printname ()


class student(Person) :

    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.graduation = year

    def welcome(self) :
        print("Welcome",self.firstname,self.lastname,"to the class of ",self.graduation)

x1 = student("Guido","Rossum",2019)
print(x1.welcome())

'''

''' Encapsulation '''

