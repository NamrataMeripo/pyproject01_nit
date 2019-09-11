# Lists
'''
variables = ['a',0,'%',1,'k']
print(variables)
#enumerate
print(list(enumerate(variables)),len(variables),type(variables),id(variables))
'''

"""
values.append()
values.extend()
values.insert()
values.remove()
values.pop()
values.reverse()
values.sort()
values.count()
values.join()
"""
'''
# append
values = [10,20,30,10]
values.append('Guido Van Rossum')
print(values)

# extend
values.extend('Van')
print(values)

# insert
values.insert(4,'aeiou')
print(values)

#remove
values.remove(20)
values.remove('aeiou')
print(values)

#pop
values.pop(4)
print(values)

#reverse
values.reverse()
print(values)

#sort
numbers = [4,2,6,7,3,22,3,55,7,8]
numbers.sort()
print(numbers)
'''
'''
countnames = ["Guido","van","VAN","VAN","Python","vAN"] 
countnumbers = [64,2,53,64,64,48]
#print(list(enumerate(countnames)))
#print(list(enumerate(countnumbers)))
print(countnames.count("van"))
print(countnames.count("van".upper()))
print(countnames.count("van"))
print(countnumbers.count(64))
'''

#join  -- list will not have joins.. hence invalid
'''accountnames = ['_']
othernames = ['kim','Tim','Bim','Nim']
print(accountnames.join(othernames))

'''
# tuple
tuplevendors = ('a','D,',1,5,'%')
print(tuplevendors,len(tuplevendors),type(tuplevendors),id(tuplevendors))
print(tuple(enumerate(tuplevendors)))

# tuple example
tup1 = ('python', 'linux', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "A", "B", "C", "E",5,"$"
#tup3 = """A""","""B""","""C""","""E"""
tup4 = 'a', 'b', 'c', 'd'
'''
#tup4 = '''a''', '''b''', '''c''', '''d'''  '''
'''
print(tup1,len(tup1),id(tup1),type(tup1))
print(tup2,len(tup2),id(tup2),type(tup2))
print(tup3,len(tup3),id(tup3),type(tup3))
print("tup4 is :",tup4,len(tup4),id(tup4),type(tup4))

print(tup1[2])
print(tup2[3])
print(tup3[4])
print(tup4[2])
'''
'''
# Tuple methods
Tup1, Tup2 = ('Nam',"Man","Sam",1,4) ,(3,5,6,'%','Dam')
Tup3 = Tup1 + Tup2
print(Tup3)
print("")
print(Tup1+Tup2)
print("")
print(Tup1,Tup2)
print("")

# convert Tuple to List
Tuplenames = ('Nam',"Man","Sam",1,43,5,6,'%','Dam')
Listconvert = list(Tuplenames)
print(Listconvert)

# convert List to Tuple
listnames = ['Nam', 'Man', 'Sam', 1, 43, 5, 6, '%', 'Dam']
tuplecovert = tuple(listnames)
print(tuplecovert)

# tuple slices
tup1 = ['python','linux',1998,3000,20]
tup2= (1,2,4,5,3)
print(tuple(enumerate(tup1)))
print(tuple(enumerate(tup2)))
print("tup1 : ", tup1[-3])
print("tup2 :",tup2[-4])


# Empty dictionary
cloudpro = {}
print(cloudpro,len(cloudpro),type(cloudpro),id(cloudpro))

cloudnames = {"cloud1":"aws", "cloud2":"gcp","cloud3":"python"}
print(cloudnames)

# updating the dict names
cloudnames['cloud2'] = 'Kubernetes'
print(cloudnames)
cloudnames['cloud 3']  = 'cloud 9'
print(cloudnames)

# adding new dictionary names
cloudnames['cloud4'] = "PCF"
print(cloudnames)


# deleting the dictionary
cloudnames = {"cloud1":"aws", "cloud2":"gcp","cloud3":"python"}
del cloudnames['cloud3'] 
print(cloudnames)

cloudnamesdel = {"cloud1":"aws", "cloud2":"gcp","cloud3":"python"}
print(cloudnamesdel)

cloudnamesdel.clear ()
print(cloudnamesdel)


# Get 
cloudnames = {"cloud1":"aws", "cloud2":"gcp","cloud3":"python"}
print(cloudnames.get('cloud2'))
print(cloudnames.get('cloud3'))
print("")
print(cloudnames.keys())
print("")
# copy to other variable
copycloud = cloudnames.copy()
print(copycloud)
'''

'''
# from keys
dictnames = {"Sun","Mon","Tues","Wed"}
keynames = dict.fromkeys(dictnames)
print(keynames)

keynames["Sun"] = "Sunday"
keynames["Mon"] = "Monday"
keynames["Tues"] = "Tuesday"
keynames["Wed"] = "Wednesday"
print(keynames) 
'''
keyscreation = {"Jan","Feb","Mar"}
createkeys = dict.fromkeys(keyscreation)
print(createkeys)
print("")
print(dict(enumerate(createkeys)))
print("")


createkeys["Jan"] = "January"
createkeys["Feb"] = "February"
createkeys["Mar"] = "March"
print(createkeys)


keysnames = {"Jan","Feb","Mar"}
copynames = keysnames.copy ()
print(copynames)
print(createkeys.keys ())

