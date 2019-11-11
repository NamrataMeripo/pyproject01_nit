'''  # Strips
1. ljust
2. rjust
3. strip
4. lstrip
5. rstrip
6. index
7. rindex
8. join
9. replace
10. center
'''

'''
accountholdername = 'GuidoVanRossum'
print(accountholdername, len(accountholdername), id(accountholdername), type(accountholdername))

#ljust
print(accountholdername.ljust(20,'#'))

#rjust
print(accountholdername.rjust(20,'@'))

#strip
stripchar = "####Namrata####@@@@@"
#print(stripchar.strip('@'))

#rstrip
print(stripchar.rstrip('@'))

#lstrip
print(stripchar.lstrip('#'))


#index
stripchar = "####Namrata Namrata Namrata ####@@@@@"
middle='Nam'
print(stripchar.find('rat'))
print(stripchar.rfind('rat'))
print(stripchar.index(middle))

#rindex
print(stripchar.rindex(middle))

# Join
joiner = '-'
title = '10 20 30 40 50'
print(joiner.join(title))


# replace
information = 'python is a script and is a language and is the best automation tool'
print(information.replace('is','was'))
print(information.replace('is','was',2))

'''

#center
avalue ="abcdefgijklm"
morevalues= """ abc \
def \
ghi \
""" 
print(avalue.center(40,'*'))
print(morevalues.center(60,'$'))













