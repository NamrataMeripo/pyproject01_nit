
# Arithematic
# Comparison
# Assignment
# Logical
# Bitwise
# Membership
# Identity

# Arithematic operators
# + , - , *, /, %, ** ,//
x = 10
y = 20

print("Total :", x+y)
x = 10
y = 20

print("Addition :", x+y)
print("Substraction :", y-x)
print("Mutiplication :", x*y)
print("Division :", y/x)
print("Modulus",x%y)
print("Exponent", x ** y)
print("Floor division :", x // y)
print("") # Comparison
print("Equal to : ", x==y)
print("Greater than :", x>y)
print("Less than : ",x<y)
print("Greater than or equal to :", x >= y)
print("Less than equal to :", x<=y)
print("Not equal to :",x !=y)
print("") # Assignment operators
x = 10
y = 20
z = 0
z = x + y
print("Assignment + : ", z)
z += x
print("Plus equal to : ",z)
z *= x
print("40 * 10: ", z)
z /= x
print("division ",z)
z %= x
print("modulus: ",z)
z **= x
print("Double mutliply :",z)
z //=x
print("double slash :",z)



# Logical operators
# AND , OR , NOT

x = True
y = False

print(x and y)
print(x or y)
print(not y)

# Membership operator
x = " HelloWorld"
print('H' in x)
print('Hello' not in x)

# Identity operator 
x = 4
y = 4

print(id(x),id(y),type(x),type(y))

# Lists
x1 = (1,2,3)
y1 = (1,2,3)
print("Tuple - same ID:",id(x1),id(y1))

a1 = [1,2,3]
b1 = [1,2,3]
print("List - different ID:",id(a1),id(b1))



# Bitwise operator

a = 5
b = 10
print(bin(a))
print(bin(b))
print(bin(a) and bin(b))
print(bin(a) or bin(b))


# shift left
a = 40
b = 20
c = b <<2
print(c)

#shift right
d = b >> 2
print(d)




