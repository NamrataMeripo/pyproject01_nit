
listofcloud = ("GCP","AWS","CLOUD",1,'$')
print(listofcloud,id(listofcloud),type(listofcloud),len(listofcloud))

  
'''
A tuple is an immutable sequence of values of any type.
Tuple elements are indexed by sequential integers, starting with zero.
Tuples are constructed by the comma operator,
with or without enclosing parentheses.
An empty tuple must have the enclosing parentheses.
A single item tuple must have a trailing comma.
'''

# Empyt Tuple Variable 
list_of_cloud_vendors = (1,2,3,4,'A','z','%')
list_of_cloud_vendors = 1,2,3,4,'A','z','%'
list_of_cloud_vendors = ()
list_of_cloud_vendors = 1,

print(list_of_cloud_vendors,type(list_of_cloud_vendors),id(list_of_cloud_vendors),len(list_of_cloud_vendors))
print(tuple(enumerate(list_of_cloud_vendors)))
