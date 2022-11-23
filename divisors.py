#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
Number=int(input("Enter a number:"))
divisors_list=[]
for i in range(1,Number+1):
    if(Number%i==0):
        divisors_list.append(i)
print(divisors_list)        
