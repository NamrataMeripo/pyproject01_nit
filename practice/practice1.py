''''# int
# float
# complex

intaccountname = 2600
print(intaccountname,type(intaccountname))

floataccoutname = 2600.5
print(floataccoutname,type(floataccoutname))

complexaccoutname = 5+6j
print(complexaccoutname,type(complexaccoutname))
'''
'''
# String special characters
# + addition
bankdetails ="BOA"
branch = "US"
print(bankdetails + "" + branch)
print(bankdetails,branch)
print(bankdetails , "localbranch")
'''
'''
# * 
bankdetails ="BOA  "
print(bankdetails *10)
'''
'''
# slice []
accountname = "python and python"
print(accountname[12])
'''
'''
# Zero based indexing [::]
accountname = "python and python"
print(accountname[0::12])
'''

# Remainders
'''Bankname,Branch,State,Zipcode = "BOA","Dunwoody","GA",30338
print("Bankname %s Branch %s State %s Zipcode %d",(Bankname,Branch,State,Zipcode))
print("Bankname %s Branch %s State %s Zipcode %d" %(Bankname,Branch,State,Zipcode))
print("Bankname %s Branch %s State %s Zipcode %d" %('BOA',"Dunwoody",'GA',30338))
'''
'''
# .format
Bankname,Branch,State,Zipcode = "BOA","Dunwoody","GA",30338
print("Bankname {} Branch {} State {} Zipcode {}" .format(Bankname,Branch,State,Zipcode))
print(f"Bankname {Bankname} Branch {Branch} State {State} Zipcode {Zipcode}")
'''

# Methods
'''
captalize
upper
swapcase
lower
title
count
find
rfind
startswith
endswith
'''
'''
# captalize
bankname = "boa"
print(bankname.capitalize())
print("")

#Upper
print(bankname.upper())
print("")

# swapcase
branch= "dunwoody"
print(branch.swapcase())

#title
branch ="dunwoody"
print(branch.title())

# count
phrase = "this is python this is python this is python this is python"
print(phrase.count ('python'))

# find
phrase = "this is python this is python this is python this is python"
print(phrase.find('python'))
# rfind
print(phrase.rfind('python'))
print(phrase.rfind('PYTHON'.swapcase()))

#starts with
phrase = "this is python"
print(phrase.startswith("this"))
print("")
print(phrase.startswith('python'))

#endswith
phrase = "this is python"
print(phrase.endswith("python"))
print("")
print(phrase.endswith("PYTHON"))
'''

#Strips
'''
ljust
rjust
strip
lstrip
rstrip
index
join
replace
center
'''
'''
#ljust
accountname= "Guido Van Rossum"
print(len(accountname))
print(accountname.ljust(40,'@'))

#rjust
print(accountname.rjust(30,'#'))

#strip
coursename="######python@@@@@@"
print(coursename.strip('@'))

#rstrip
coursename = "@@@@@@python@@@@@@"
print(coursename.rstrip("@"))

#lstrip
print(coursename.lstrip('@'))
print("")

#index
coursename = "@@@@@@python@@@@@@"
print(coursename.index('python'))
print(coursename.rindex('python'))

#joins
connect ='_'
branch = "springs","sandy","Roswell"
print(connect.join(branch))

username = " Guido name is Guido and is Van and is Rossum and"
print(username.replace('and',';'))
print(username.replace('is','was',2))

#center
username = " Guido "
print(username.center(30,'*'))
'''
