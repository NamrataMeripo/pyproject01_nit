# Loops
'''
# while user input

sum = 0
i = 1

n = int(input("Enter the number :: "))
while i <= n:
    sum = sum + 1
    print(sum)
    i = i +1
'''
'''
# While password and If - elif

password = ""

while password != "RedHat":
    print(str(input("Enter the password :: ")))
    if password == "RedHat" :
        print("Correct password : RedHat")
    elif password == "Admin@123" :
        print("Old Password - Please enter the new password")
    elif password == "RedHat@123" :
        print("This is your recently changed password")
    else :
        print ("Incorrect Password : Try again : ")
        print(password)
    '''

'''
# while if else
invalid = True

while invalid :
    number = int(input("Enter the numbers between 10 to 20 :"))
    if number > 0 and number <=10 :
        print("Take right direction ")
    else :
        invalid = False
        print("False = Take left direction")
    
print("{}".format(number))
'''
'''
# while Else

counter = 0
while counter < 3 :
    print("value ")
    counter+=1
else :
    print("empty")
    '''

# For loop

'''
for val in 'hyderabad':
    if val == "r":
        break
    print(val)

print("The End!")

for bankname in 'Atlanta' :
    if bankname == 'n':
        continue
    print(bankname)

print("The End")
'''
# while break
vowels = "AEIOUaeiou"

invalid = True
while invalid :
    v = input("enter the vowel : ")
    if v in vowels :
        break
    else:
        continue

print( " Thank you")
