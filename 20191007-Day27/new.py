
while True :
    try :
        n1 = int(input("Enter n1 :"))
        n2 = int(input("Enter n2 :"))

        n3 = n1/n2  
        print("result",n3)
    except ZeroDivisionError :
        print("Zero division error")
    
    except ArithmeticError :
        print("Arithematic error")
    
    except SyntaxError :
        print("Syntax error")
    
    else : 
        print("Go to final statement")

    finally :

        print("GoodBye")

