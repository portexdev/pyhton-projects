import  random
import math
lower_bounds= int(input("input lower-bound:"))
upper_bounds = int(input("input upper-bound:"))
random_num= random.randint(lower_bounds,upper_bounds)
chances = round(math.log(upper_bounds-lower_bounds + 1,2))
count = 0

print("    you have only " + str(chances) + " left to guess the right number")


while count <= chances:
    player_num = int(input("input your number : "))
    count+=1
    if player_num == random_num:
        print("congratulations you have won \n you'v guessed the correct number ")
        break
    elif player_num < random_num:
        print("you have guesssed too low")
    else:
        print("you have guesssed too high")

if count > chances:
    print("the number is " + str(random_num) )
    print("better luck next time")