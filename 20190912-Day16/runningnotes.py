info = "Welcome to the python world"
def bigdata() :
    global info
    print(info)
    info = "Hello there!"
    return 

bigdata ()  # First call
print(info) # Second call




level = "you are in levels"

def game() :
    global level
    print("Global:",level)
    level = "Enter next level"
    print("Firstone:",level)
    level = "Goto another level"
    print("Secondone:",level)
    return game

game ()
print("lastcapture:",level)



carinfo = "Welcome to the world of cars"

def cars() :
    global carinfo 
    print(carinfo)
    carinfo = "Here are local cars"
    return

cars ()
print(carinfo)