import random
import time
board_items = [" "," "," "," "," "," "," "," "," "]
winner = False
Player_Names=[]

def intro():
    print("Welcome to Tic Tac Toe!")
    print("\n")
    print("The game is played on a grid that's 3 squares by 3 squares.")
    print("Rules: Player 1 and player 2, represented by X and O, take turns "
          "marking the spaces in a 3*3 grid. The player who succeeds in placing "
          "three of their marks in a horizontal, vertical, or diagonal row wins.")
    print("\n")
    input("Press enter to continue...")
    print("\n")



def game_mode():
    response=input("Player1 Please select '1' for Player vs. Player or '2' for Player vs. CPU: ")
    if response == "1":
        print("Player1 will be using X and Player2 wil be using O")
        player1_name=input("player1 input your name: ").upper()
        Player_Names.append(player1_name)

        player2_name=input("player2 input your name: ").upper()
        Player_Names.append(player2_name)
        return "PvP"
    elif response == "2":
        print("Player1 will be using X and COM wil be using O")
        player1_name=input("player1 input your name: ").upper()
        Player_Names.append(player1_name)
        return "PvC"
    else:
        print("this value is not permited")

def winning():
    global winner
    possible_outcomes= [
        # Horizontal
        [board_items[0],board_items[1],board_items[2]],
        [board_items[3],board_items[4],board_items[5]],
        [board_items[6],board_items[7],board_items[8]],
        #Vertical
        [board_items[0],board_items[3],board_items[6]],
        [board_items[1],board_items[4],board_items[7]],
        [board_items[2],board_items[5],board_items[8]],
        #Diagonal
        [board_items[0],board_items[4],board_items[8]],
        [board_items[6],board_items[4],board_items[2]],
    ]
    
    for  x in possible_outcomes:
        if (x[0] != " ") and (x[0] != " ") and (x[0] != " "):
            if ( (x[0] == "X") and (x[1] == "X") and (x[2] == "X") ) or  ( (x[0] == "O") and (x[1] == "O") and (x[2] == "O") ):
                return True

def tie():
    temp= []
    for x in board_items:
        if x == " ":
            temp.append(x)
    if len(temp) == 0:
        return True



def display_board():
    print("  " + str(board_items[0]) + "  |" + "  " + str(board_items[1]) + "  |" + "  " + str(board_items[2]))
    print("------------------")
    print("  " + str(board_items[3]) + "  |" + "  " + str(board_items[4]) + "  |" + "  " + str(board_items[5]))
    print("------------------")
    print("  " + str(board_items[6]) + "  |" + "  " + str(board_items[7]) + "  |" + "  " + str(board_items[8]))

class Player():
    def __init__(self, symbol, array,name) -> None:
        self.symbol= symbol
        self.array = array
        self.name=name
    
    def player_trigger(self):
        player_val = input(str(self.name) + " please input the value position of where you want to play: ")
        if player_val.isdigit() and int(player_val) <= 9:
            if self.array[int(player_val) - 1] == " ":
                self.array[int(player_val) -1] = self.symbol
            else:
                print("that position is already taken my dear")
        else:
            print("invalid input")
            self.player_trigger()

    def get_name(self):
        return self.name
    
    def computer(self):
        temp_list=[]
        for i,x in enumerate(self.array):
            if x == " ":
                temp_list.append(i+1)
        comp_val = int(random.randrange(temp_list[0],temp_list[-1]))
        if self.array[int(comp_val) - 1] == " ":
            self.array[int(comp_val) -1] = "O"

intro()
display_board()
if game_mode() == "PvP":
    Player1 = Player("X",board_items,Player_Names[0])
    Player2 = Player("O",board_items,Player_Names[1])
    while winner == False:
        Player1.player_trigger()
        display_board()
        if tie():
            print("its a tie")
            break
        if winning():
            print(str(Player1.get_name()).upper()+ "has won ")
            break
        Player2.player_trigger()
        display_board()
        if tie():
            print("its a tie")
            break
        if winning():
            print(str(Player2.get_name()).upper()+ "has won ")
            break
else :
    Player1 = Player("X",board_items,Player_Names[0])
    computer = Player("O",board_items,"COM")
    while winner == False:
        Player1.player_trigger()
        display_board()
        if tie():
            print("its a tie")
            break
        if winning():
            print(str(Player1.get_name()).upper()+ "has won ")
            break
        print("generating AI response ---------------")
        time.sleep(1)
        computer.computer()
        display_board()
        if tie():
            print("its a tie")
            break
        if winning():
            print(str(computer.get_name()).upper()+ "has won ")
            break