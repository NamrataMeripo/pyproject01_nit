
vowels = "aeiouAEIOU"

while True :
    n = input("Enter the letter:")
    if n not in vowels :
        print("This is not a vowel: Incorrect")
        continue
    else :
        print("This is a vowel")
        break

print("Thank You")

