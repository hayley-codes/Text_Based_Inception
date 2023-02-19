# Gary Lie & Hayley Collins
# Jan. 15, 2023
# A text based game.
# This game combinds the pricinples of Inception with a bit of world cup. Yassine Bounou will go through three of the locations that the movie Inception did and then will end in Morroco, the world cup team member's home country. 

import random 
import os
import time
#these are our modules
#these two items are defined before the code so they can be used in the word command function.
items_inventory = []
country = "Japan"

def checkWords(var):
  if var == ("info"):
    print("What a time to be alive! Your country, Morroco is hosting the world cup and you have reached the finals against Portugal. As you are on your plane to Qutar, someone comes up behind you, and pushed you out of the plane!\n")
    print("You wake up in a city you do not recongnize, you hear a women's voice \"Welcome, Yassine. You are in Nijo Castle of Kyoto, Japan. You are in a maze, deep within the caslte. Your first task is to figure out how many layers of dream you are in if you want to live and escape.\"\n")
#information of our game
  elif var == ("quit"):
    print("You have chosen to exit the game.")
    time.sleep(5)
    exit()
#a way to quit the game
  elif var == ("inventory"):
    print(f"Inventory: {items_inventory}")
    time.sleep(5)
#to see what is in your inventory
  elif var == ("location"):
    print(f"You are in {country}.")
    time.sleep(5)
#location to determine where you are on your journey
  elif var == ("help"):
    print("The 'info' command prints information which might give some idea of what the game is about.")
    print("The 'quit' command exits the game for you. ")
    print(" The 'inventory' command lists the objects in your possession.")
    print(" The 'location' command lists what country you are in.")
    print("PLEASE NOTE that after entering a command you must press the enter key on your keyboard.")
#to know the commands able to use
  return (" ")

print("What a time to be alive! Your country, Morroco is hosting the world cup and you have reached the finals against Portugal. As you are on your plane to Qutar, someone comes up behind you, and pushed you out of the plane!\n")

print("You wake up in a city you do not recongnize, you hear a women's voice \"Welcome, Yassine. You are in Nijo Castle of Kyoto, Japan. You are in a maze, deep within the caslte. Your first task is to figure out how many layers of dream you are in if you want to live and escape.\"\n")

help_print = input("\nFor more information on how to play type 'help': ")
if help_print == "help":
  print("The 'info' command prints information which might give some idea of what the game is about.")
  print("The 'quit' command exits the game for you. ")
  print(" The 'inventory' command lists the objects in your possession.")
  print(" The 'location' command lists what country you are in.")
  
else:
  print("Sorry I don't understand that please try again")

enter = input("When you are ready to begin, click enter.")
#you will see the print(checkWord(var)) function applied to every user-input variable to leave the option for them to ask for all kinds of help at any stage of the code. 
print(checkWords(enter))

os.system("clear")
#to let them know about functions
### THIS IS WHERE THE PUZZLE BEGINS
print("Using the 'WASD' keys escape through this deadly maze.")
print(" W - Move Forward\n A - Turn to the left\n D - Turn to the Right\n Look - Describes the room you are in or use look at (item) to view an item up close")
#instructions on how to play
i = 0
while i == 0 :
  action = input("\nEnter your action:").upper()
  print(checkWords(action))
  if action == "A":
    print ("You turned left. After a while you get to another intersection")
    break
  elif action == "W":
    print("You continue to run straight. Until a wall stops you.  You procceed to turn back around and ran to the intersection. ")
  elif action == "D": 
    print("You turned right. You keeping running straight until a wall stops you. You procceed to turn back around and ran to the intersection. ")
  elif action == "LOOK": 
    print("You look around and see a dark smudge on the floor. Time is ticking you better make a choice.")
  else: 
   print("That is not possible please try again")
 #what happens at the first intersection for the user.   
