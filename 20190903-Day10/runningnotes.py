'''
# Extend- to extend the varibles
names = ["Guido", "van", "Rossum", 0,1,2]
othernames = ["aaa","bbb","ccc"]
names.append(othernames)
print(names)

names.extend(othernames)
print(names)


# remove with the identification of variables
removenames = ["Guido" , "Van", "Rossum", "Namrata" , 'Riya', 'mmmlll']
print(list(enumerate(removenames)))
removenames.remove("Guido")
print(removenames)

# remove with the identification of index
removenames.pop(4)
print(removenames)
print(list(enumerate(removenames)))


# reverse
onereverse =["Guido",'Van','Rossum','Riya','Namrata']
tworeverse = [2,3,4,5,6,7,8]
onereverse.reverse()
print("After reversing the names are :", onereverse)

# sort
onesortnames = ["Guido",'Van','Rossum','Riya','Namrata']
onesortnames.sort()
print( "After sorting: ",onesortnames)

twosortnames = [1,4,6,8,5,9]
twosortnames.sort()
print(twosortnames)

# Based on ASCII codes
thirdsortnames =["G",'t',"9",'@',"r","L"]
thirdsortnames.sort()
print(thirdsortnames)
'''

# Insert
oneinsert = ['Guido','Van',1,2,"R"]
twoinsert = ["Rossum"]
print(list(enumerate(oneinsert)))


oneinsert.insert(3,"Rossum")



values = [3,2,4,1,"Guido","Ron",10.9]
values.append("Namrata")
print(values)

values.extend ("Van")
print(values)

values.insert(3,"Riya")
print(values)

values.remove(1)
print(values)

values.pop(2)
print(values)

values.reverse ()
print(values)

numbers = [3,2,4,6,7,1,9,3,2,4,2]
numbers.sort()
print(numbers)

print(numbers.count(3))
