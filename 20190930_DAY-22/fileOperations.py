import os

print(os.getcwd())

print(os.listdir('/Users/keshavkummari/pyproject01_nit/20190930_DAY-22'))

openAfile = open('aws.txt')
#openAfile = open('aws.txt','rt')
print(openAfile.read())

file = open('aws.txt','w')
file.write("I am a New Text File")
file.close()

aFile = open('aws.txt')
print(aFile.read())
aFile.close()