while i == 0:
  action = input("\nEnter your action:").upper()
  print(checkWords(action))
  if action == "W":
    print("You continued straight. Until you reach another intersection")
    break
  elif action == "A":
    print("You turn right. You keeping running straight until a wall stops you.  You procceed to turn back around and ran to the intersection. ")
  elif action == "D":
    print("You turn left. You keeping running straight until a wall stops you.  You procceed to turn back around and ran to the intersection. ")
  elif action == "LOOK": 
    print("You look up to see a mural of soccer legends. Pele, Maradona, Cruyff, Di Stefano, Bobby Moore all loking down on your journey")
  else: 
    print("That is not possible please try again")
#what happens at the second intersection for the user.
while i == 0:
  action = input("\nEnter your action:").upper()
  print(checkWords(action))
  if action == "W":
    print("You continue to run straight. Until a wall stops you. You procceed to turn back around back to the intersection")  
  elif action == "A":
    print("You turn left. You keeping running straight until a wall stops you. You procceed to turn back around back to the intersection. ")
  elif action == "D":
    print("Yet again you continue on your journey until you arrive at an intersection where you can only go left or right. Up above there is an inscription stating \"One path will lead you to death the other to the puzzle\"")
    break
  elif action == "LOOK": 
    print("You see a portrait of a women which motivates you to continue your quest.")
  else: 
    print("That is not possible please try again")
#what happens at the third intersection for the user. 
while i == 0:
  action = input("\nEnter your action:").upper()
  print(checkWords(action))
  if action == "D":
    print("You picked the left path. After a while of running you see the light. This leads you to the riddle")
    break
  elif action == "A":
    print("You turn to the left. And slowly you hear a rumble growing in volume. The ground starts to shake and you feel the vibration all over your body. Chuncks of the path starts to fall down into a pit of lava. You quickly run back to the intersection before you get stuck forever.")
  elif action == "W":      
    print("You cannot walk forward!")
  elif action == "LOOK":
    print("It seems like going right is the better path!")
  else:
    print("That is not possible please try again")
#Fourth intersectio wehre the user must make a choice. With a twist as picking the wrong path will cause them to lose at the game.
while i == 0:
  action = input("\nEnter your action:").upper()
  print(checkWords(action))
  if action == "LOOK":
    print("\nSolve this problem to figure how many dreams there are.")
    print("How many days of the week is the answer to your first number.\nNext multiply it to the number of basketball players on the court for a single team. \nAfter, find the smallest positive interger which is non prime and add it.\nFinally, divide it by an unlucky number")
    break
  elif action == "W" or "A" or "D":
    print("You can not move!")
  else:
    print("That is not possible please try again.")
#The riddle and how to acces it for the user.
go = 0
while go == 0:
  dream = input("\nWhat is the answer? ").lower()
  print(checkWords(dream))
  if (dream == "3") or (dream =="three"):
      print("That is correct. Go on your journey to find the first item to return back to reality. Wait a couple more seconds. ")
      go = 1
  else:   
    print("Incorrect '\033[1m' Try Again! '\033[0m'")
#to get the riddle answer
time.sleep(10)
os.system("clear")

### THIS IS WHERE THE ITEMS START
#item one
print("You enter a room in the palace, on a table in the entry-way you see a completed rubix cube with solid coloured faces. You can only pick up the rubix cube if it is showing the red face upwards but you cannot see it once it begins to spin.")

colours = ["red", "blue", "white", "yellow", "orange","green"]

want_spin = input("When you are ready for it to begin spinning, click enter.").lower()
print(checkWords(want_spin))
# The face_up is defined as something random so it can enter the while loop to let the user try and and pick up the cube. 
face_up = "blue"

