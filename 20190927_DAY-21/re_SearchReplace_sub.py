import re

contact_number = "9900-888-666 # This is Guido Van Rossum Contact Number"

print(contact_number)

num = re.sub(r'#.*$', "",contact_number)

print(num)

num1 = re.sub(r'\D',"",contact_number)

print(num1)
