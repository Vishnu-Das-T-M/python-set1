#Take the following lists
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_list=[]
a1=list(set(a))
b1=list(set(b))  
for x in a1:
    if x in b1:
        new_list.append(x)
print(new_list)        