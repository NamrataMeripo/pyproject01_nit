
"""
1. list()

A list is a mutable sequence of values of any type.

A list with zero elements is called an empty list.

List elements are indexed by sequential integers, starting with zero.

Example :

listOfBanks = []
listOfBanks = ['a','A','%',0,9]
"""
# Method : list()
int()
complex()
float()
str()

listOfBanks = ['SBI','HDFC',"AXIS",'''ABN''',"""AMX"""]
print(listOfBanks)

print(list(enumerate(listOfBanks)))

print(type(listOfBanks))

print(id(listOfBanks))

print(len(listOfBanks))

    
list1 = [1, 2, 3,4,1, 4,1,3, 1, 4, 5] # returns the lowest index of the list
print(list1.index(1)) 

print(list1.index(1,3,9)) # Search for 1 number from  3 to 9 index



