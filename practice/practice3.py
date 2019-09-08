 # set

'''
#no duplicates - only keys will be displayed
cloudnames = {"aws":"cloud1","aws":"cloud1","Aws":"cloud1","Aws":"cloud1","bws":"Cloud1"}
print(set(cloudnames))

# list 
languages = ["java","net","net","python","Ruby","Ruby",1,4]
print(set(languages),len(languages),id(languages),type(languages))

# dictionaries
cloudnames = {"aws":"cloud1","aws":"cloud1","Aws":"cloud1","Aws":"cloud1","bws":"Cloud1"}
print(set(cloudnames),len(cloudnames),type(cloudnames),id(cloudnames))


# assigning to other variable
cloudnames = {"aws":"cloud1","aws":"cloud1","Aws":"cloud1","Aws":"cloud1","bws":"Cloud1"}
abc = set(cloudnames)
print(cloudnames.keys())
print("")
print(cloudnames.fromkeys(abc))

'''

# set methods 

'''
1. union
2. intersection
3. difference
4. update
5. add
6.remove
7.discard
'''

# union
a = [1,2,3,4,5,6,7,2,3,4,5,6,7,8]
b = ["a","b","c","d","a","b",1,2]

'''print(set(a).union(set(b)))
print("")
# intersection
print(set(a).intersection(set(b)))
print("")
# difference
print(set(a).difference(set(b)))
print("")
print(set(b).difference(set(a)))
print("")


# udpate
c = set(a)
c.update("a","b","c")
print(c)

# add - takes only one argument
c.add("s")
print(c)

# remove - takes only one argument
c.remove(5)
print(c)

# discard - will not give any exceptions
c.discard (10)
print(c)
print("")

# if conditon

if 2 == 2 :
    print(" The value is true")

if 2 != 4 :
    print(" The value is not true")
    print("")

# elif

if a == a:
        print("The value is true")
elif a == b:
    print("The value is false")

# elif

fee = 10
if fee == 4 :
    print("The fee is 4")
    print(fee)

elif fee == 8 :
        print("The fee is 10")
        print(fee)
else :
    print("Good Bye")


'''

# operators 
'''
1. Arithematic operators
2. comparision operators (Relational)
3. Assignment operators
4. Logical operators
5. Bitwise operators
6. Membership operators
7. Indentity operators
'''

# Arithematic operators
''' 
1. + (addition)
2. - (substraction)
3. * (multiplication)
4. / (divisio)
5. % (modulus)
6. ** (exponent)
7. // (floor division)
'''

'''
x = 150
y = 10
z = x + y
print("addition : ",z)
print("")
z = x - y
print("substraction :",z)
print("")
z = x * y
print("mutiplication : ",z)
print("")
z = x/y
print("division :",z)
print("")
z = x % y
print("modulus :",z)
print("")
z = x // y
print("floor division :", z)
print("")
z= x ** y
print("exponent : ", z)
print("")
'''

# Comparision
'''
1. ==
2. >
3. <
4. >=
5. <=
6. !
'''


'''
1. ==
2. >
3. <
4. >=
5. <=
6. !=


# Comparison operators in Python
# Example: 
x = 10
y = 12

print(id(x),type(x))

print(id(y),type(y))

# Output: x > y is False
print('x > y  is',x>y)

# Output: x < y is True
print('x < y  is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)
'''
'''
# Assignment operators
a= 20
b = 30
c = 0
c = a + b
print("value of c :",c)
print("")
c += a 
print("value of c :",c)
print("")
c*= a
print("value of c :",c)
print("") 

c /= a
print("value of c :",c)
print("")

c %= 1
print("value of c :",c)
print("")

c**= a
print("value of c :",c)
print("")

c //= a
print("value of c :",c)
print("")
'''

# Logical operator
'''
1) and logical AND
2) or logical OR
3) not logical NOT

Keywords - True
Keywords - False
'''
'''
x = True
y = False

print('x and y ', id(x),id(y),type(x),id(y),x and y)
print("")
print('x or y ', id(x),id(y),type(x),id(y),x or y)
print("")
print('x not y ', id(x),id(y),type(x),id(y),not x)

# Membership operators
x = "Hello World"
y = {1:'a',2:'b'}
# Output: True
print('H' in x)
# Output: True
print('hello' not in x)
# Output: True
print(1 in y)
# Output: False
print('a' in y)
'''

# identity operators
'''
1. is
2. is not

x = 20
y = 20
print(x is y)
print(x is not y)
print(x,y , id(x),id(y),type(x),type(y))

# Strings
x2 = 'Hello'
y2 = 'Hello'
print(x2,id(x2),type(x2))
print(y2,id(y2),type(y2))   
print(x2 is y2)
print(x2 is not y2)

x3 = (1,2,3)
y3 = (1,2,3)
print(x3,id(x3),type(x3))
print(y3,id(y3),type(y3))

print(x3 is not y3)
'''

# Bitwise operators - works on bit performing bit by bit

a = 192
b = 168 
c = 0
d = 3 
print(bin(a))
print(bin(b))
print("results " , bin(a) , " AND" , bin(b), "AND", bin(a&b))






