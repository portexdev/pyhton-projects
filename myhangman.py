import random
#introduction
print("This is a simple hangman game, you have just 6 chances to guess the correct name of a random fruit")


words="apple banana mango peaches pineapple tangerine pawpaw orange pear carrot lemon cherry coconut strawberry"
words =words.split(" ")
rand_fruit= random.choice(words)
wrong = 0

guessed_letters= []
count = 0
correct_letters=[]

print("guess the word!!!!!!!! \n HINT:the word is a name of fruit")
print("---------------------------------------------------------------")



def Print_hangman(wrong):
    if wrong == 0:
        print("\n+----+")
        print("    ||")
        print("    ||")
        print("    ||")
        print("  ======")
    elif wrong == 1:
        print("\n+----+")
        print(" O  ||")
        print("    ||")
        print("    ||")
        print("  ======")
    elif wrong == 2:
        print("\n +----+")
        print(" O   ||")
        print("/    ||")
        print("     ||")
        print("  ======")
    elif wrong == 3:
        print("\n +----+")
        print(" O   ||")
        print("/|   ||")
        print("     ||")
        print("  ======")
    elif wrong == 4:
        print("\n +----+")
        print(" O   ||")
        print("/|\  ||")
        print("     ||")
        print("  ======")
    elif wrong == 5:
        print("\n +----+")
        print(" O   ||")
        print("/|\  ||")
        print("/    ||")
        print("  ======")
    elif wrong==6:
        print("\n +----+")
        print(" O   ||")
        print("/|\  ||")
        print("/ \  ||")
        print("  ======")

# This first piece of code prints the game start-up    
if count == 0:
    print(rand_fruit)
    Print_hangman(0)
    print("this is a " + str(len(rand_fruit)) + " letter word")
    for char in rand_fruit:
        print("_", end=" ")

#this while loop deals with the functionality of the entire game
while count <=  6 :
    # gets the player guess
    player_guess= input("\ninput your guess here:")
    # this varible helps to verify if the game is won
    won_counter=0
    #adding player_guess to a list
    guessed_letters.append(player_guess)
    print("\rguessed letters:")

    # printing the guessed letters
    for x in guessed_letters:
        print(x,end=" ")
    
    #printing the hangman diagram
    if player_guess not in rand_fruit:
        wrong+=1
        Print_hangman(wrong)
    else:
        Print_hangman(wrong)
    #printing out the correct guessed letters
    for char in rand_fruit:
        if char in guessed_letters:
            print(char, end="")
        else:
            print("_", end=" ")
    #validating if player guessed letter is same as the fruit
    for char in rand_fruit:
        if char in guessed_letters:
            # it took me some time to come about this solution
            got = 3+3
        elif char not in guessed_letters:
            won_counter+=1
    #breaks th while loop if winner emerges
    if won_counter == 0:
        print("\n you have won")
        break
    #incrementing number of time a player have guessed
    count+=1
    # validating loss
    if count >6:
        print("you lost")
        break
       
       
