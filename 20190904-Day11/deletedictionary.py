
#!/bin/usr/python
# Create a dictionary
deldict1 = {"Name":'Guido',"Class":" Middle","School":"Apostles"}
print("print values :",deldict1)
print("")
print("Name ...... :",deldict1['Name'])
print("")

print("class ... :", deldict1['Class'])
print("")
print("School  :-) :", deldict1['School'])


# Delete the entry
del deldict1['Name'];
print(deldict1)

# clear the entries in deldict
deldict1.clear ()
print("")
print(deldict1)

'''
# Delete entire directory
del.deldict
'''

deldict1['Name'] = "Guido"
deldict1['School'] = "Middle"
deldict1 ['Age'] = 5
print(deldict1)
print("")