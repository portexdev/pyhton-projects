import random
words = ["party","slave","affiliate","python","javascript","laptop","headphone","keyboard","mouse","cash","facualty"]
rand_word = random.choice(words)
print(rand_word)
count = 0
mop=len(rand_word)
po = "you have {} chances to guess the correct word. Goodluck".format(mop)
print(po)
words_list=list(rand_word)
player_guesses=[rand_word[0]]


for char in words_list:
    if char in player_guesses:
        print(char)
    else:
       print("--")


while count <= mop + 1:
    failed = 0
    player_num=str(input("input your guess:"))
    player_guesses.append(player_num)
    prin = "you have {} chances left ".format(count)
    print(prin)
    for char in words_list:
        if char in player_guesses:
            print(char)
        else:
            print("--")
            failed+=1
    if failed == 0:
        print("you win")
        break
    else:
        if count == mop:
            print("you lost")
            break
        else:
            count+=1
       
