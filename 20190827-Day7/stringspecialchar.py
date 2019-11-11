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


# strings
# +
# *
# []
# [:]
# [::]
# raw string r or R
# %
# .format ()

'''
# +
bankname = "BOA  "
bankaddress = "SandySprings"
print(bankname +bankaddress)
print(bankname,bankaddress)

# *
statename = "GA "
print(statename * 3)

'''
# [] - Slicing
countryname = "UnitedStatesofAmerica "
#print(countryname [4])
#print("")
print(countryname [3::2])


# Remainders
print("Firstname: %s Middlename: %s Lastname: %s" %("Namrata","M","Meripo"))
Firstname,Lastname,Middlename,DOB = "Namrata","Meripo","M",3030
print("Firstname: %s Lastname: %s Middlename %s DOB: %d" %(Firstname,Lastname,Middlename,DOB))

# .format
print("Firstname {} Middlename {} Lastname {}" .format(Firstname,Middlename,Lastname))
print(f"Firstname {Firstname} Lastname {Lastname}")


