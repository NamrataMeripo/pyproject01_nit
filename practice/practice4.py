
'''
def rawdata(a,b):
    print("value of a is :", a)
    print("value of b is :", b)
    return
# create a variable
information = "Welcome to Python world"
rawdata(information,'aws')
'''
'''
info = "Welcome to the bigdata"
def bigdata () :
    global info
    print(info)
    info = "This is python"
    print(info)
    print("")
    return

bigdata ()
print(info)
'''
'''
def text(arg1,*argue) :
    print(arg1)
    print(*argue)
    return
    
text ('aws','gcp','abc','ced')
'''
'''
# for loops
cloudvendors = "Aws","GCP","Python"
for i in cloudvendors :
    print(i)
'''
'''
# printing in sequence
def abc ():
    banknames = "BOA","CHASE","PHASE"
    for i in banknames:
        print(i)
    return

abc ()
'''
'''
balance = 10

def nameofbank (): 
    bankname = "Bankofamerica"
    print("bankname")
    print("I am on practice4.py ")
    return

if __name__ == "__main__" :
    print(__name__)
nameofbank ()
'''
'''
def listofbank () :
    print("International banks")
    print("National banks")
    print("I am on practice4.py")
    return listofbank

listofbank ()
'''
'''import practice4
print(practice4.balance)

practice4.nameofbank ()
'''
'''
import practice4

def internationalbank () :
    print("Chase Bank")
    return internationalbank 
def nationalbank () :
    print("HDFC Bank")
    return nationalbank

internationalbank ()
nationalbank ()


def allbanks () :
    internationalbank ()
    nationalbank ()
    practice4.listofbank
    return allbanks

allbanks ()

'''

