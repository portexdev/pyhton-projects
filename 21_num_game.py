import random
import time
import os


# INTRODUCTION
print("welcome to the 21 number game!! \nits a pleasure to have you with us")
print("you will get to choose a number until 21, but only in range in mutiple of 4s.\nany the player who get the chance to call 21 lose the game\n")
#GAME-MODE
player_opp=input("Do you wish to play with computer or another player?Type C to play computer and P to play a friend:")

#list of guesses by the players
played_number=[0]
#Play again or Exit the game
def again():
    res = input("Do you want to play again? YES or NO:")
    if res == "YES":
        print("Rebooting game servers.....")
        time.sleep(1)
        pass
    else:
        exit()
#computer-algorithm
def comp_alg():
    if sum(played_number[:4]) < 9:
        comp_rand= random.randrange(played_number[-1] + 1,played_number[-1] + 4)
        return comp_rand  
    elif sum(played_number[:4]) >= 9:
        last_num = played_number[-1]
        match last_num:
            case 5:
                comp_rand = 8
                return comp_rand
            case 6:
                comp_rand = 10
                return comp_rand
            case 7:
                comp_rand = 9
                return comp_rand
            case 8:
                comp_rand = 10
                return comp_rand
            case 9:
                comp_rand = 12
                return comp_rand
            case 9:
                comp_rand = 11
                return comp_rand
            case 10:
                comp_rand = 12
                return comp_rand
            case 11:
                comp_rand = 12
                return comp_rand
            case 12:
                comp_rand = 15
                return comp_rand
            case 13:
                comp_rand = 15
                return comp_rand
            case 14:
                comp_rand = 15
                return comp_rand
            case 14:
                comp_rand = 15
                return comp_rand
            case 15:
                comp_rand = 16
                return comp_rand
            case 16:
                comp_rand = 20
                return comp_rand
            case 17:
                comp_rand = 20
                return comp_rand
            case 18:
                comp_rand = 20
                return comp_rand
            case 19:
                comp_rand = 20
                return comp_rand
            case 20:
                comp_rand = 20
                return comp_rand
    else:
        comp_rand= random.randrange(played_number[-1] + 1,played_number[-1] + 4)
        return comp_rand                

#computer player
def computer_card(last_played):
    
    if len(last_played) == 0:
        print("---generating response from computer-----")
        time.sleep(2)
        print("--- response generated-----")
        comp_card =random.randrange(1,4)
        last_played.append(comp_card)
        print("order of inputs after after computer's turn is:")
        print(last_played)
    else:
        print("---generating response from computer-----")
        time.sleep(2)
        print("--- response generated-----")
        comp_card =comp_alg()
        last_played.append(comp_card)
        print("order of inputs after after computer's turn is:")
        print(last_played)

    return last_played
#user-player1
def player_card(last):
    player_number = input("its player1 turn input your number:")
    if len(player_number)==0:
       print("your input is empty!!! you lost your turn")
    elif player_number.isdigit() != True:
        print("your number is not a digit!!!  you lost your turn")
        exit()
    elif int(player_number) <= int(last[-1]) or int(player_number) > int(last[-1]) + 4 :
        print("you are exceeding bounds!!!! try again")
        player_card(last)
        pass
    else:
        last.append(int(player_number))
        print("order of inputs after after player1 played is:")
        print(last)
    return last
#user player2
def player_card2(last):
    player_number = input("its player2 turn input your number:")
    if len(player_number)==0:
       print("your input is empty!!! you lost your turn")
    elif player_number.isdigit() != True:
        print("your number is not a digit!!!  you lost your turn")
    elif int(player_number) <= int(last[-1]) or int(player_number) > int(last[-1]) + 4 :
        print("you are exceeding bounds!!!! try again")
        player_card2(last)
        pass
    else:
        last.append(int(player_number))
        print("order of inputs after player2 played is:")
        print(last)
    return last


# running Game
if player_opp == "C" or player_opp == "c":
    #decides who goes first between Player & computer
    first_try=input("Do you wish to go first? Type in YES / NO:") 
    #response outcome
    if first_try == "NO":
        # control variable
        count=0
        # while game is on
        while count < 21:
            computer_card(played_number)
            count=played_number[-1]
            if count >= 20 :
                print("you lost")
                again()
            else:
                player_card(played_number)
                count=played_number[-1]
                if count >= 20 :
                    print("you win")
                    again()
    else:
         count=0
         while count < 21:
            player_card(played_number)
            count=played_number[-1]
            if count > 21 :
                print("you lost")
                again()
            else:
                computer_card(played_number)
                count=played_number[-1]
                if count > 21 :
                    print("you win")
                    again()
else:
    #decides who goes first between player and player
    first_try=input("Player1 do you wish to go first? Type in YES / NO:") 
    #response outcome
    if first_try == "NO":
        coun=0
        #while the game is on
        while coun < 21:
            player_card2(played_number)
            coun=played_number[-1]
            if coun >= 20 :
                print("player2 won")
                again()
            else:
                player_card(played_number)
                coun=played_number[-1]
                if coun >= 20 :
                    print("player1 won")
                    again()
    else:
        coun=0
        while coun < 21:
            player_card(played_number)
            coun=played_number[-1]
            if coun >= 20 :
                print("player1 won")
                again()
            else:
                player_card2(played_number)
                coun=played_number[-1]
                if coun >= 20 :
                    print("player2 won")
                    again()

 



