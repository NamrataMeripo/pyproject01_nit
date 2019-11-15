
'''
try:
    <body>
except <ExceptionType1>:
    <handler1>
except <ExceptionTypeN>:
    <handlerN>
except:
    <handlerExcept>
else:
    <process_else>
finally:
    <process_finally>

'''

try:
    #num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1 / num2
    print("Result is", result)
 
except ZeroDivisionError:
    print("Division by zero is error !!")
 
except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like this 1, 2")
 
except:
    print("Wrong input")
 
else:
    print("No exceptions")
 
finally:
    print("This will execute no matter what")