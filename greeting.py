#Write a program that asks the user to enter their name and their age. 
#Print out a message that greets them and that tells them the year that they will turn 100 years old.
from datetime import date
Name=input("Enter your Name:")
Age=int(input("Enter Your Age:"))
today=date.today()
current_year=today.year
year100=int(current_year)-Age+100
print("you will be 100 years old in the year:",year100)