'''String Special Operators 
# +
# *
# []
# [ : ]
# [ : : ]
# raw string r or R 
# % 
# .format()
'''

# Indexing
''' Lefttoright = 012345678101112131415 ......
    righttoleft = .........-15-14-13-12-11-10-9-8-7-6-5-4-3-2-1 '''
'''
# + - Cancatenation
firstname = 'Namrata'
lastname = 'Meripo'
print(firstname + lastname)
print(firstname,lastname)
print(firstname,"Meripo")

# * - Repeatetion
coursedetails = 'python'
print(coursedetails * 6)

# [] - Slicing
firstname = 'Namrata'
lastname = 'Meripo'
print(firstname[5])
print(lastname[0])

# [0::3] - zero based indexing - starting with character and Every 3rd index
accountstatement ='WelcometoBankofAmerica'
accountspace="Welcome to Bank of America"
print(accountstatement[0::3])
print(accountspace[3::2])
'''

# Remainders
firstname,middlename,lastname,dob = 'Namrata',"Grace","Meripo",3006
print("Firstname %s Middlename %s Lastname %s DOB %d" %(firstname,middlename,lastname,dob))
print("Firstname %s Middlename %s Lastname %s DOB %d" %("Namrata",'Nobody',"Meripo",1212))
print("Firstname {} Middlename {} Lastname {} DOB {}" .format(firstname,middlename,lastname,dob))
print("Firstname {} Middlename {} Lastname {} DOB {}" .format("Namrata",'Nobody',"Meripo",1212))
print(f"Firstname {firstname}, Lastname {lastname}, Middlename {middlename}, DOB{dob}")
print(len(firstname),len(lastname),id(dob),id(firstname),id(lastname))

#,len(lastname),len(middlename),len(dob),id(firstname),id(lastname),id(middlename),id(dob))













