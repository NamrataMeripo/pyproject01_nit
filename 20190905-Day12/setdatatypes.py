

"""
Data Structures: Sets
A set is an unordered collection without duplicates.
When printed, iterated upon, or converted into a sequence,
its elements will appear in an arbitrary, implementation-dependent order.
"""
'''
set()
print(set()) # Empty set

# unordered collection
sdlc = "agile"
print(set(sdlc))

# no dupliates
sdlc1 = "agile agile"
print(set(sdlc1))


# set tuple
tupleset = ("agile",'aws','gcp')
print(" Tuple set called :", set(tupleset))
print("")
# set tuple duplicates
tupledupe = ("agile",'aws','gcp',"agile",'aws','gcp',"Agile",'aws','Gcp')
print(" Tuple set called :", set(tupledupe))

# LIST 
languages = ["java",".net","python","python","java"]
print(set(languages),len(languages),id(languages),type(languages))
print("")
#no key duplicates
vendorinfo ={"vendor -1":"aws","vendor -1":"gcp","vendor -3": "cloud" }
print(set(vendorinfo),id(vendorinfo),type(vendorinfo),len(vendorinfo))


abc = set(languages)
print(abc,type(abc),id(abc),len(abc))
print("")
'''
vendorinfo ={"vendor -1":"aws","vendor -1":"gcp","vendor -3": "cloud" }
storevalue= set(vendorinfo)
print(storevalue,len(storevalue),id(storevalue),type(storevalue))
print("")
print(vendorinfo.keys())
print("")
print(vendorinfo.fromkeys(storevalue))













