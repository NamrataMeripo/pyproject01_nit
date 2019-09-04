

#!/usr/bin/python

# create a dictionary
dic1 ={"Name":"Dory","Age":3,"Home":"Aquarium"}
print("The values of dic1 are : ", dic1, len(dic1),id(dic1),type(dic1),dict(enumerate(dic1)))
print("")
# update the dictionary
dic1['Name'] = "Nory"
print(dic1)
dic1["Home"] = "Sea World"
print("")
dic1['Age'] = 6
# Add new entry
dic1['School'] = "Apostles"
print(dic1)
print("Age :",dic1["Age"])
print(dic1)





