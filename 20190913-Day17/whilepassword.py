password = ""

while password != 'RedHat':
    password = str(input("Enter the password :- "))
    if password == 'RedHat':
        print("correct password")
    elif password == 'Admin@123' :
        print("enter another password")
    elif password == 'Welcome123' :
        print("only 2 attemps left")
    elif password == 'Welcomeabc':
        print("only one attempt remaining")
    else :
        print("Incorrect password - Account expired")
        break
    print(password)