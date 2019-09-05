

#!/usr/bin/python

seq = ('name','age','gender')
dict1 = dict.fromkeys(seq)
print("New dictionary :", str(dict1))  # here comma seperator
print("")

'''dict1['name'] = "Guido"
print(dict1)
print("")
print(seq)
'''
dict2 = dict.fromkeys(seq)
print ("Another dictionary : %s" %  str(dict2)) # here % separator  