while face_up != "red":
  face_up = random.choice(colours)
  pick_up = input("Type 'yes' to pick up: ").lower()
  print(checkWords(pick_up))
  print(f"The colour is {face_up}.")
  #below are the parameters for if it can be picked up.
  if ((pick_up == "yes") or (pick_up == "yea") or (pick_up == "yup")) and face_up == ("red"):
    items_inventory.append("Rubix cube.")
    print("The rubix cube has been added to your items inventory.")
  elif ((pick_up == "yes") or (pick_up == "yea") or (pick_up == "yup")) and face_up != ("red"):
    print("You failed. You cannot pick this up.")
  elif ((pick_up == "no") or (pick_up == "nah") or (pick_up == "nope")) and face_up == ("red"):
    print("You should have picked it up, you missed the red. Now you have to keep trying.")
  else:
    print("Keep trying.")

print(f"Here are the items in your inventory: {items_inventory}. Wait a few more seconds.")

time.sleep(10)
os.system("clear")

print("Now that you have collected the cube, you wake up in Mombassa, Kenya. You know this must not be home because you found out from the riddle that you must go through 2 more cities before you are actually awake.")
print()

#item two: get the key
country = "Kenya"
#inside this function is a game where the variable the computer chooses must match that of the user so they can unlock the door. The funtion plays the game over until the user inputs a correctly matching input and then appends it to the inventory.
def play():
  user = input("You must unlock a door to a house on the street to avoid a bustling marketplace chase. If the people running through the market in Mombassa see you for too long, they may begin to attack. To choose the square key, enter 'square', to choose the circle key, enter 'circle', to choose the triangle key, enter 'triangle':  ").lower()
  print(checkWords(user))
  computer = random.choice(['square', 'circle', 'triangle'])

  if user == computer:
    print(f"You chose {user} and the given door was the {computer} door. You unloked the door and get to keep the key!")
    items_inventory.append(user)
  else:
    print(f"You chose {user} and the given door was the {computer} door. You failed to unlock the door. Please wait 5 seconds to try again.")
    time.sleep(5)
    os.system("clear")
    play()

play()

print(f"The items in your inventory: {items_inventory}")

time.sleep(10)
os.system("clear")

print("You walk through the door you unlocked and ascend unexpectedly into a new layer, Paris! Only one more layer to go.")

country = "Paris, France"

#ITEM THREE
print("You arrive in Paris, France in front of the Eiffel Tower. You are mesmorized by the city of lights until a stranger taps your shoulder. As you turn around to look at her, she tells you her name is Ariadne and she has put you in this dream because she was payed by the Portuguese team. However, since her friend Dom's favourite team is Morroco, she says she will release you only if you can guess her word before the Jack in the Box pops out. ")

time.sleep(3)

print("\n\nIn order to get the item, you must guess a letter one at a time in order to guess the word. If you fail you get stuck here forever. Remember you can only make 5 mistakes. \n")
time.sleep(3)


# The parameters we use in order to make sure the item 3 game runs.
def main():
    global sum
    global display
    global word
    global guessed
    global length
    global play_game
    possibilities = ["avenue","soccer","door","computer","broom", "beauty","horse","imperfect","joyous","kill","anguish","nationalism","obligation"]
    word = random.choice(possibilities)
    length = len(word)
    sum = 0
    display = '_' * length
    guessed = []
    

# The main part of the code that contains all the instructions on how it should be played.
def hangman():
    global sum
    global display
    global word
    global guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + " \nEnter your guess: ")
    print(checkWords(guess))
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
#To make sure that the user doesn't use a charachter or number.
    elif guess in word:
        guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
#if the letter guessed is correct then it will display it onto the console.
    elif guess in guessed:
        print("Try another letter.\n")
