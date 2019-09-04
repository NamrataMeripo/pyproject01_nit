
#!/usr/bin/python

tuple1,tuple2 = ("Van","Guido","Rossum"),(1,4,6)
print(tuple1,tuple2)

print("Min value of tuple1 :", min(tuple1))
print("Max value of Tuple2 : ", max(tuple2))
print("")

# Convert list to tuple
list1 = ["Guido","Van","Rossum",1,3,5]
converttuple = tuple(list1)
print("")
print("Convert to tuple :", converttuple,len(converttuple),type(converttuple),id(converttuple))
print("")

# Convert tuple to list
atuple1 = ("India","America","Canada",1,3,5,6)
convertlist = list(atuple1)
print("Convert to list:", convertlist,len(convertlist),type(convertlist),id(convertlist))

