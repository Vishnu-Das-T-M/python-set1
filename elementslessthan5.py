#write a program that prints out all the elements of the list that are less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list=[]
for num in a:
    if num < 5:
        new_list.append(num)

print(new_list)        
