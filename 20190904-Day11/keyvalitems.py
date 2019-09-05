

#!/usr/bin/python

filename = {'Course' : 'Python' ,'type' :' video' , 'boolean': 1}
sample = {1 :"one" , 2 : "two"}
print(filename.get('type'))
print("")
print(filename.get('Course'))
print("")
print(filename.get('boolean'))
print ("")

print(filename.keys())
print("")

# copy the data to other variable
raw_data = filename.copy()
print(raw_data)
print("")

copydata = filename.copy()
print("Data copied from filename : ", copydata)
print("")



