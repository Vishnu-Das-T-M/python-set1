#Ask the user for a string and print out whether this string is a palindrome or not
string=str(input("Enter a string:"))
def ispalindrome(string):
    return string==string[::-1]
result=ispalindrome(string)
if result:
    print("The string",string,"is palindrome")
else:
    print("The string",string,"is not palindrome")    