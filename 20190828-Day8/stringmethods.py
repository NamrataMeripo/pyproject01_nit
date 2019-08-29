

# Create a variable 

#cloud ="azure gcp azure kubernetes"
#print(cloud,len(cloud),id(cloud))

' capitalize - First letter capital and remaining all lower case'
#print(cloud.capitalize())

'Upper - all letter in upper case'
#print(cloud.upper())

'lower - converts to lower case'
#accountname= "NAMRATA MERIPO"
#print(accountname.lower())


'swap case- upper to lower vice versa'
#languages ="Java .Net Python"
#print(languages.swapcase())

'title - First character uppercase and remaining all lower case'
#print(accountname.title())

' count - search the variable between start number and end number'
#print(len(languages))
#print(languages.count('a'))
#print(languages.count('a',0,15))

' find -  a word --- Index will be captured '
#cloud ="azure gcp aws kubernetes aws gcp aws kubernetes"
#searchword ='aws'
#print(len(cloud))
#print(cloud.find('aws'))
#print(cloud.find('AWS'.swapcase()))


'rfind -  reverse order --- Index will be captured '
#print(cloud.find('aws'))
#print(cloud.rfind('aws'))



# Python code to demonstrate working of  
# find() and rfind() 
linestatement = "phrase is a phrase is a phrase is a phrase"
searchword = "is"
#print(len(linestatement))
  
# using find() to find first occurrence of searchword 
print("The first occurrence of searchword is at : ", end="") 
#print(linestatement.find(searchword))
#print (linestatement.rfind(searchword) ) 

'''
# using rfind() to find last occurrence of searchword 
# returns 21 
print ("The last occurrence of searchword  is at : ", end="") 
print ( linestatement.rfind( searchword, 4) ) 

'Starts with is True or False'
print(linestatement.startswith('is'))

'endswith phrase True or False'
print(linestatement.endswith('phrase'))


'''







