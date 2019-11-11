#cloud ="azure gcp azure kubernetes"
#print(cloud,len(cloud),id(cloud))

' capitalize - First letter capital and remaining all lower case'
accountname = "namratameripo"
print(accountname.capitalize())

'Upper - all letter in upper case'
print(accountname.upper())


'lower - converts to lower case'
locationname = "ATLANTA"
print(locationname.lower())

'swap case- upper to lower vice versa'
print(locationname.swapcase())


'title - First character uppercase and remaining all lower case'
print(locationname.title())





' count - search the variable between start number and end number'
launguages = "java,python,angular"
print(len(launguages))
#print(launguages.count('a'))
#print(launguages.count('n',0,20))
#print(launguages.startswith('a',20))
#print(launguages.endswith('r',19))
print(launguages.find('angular'))
print(launguages.rfind('angular'))




' find -  a word --- Index will be captured '
#cloud ="azure gcp aws kubernetes aws gcp aws kubernetes"
#searchword ='aws'
#print(len(cloud))
#print(cloud.find('aws'))
#print(cloud.find('AWS'.swapcase()))


cloud = "azure gcp aws kubernetes aws gcp aws kubernetes"
print(cloud.find('aws'))
print(cloud.rfind('aws'))

'rfind -  reverse order --- Index will be captured '




# Python code to demonstrate working of  
# find() and rfind() 



'Starts with is True or False'




States = "Georgia","Texas","Ohio","Washington"
print(States, type(States),id(States),len(States))


# capitalize
# upper
# lower
# title 
# swapcase

myname= "namratameRipo"
print(myname.capitalize())
print(myname.upper())
print(myname.lower())
print(myname.title())
print(myname.swapcase())
print(myname.count('a',1,13))
print(myname.find('rat',2,13))
print(myname.rfind('po',1,13))
print(myname.startswith("namr"))
print(myname.endswith("ta"))


