

def info(name,age) :
    print("Name : ",name)
    print("Age : ", age)
    return

info(50,'Guido')


def car(a,b,c):
    if a == b :
        print("This is true")
    elif b == c:
        print("This is also true")
    elif a == c:
        print("This is also also true")
    else :
        print("Everything is false , now exit - Good Bye")
    

values = car("1","2","2")


def van(a,*more) :
    print(a)
    print(more)
    print("")
    return

values=van('namrata','nam','sam','mam','dam','tam','vam','kam')
print(values)

