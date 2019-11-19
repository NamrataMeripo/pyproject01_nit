

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