#if you already guessed a letter then it will tell you to guess a different one.
    else:
        sum += 1
        if sum == 1:
            time.sleep(1)
            print("+------+.   ")
            print("|`.    | `. ")
            print("|  `+--+---+")
            print("|   |  |   |")
            print("+---+--+.  |")
            print(" `. |    `.|")
            print("   `+------+")
        
            print("\nWrong letter. " + str(limit - sum) + " guesses remaining\n")
          
        elif sum == 2:
          time.sleep(1)
          print("+------+.   ")
          print("|`.    | `. ")
          print("|  `+--+---+")
          print("|   |  |   |")
          print("+---+--+.  |")
          print(" `. |    `.|")
          print("   `+------+")
        
          print("\nWrong letter. " + str(limit - sum) + " guesses remaining\n")


        elif sum == 3:
          time.sleep(1)
          print("+------+.   ")
          print("|`.    | `. ")
          print("|  `+--+---+")
          print("|   |  |   |")
          print("+---+--+.  |")
          print(" `. |    `.|")
          print("   `+------+")
        
          print("\nWrong letter. " + str(limit - sum) + " guesses remaining\n")

        elif sum == 4:
            time.sleep(1)
            print("+------+.   ")
            print("|`.    | `. ")
            print("|  `+--+---+")
            print("|   |  |   |")
            print("+---+--+.  |")
            print(" `. |    `.|")
            print("   `+------+")
            print("\nWrong letter. " + str(limit - sum) + " last guess remaining\n")

        elif sum == 5:
          time.sleep(1)
          print("         _,;;.,_             \n"
                ",-;;,_  ;,',,,'''@           \n"
                ",;;``  `'\\|//``-:;,.        \n"
                "@`       ;^^^;      `'@\"    \n"
                "         :@ @:               \n"
                "         \ u /               \n"
                ",=,------)^^^(------,=,      \n"
                "'-'-----/=====\-----'-'      \n"
                "        \_____/              \n"
                "    '`\ /_____\              \n"
                "    `\ \\\_____/_            \n"
                "      \//_____\/|            \n"
                "      |        ||            \n"
                "      |        |'            \n"
                "      :________:`            \n")
          print("Wrong guess. Too Late! You were unable to get the word! \n")
          print("The word was:",guessed,word)
          retry = input("(Y for yes and N for no)Do you want to turn back time and try again? ").upper()
# to add a number to sum and then to tell the user they have only a certain amount of guesses remaining. If you get 5 mistakes your game is over.
          print(checkWords(retry))
          if retry == "Y" or "YES":
            print("\nTurning back the time\n\n")
            main()
          elif retry == "N or NO":
            print("You are stuck in Paris dream land forever. In the real world you are permanently a vegetable")
            print("'\033[1m' GAME OVER '\033[0m'Thank You for playing!")
#to give an option to retry to be ablw to complete the game.   
           
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
#if all the letters are filled then you are right
    elif sum != limit:
        hangman()

main()
hangman()
time.sleep(5)
os.system("clear")

#Ariadne interaction - this is the final interaction where the user ultimatly chooses to empty their inventory in exchange for freedom or keeping their items instead of handing them over to Ariadne. 
print("Ariadne says 'Since you have guessed my word, I only need one more thing from you before I can let you go.'")
print("")
print(f"Inventory = {items_inventory}")
print("")
print("Once you hand over the rubix cube and the key, the people around us will begin to attack. You dying is the only way I can send you back without taking any blame from my client.")

print("")
aridane_inventory = []
hand_over = input("Will you hand over your items? 'Yes' to give them and 'No' to stay and die.").lower()
print(checkWords(hand_over))
if hand_over == "yes":
  aridane_inventory.append(items_inventory)
  items_inventory = []
  print(f"Ariadne's inventory : {aridane_inventory}")
  print("Your inventory : ")
  print("")
  time.sleep(5)
  os.system("clear")
  print("You eyes whip open after a man walks up and stabs you, and you find yourself back on the plane, your Morrocan teamates surrounding you. You sag back into your chair, releived to have exited the dream. But wait. If this is reality, where is the man who pushed you in the first place? Why are you still on the plane?")
else:
  print("Ariadne scoffs and walks away. 'Have it your way then!', she calls behind her back.")
  print("'\033[1m'YOU'RE DONE THE GAME.")