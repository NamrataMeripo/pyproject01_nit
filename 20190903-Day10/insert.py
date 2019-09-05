#!/usr/bin/python

# Example 1
aCoolList = ["superman", "spiderman", 1947,1987,"Spiderman"]
oneMoreList = [22, 34, 56,34, 34, 78, 98]
print(list(enumerate(aCoolList)))

# inserting values
aCoolList.insert(0, "street750")
print(list(enumerate(aCoolList)))

# Example 2
insertnames = ["Guido","Van","Rossum","Python"] 
insertnumbers = [41,2,53,25,64,48]
print(list(enumerate(insertnames)))
insertnames.insert(1,"Intro")
print(list(enumerate(insertnames)))