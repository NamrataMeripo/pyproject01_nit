
import os 

'''
aFile = open("aws.txt")
print(aFile.readline())
print(aFile.read())
aFile.close()
'''

'''
try:
    aFile = open("a.txt")
    print(aFile.readline())
    print(aFile.read())
except:
    print("File Does not exists")
finally:    
    aFile.close()
'''

with open('aws.txt') as afile:
    print(afile.tell())
    print(afile.readline())
    print(afile.seek(0))
    print(afile.tell())
    print(afile.read())
    print(afile.tell())