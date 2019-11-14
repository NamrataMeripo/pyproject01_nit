
while True:
    try:
        x = int(input('Enter a Number : '))
        break
    except ValueError:
        print('This is not a Valid Number')
