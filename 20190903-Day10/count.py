

countnames = ["Guido","van","VAN","Python","vAN"] 
countnumbers = [64,2,53,64,64,48]
#print(list(enumerate(countnames)))
#print(list(enumerate(countnumbers)))
print(countnames.count("van".upper()))
print(countnames.count("van".swapcase()))
print(countnames.count("van".lower()))
