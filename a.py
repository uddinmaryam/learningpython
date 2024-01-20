#write a program that takes integer as input and prints whether it is negative or positive or zero
number = int(input("Enter an integer:"))
if (number > 0):
    print("The integer is postive")
elif (number == 0):
    print("The integer  is zero")
else:
    print("The integer is negative")