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
