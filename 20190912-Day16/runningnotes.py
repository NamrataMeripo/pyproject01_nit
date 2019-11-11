info = "welcome to python world"
def bigdata():
    global info
    print(info)
    info = "Hadoop"
    print(info)
    return bigdata

value = "welcome to Bigdata"
bigdata ()
print(info)



level = "you are in levels"

def game() :
    global level
    print(level)
    level = "Enter next level"
    print(level)
    level = "Goto another level"
    print(level)
    return game

game ()
print(level)
