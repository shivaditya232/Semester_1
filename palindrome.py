number=int(input("enter a number"))
string=str(number)
if string[::-1]==string:
    print("number is a palindrome")
else:
    print("number is not a palindrome")
