# checking no. is divisible by 3 or not
no = input("Enter a Decimal Number :")
try :
    num = int(no)
except :
    print("Please enter a valid input")

if num % 3 == 0:
    print("Number  is divisible by 3")
else :
    print("Number is not divisible by 3")
