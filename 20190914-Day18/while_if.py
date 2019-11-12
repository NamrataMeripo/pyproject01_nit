password = ""

while password != "redhat" :
    password = input("Enter the password :")
    if password == "redhat" :
        print("correctpassword")
    elif password == "admin@123" :
        print("It was previously used password")
    elif password == "redhat@123":
        print("This is your recent changed password")
    else :
        print("Incorrect password - try again")
    
    print(password)