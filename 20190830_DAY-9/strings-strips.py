#!/usr/bin/python

"""
1. ljust
2. rjust
3. strip
4. lstrip
5. rstrip
6. index 
7. rindex
8. join
9. replace 
10. center 
"""

account_holder_name = "Guido Van Rossum"

print(account_holder_name,id(account_holder_name),type(account_holder_name),len(account_holder_name))

#print(account_holder_name.ljust(20,'@'))
#print(account_holder_name.rjust(20,'#'))
aValue = "abcdef"

moreValues = """ abc 
def 
ghi
"""
#print(aValue.center(10,'*'))
#print(moreValues.center(40,'$'))

#print(account_holder_name.lstrip('@'))
#print(account_holder_name.rstrip('@'))
#print(account_holder_name.strip('@'))
middle="Van"
#print(account_holder_name.index(middle))   # Left to Right Search
#print(account_holder_name.rindex(middle))  # Right to Left Search
#print(account_holder_name.find(middle))     # Left to Right Search
#print(account_holder_name.rfind(middle))    # Right to Left Search
joiner = '-'
title = "10 20 30 abc"
#print(joiner.join(title))

information = "Python is a Scripting is and Programming is Language"
print(information.replace('is','was',2))



countryname = "@@@@@@@@@@@unitedstatesofamerica@@@@@@@@@@"
print(len(countryname))
print(countryname.strip('@'))
print(countryname.rstrip('@'))
print(countryname.lstrip('@'))

capname = "Lenevo","Acer"
print(capname.index("Acer"))
bridging = "*_*"
print(bridging.join(capname))


txt="banana"
print(txt.center(30))

replacesub = "Python was a name and was a subject and was a language and was easy learning"
print(replacesub.replace('was','is'))
print(replacesub.replace('was','is',3))

x = frozenset({"apple","orange"})
print(x)


