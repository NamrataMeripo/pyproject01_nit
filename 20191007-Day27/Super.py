
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

