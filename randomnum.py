#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right
import random
guessed_num=int(input("Guess a number:"))
random_num=random.randrange(1,10)
print("random number:",random_num)
if guessed_num not in range(1,10):
    print("Enter a number between 1 and 9 including both")
elif guessed_num < random_num:
    print("guessed low")
elif guessed_num > random_num:
    print("guessed high")
elif guessed_num == random_num:
    print("guessed right")    
