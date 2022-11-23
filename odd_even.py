#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Number=int(input("Enter a number:"))
if (Number % 2)==0:
    print("The number,",Number,"is an even number")
else:
    print("The number",Number,"is an odd number")    