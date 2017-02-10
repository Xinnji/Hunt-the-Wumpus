# WumpusHunt.py
# by Jason Scott-Hakanson
# This is a recreation of the classic text game Hunt the Wumpus by Greg Yob, made totally
# from scratch based only off of the gameplay seen in other versions of "Hunt the Wumpus".

from random import *
from time import sleep


### ONE GAME TURN ###
def Turn():
    global currentRoom
    global Arrow
    global arrowRoom
    global adjRoom1
    global adjRoom1a
    global adjRoom2
    global adjRoom2a
    global adjRoom3
    global adjRoom3a
    global winCon
    global turnCount
    global Bat1
    global Bat2
    global Pit1
    global Pit2
    global Wumpus

    World()
    Encounter()
    Rooms()
    Act()
    if winCon:
        Win()
    else:
        pass
    if Arrow < 1:
        loseArrow()
    World()
    turnCount = turnCount + 1
    arrowRoom = None
    Turn()


### MENU TO BEGIN GAME ###
def StartMenu():
    try:
        start = str(input())
        if start[0] in ["y","Y"]:
            print("You enter the lair of the Wumpus...")
            print("———————————————————————————————————")
            sleep(1)
            Hazards()
            Turn()
        elif start[0] in ["n","N"]:
            print("Well why did you open this in the first place then?")
            if input("Are you sure you want to quit?\n")[0] in ["y","Y"]:
                pass
            else:
                print("I knew you wanted to play still.\n")
                print("Would you like to start a new game? (y/n/i)")
                StartMenu()
    
        elif start[0] in ["i","I"]:
            print("INSTRUCTIONS:\n")
            print("Welcome to a remake of Hunt the Wumpus by Jason Scott-Hakanson. In this game, you, an intrepid Wumpus Hunter, are tasked with entering the dark, twisting passages of the Wumpus's lair and killing it for fame, glory, and a nice coat.")
            print("Beware! There are many hazards in the lair of the Wumpus. Bottomless pits, nests of giant superbats and the Wumpus itself await you; Do not enter the rooms in which they await lest you fall to your death, be carried away or get eaten.")
            print("Using your senses you can tell when dangers are adjacent to the room you stand in. Locate the Wumpus in this way, and shoot it with a wumpus-piercing Crooked Arrow. But do not waste them; You only have 5.")
            print("Would you like to start a new game? (y/n/i)\n")
            StartMenu()
        else:
            StartMenu()
    except IndexError:
        StartMenu()

        

### ADJACENT ROOM FUNCTIONS ###
def World():
    global currentRoom
    global Arrow
    global arrowRoom
    global adjRoom1
    global adjRoom1a
    global adjRoom2
    global adjRoom2a
    global adjRoom3
    global adjRoom3a
    global winCon
    global turnCount
    global Bat1
    global Bat2
    global Pit1
    global Pit2
    global Wumpus

    if currentRoom == 1:
        adjRoom1 = 2
        adjRoom2 = 5
        adjRoom3 = 8
    if currentRoom == 2:
        adjRoom1 = 3
        adjRoom2 = 1
        adjRoom3 = 10
    if currentRoom == 3:
        adjRoom1 = 4
        adjRoom2 = 2
        adjRoom3 = 12
    if currentRoom == 4:
        adjRoom1 = 5
        adjRoom2 = 3
        adjRoom3 = 14
    if currentRoom == 5:
        adjRoom1 = 1
        adjRoom2 = 4
        adjRoom3 = 6
    if currentRoom == 6:
        adjRoom1 = 15
        adjRoom2 = 7
        adjRoom3 = 5
    if currentRoom == 7:
        adjRoom1 = 8
        adjRoom2 = 6
        adjRoom3 = 17
    if currentRoom == 8:
        adjRoom1 = 9
        adjRoom2 = 7
        adjRoom3 = 1
    if currentRoom == 9:
        adjRoom1 = 10
        adjRoom2 = 8
        adjRoom3 = 18
    if currentRoom == 10:
        adjRoom1 = 11
        adjRoom2 = 9
        adjRoom3 = 2
    if currentRoom == 11:
        adjRoom1 = 12
        adjRoom2 = 10
        adjRoom3 = 19
    if currentRoom == 12:
        adjRoom1 = 13
        adjRoom2 = 11
        adjRoom3 = 3
    if currentRoom == 13:
        adjRoom1 = 14
        adjRoom2 = 12
        adjRoom3 = 20
    if currentRoom == 14:
        adjRoom1 = 15
        adjRoom2 = 13
        adjRoom3 = 4
    if currentRoom == 15:
        adjRoom1 = 6
        adjRoom2 = 14
        adjRoom3 = 16
    if currentRoom == 16:
        adjRoom1 = 17
        adjRoom2 = 20
        adjRoom3 = 15
    if currentRoom == 17:
        adjRoom1 = 18
        adjRoom2 = 16
        adjRoom3 = 7     
    if currentRoom == 18:
        adjRoom1 = 19
        adjRoom2 = 17
        adjRoom3 = 9
    if currentRoom == 19:
        adjRoom1 = 20
        adjRoom2 = 18
        adjRoom3 = 11     
    if currentRoom == 20:
        adjRoom1 = 16
        adjRoom2 = 19
        adjRoom3 = 13


### ARROW PERSISTENCE WORLD ###
def ArrowWorld():
    global currentRoom
    global Arrow
    global arrowRoom
    global adjRoom1
    global adjRoom1a
    global adjRoom2
    global adjRoom2a
    global adjRoom3
    global adjRoom3a
    global winCon
    global turnCount
    global Bat1
    global Bat2
    global Pit1
    global Pit2
    global Wumpus

    if arrowRoom == 1:
        adjRoom1a = 2
        adjRoom2a = 5
        adjRoom3a = 8
    elif arrowRoom == 2:
        adjRoom1a = 3
        adjRoom2a = 1
        adjRoom3a = 10
    elif arrowRoom == 3:
        adjRoom1a = 4
        adjRoom2a = 2
        adjRoom3a = 12
    elif arrowRoom == 4:
        adjRoom1a = 5
        adjRoom2a = 3
        adjRoom3a = 14
    elif arrowRoom == 5:
        adjRoom1a = 1
        adjRoom2a = 4
        adjRoom3a = 6
    elif arrowRoom == 6:
        adjRoom1a = 15
        adjRoom2a = 7
        adjRoom3a = 5
    elif arrowRoom == 7:
        adjRoom1a = 8
        adjRoom2a = 6
        adjRoom3a = 17
    elif arrowRoom == 8:
        adjRoom1a = 9
        adjRoom2a = 7
        adjRoom3a = 1
    elif arrowRoom == 9:
        adjRoom1a = 10
        adjRoom2a = 8
        adjRoom3a = 18
    elif arrowRoom == 10:
        adjRoom1a = 11
        adjRoom2a = 9
        adjRoom3a = 2
    elif arrowRoom == 11:
        adjRoom1a = 12
        adjRoom2a = 10
        adjRoom3a = 19
    elif arrowRoom == 12:
        adjRoom1a = 13
        adjRoom2a = 11
        adjRoom3a = 3
    elif arrowRoom == 13:
        adjRoom1a = 14
        adjRoom2a = 12
        adjRoom3a = 20
    elif arrowRoom == 14:
        adjRoom1a = 15
        adjRoom2a = 13
        adjRoom3a = 4
    elif arrowRoom == 15:
        adjRoom1a = 6
        adjRoom2a = 14
        adjRoom3a = 16
    elif arrowRoom == 16:
        adjRoom1a = 17
        adjRoom2a = 20
        adjRoom3a = 15
    elif arrowRoom == 17:
        adjRoom1a = 18
        adjRoom2a = 16
        adjRoom3a = 7     
    elif arrowRoom == 18:
        adjRoom1a = 19
        adjRoom2a = 17
        adjRoom3a = 9
    elif arrowRoom == 19:
        adjRoom1a = 20
        adjRoom2a = 18
        adjRoom3a = 11     
    elif arrowRoom == 20:
        adjRoom1a = 16
        adjRoom2a = 19
        adjRoom3a = 13


### HAZARD LOCATIONS ###
def Hazards():
    global currentRoom
    global Arrow
    global arrowRoom
    global adjRoom1
    global adjRoom1a
    global adjRoom2
    global adjRoom2a
    global adjRoom3
    global adjRoom3a
    global winCon
    global turnCount
    global Bat1
    global Bat2
    global Pit1
    global Pit2
    global Wumpus

    currentRoom = randint(1,20)
    Arrow = 5
    arrowRoom = "Marcus is a butt #EasterEgg"
    winCon = False
    adjRoom1 = None
    adjRoom2 = None
    adjRoom3 = None
    adjRoom1a = None
    adjRoom2a = None
    adjRoom3a = None
    turnCount = 1

    Pit1 = randint(1,20)
    while Pit1 in [currentRoom]:
        Pit1 = randint(1,20)

    Pit2 = randint(1,20)
    while Pit2 in [currentRoom, Pit1]:
        Pit2 = randint(1,20)

    Bat1 = randint(1,20)
    while Bat1 in [currentRoom, Pit1, Pit2]:
        Bat1 = randint(1,20)

    Bat2 = randint(1,20)
    while Bat2 in [currentRoom, Pit1, Pit2, Bat1]:
        Bat2 = randint(1,20)

    Wumpus = randint(1,20)
    while Wumpus in [currentRoom]:
        Wumpus = randint(1,20)


### CHECK IF YOU IS THE DEADLES ###
def Encounter():
    global currentRoom
    global Arrow
    global arrowRoom
    global adjRoom1
    global adjRoom1a
    global adjRoom2
    global adjRoom2a
    global adjRoom3
    global adjRoom3a
    global winCon
    global turnCount
    global Bat1
    global Bat2
    global Pit1
    global Pit2
    global Wumpus

    if currentRoom in [Pit1,Pit2]:
        losePit()
    elif currentRoom in [Wumpus]:
        loseWumpus()
    if currentRoom in [Bat1,Bat2]:
        check = currentRoom
        currentRoom = randint(1,20)
        while check == currentRoom:
            currentRoom = randint(1,20)
            World()
        print()
        print("You wandered into a nest of superbats! They carry you to a random room.")


### PRINT WHAT ROOMS ARE NEAR ###
def Rooms():
    global currentRoom
    global Arrow
    global arrowRoom
    global adjRoom1
    global adjRoom1a
    global adjRoom2
    global adjRoom2a
    global adjRoom3
    global adjRoom3a
    global winCon
    global turnCount
    global Bat1
    global Bat2
    global Pit1
    global Pit2
    global Wumpus

    World()
    Danger()
    print("You are in Room " + str(currentRoom) + ".")
    print("There are passages to Rooms " + str(adjRoom1) + ", " + str(adjRoom2) + ", and " + str(adjRoom3) + ".")
    sleep(1)
    print("What will you do? (shoot/move/quit)")

    
### GIVES USER INPUT TO SHOOT OR MOVE ###
def Act():
    act = input()
    try:
        if act[0] in ["m","M"]:
            print("Move to which room? (# or stay)")
            Move()
        elif act[0] in ["s","S"]:
            print("How far will the arrow fly? (1-5 rooms. 0 to not shoot.)")
            Shoot()
        elif act[0] in ["q","Q"]:
            loseQuit()
        else:
            if len(act) >= 18:
                print("I don't know what \"" + act[0:18] + "...\" means.")
            else:
                print("I don't know what \"" + act + "\" means.")
            Act()
    except IndexError:
        Act()


### MOVE FUNCTIONS ###
def Move():
    global currentRoom
    global Arrow
    global arrowRoom
    global adjRoom1
    global adjRoom1a
    global adjRoom2
    global adjRoom2a
    global adjRoom3
    global adjRoom3a
    global winCon
    global turnCount
    global Bat1
    global Bat2
    global Pit1
    global Pit2
    global Wumpus

    try:
        move = input()
        if int(move) == adjRoom1:
            currentRoom = adjRoom1
            sleep(1)
        elif int(move) == adjRoom2:
            currentRoom = adjRoom2
            sleep(1)
        elif int(move) == adjRoom3:
            currentRoom = adjRoom3
            sleep(1)
        elif move == ["stay","Stay"]:
            print("\"I guess I won't move yet.\"\n")
            Act()
        elif int(move) == currentRoom:
            print("\"I guess I won't move yet.\"\n")
            Act()
        else:
            print("There are no passages to that room.")
            Move()
    except ValueError:
            Move()
        

### SHOOT FUNCTIONS ###
def Shoot():
    global currentRoom
    global Arrow
    global arrowRoom
    global adjRoom1
    global adjRoom1a
    global adjRoom2
    global adjRoom2a
    global adjRoom3
    global adjRoom3a
    global winCon
    global turnCount
    global Bat1
    global Bat2
    global Pit1
    global Pit2
    global Wumpus

    try:
        shoot = int(input())
        arrowRoom = currentRoom

        if shoot == 1:
            ArrowWorld()
            
            shoot = input("Which room will the arrow fly into?\n")
            if shoot == adjRoom1a:
                arrowRoom = adjRoom1a
            elif shoot == adjRoom2a:
                arrowRoom = adjRoom2a
            elif shoot == adjRoom3a:
                arrowRoom = adjRoom3a
            else:
                arrowRoom = choice([adjRoom1a, adjRoom2a, adjRoom3a])

            ArrowWorld()

            if arrowRoom == Wumpus:
                winCon = True
                arrowRoom = None

        elif shoot == 2:
            ArrowWorld()
            
            shoot = input("Which room will the arrow fly into? (1/2)\n")
            if shoot == adjRoom1a:
                arrowRoom = adjRoom1a
            elif shoot == adjRoom2a:
                arrowRoom = adjRoom2a
            elif shoot == adjRoom3a:
                arrowRoom = adjRoom3a
            else:
                arrowRoom = choice([adjRoom1a, adjRoom2a, adjRoom3a])

            ArrowWorld()

            if arrowRoom == Wumpus:
                winCon = True
                arrowRoom = None

            ArrowWorld()
            
            shoot = input("Which room will the arrow fly into? (2/2)\n")
            if shoot == adjRoom1a:
                arrowRoom = adjRoom1a
            elif shoot == adjRoom2a:
                arrowRoom = adjRoom2a
            elif shoot == adjRoom3a:
                arrowRoom = adjRoom3a
            else:
                arrowRoom = choice([adjRoom1a, adjRoom2a, adjRoom3a])

            ArrowWorld()

            if arrowRoom == Wumpus:
                winCon = True
                arrowRoom = None

        elif shoot == 3:
            ArrowWorld()
            
            shoot = input("Which room will the arrow fly into? (1/3)\n")
            if shoot == adjRoom1a:
                arrowRoom = adjRoom1a
            elif shoot == adjRoom2a:
                arrowRoom = adjRoom2a
            elif shoot == adjRoom3a:
                arrowRoom = adjRoom3a
            else:
                arrowRoom = choice([adjRoom1a, adjRoom2a, adjRoom3a])

            ArrowWorld()

            if arrowRoom == Wumpus:
                winCon = True
                arrowRoom = None

            ArrowWorld()
            
            shoot = input("Which room will the arrow fly into? (2/3)\n")
            if shoot == adjRoom1a:
                arrowRoom = adjRoom1a
            elif shoot == adjRoom2a:
                arrowRoom = adjRoom2a
            elif shoot == adjRoom3a:
                arrowRoom = adjRoom3a
            else:
                arrowRoom = choice([adjRoom1a, adjRoom2a, adjRoom3a])

            ArrowWorld()

            if arrowRoom == Wumpus:
                winCon = True
                arrowRoom = None

            ArrowWorld()
            
            shoot = input("Which room will the arrow fly into? (3/3)\n")
            if shoot == adjRoom1a:
                arrowRoom = adjRoom1a
            elif shoot == adjRoom2a:
                arrowRoom = adjRoom2a
            elif shoot == adjRoom3a:
                arrowRoom = adjRoom3a
            else:
                arrowRoom = choice([adjRoom1a, adjRoom2a, adjRoom3a])

            ArrowWorld()

            if arrowRoom == Wumpus:
                winCon = True
                arrowRoom = None

        elif shoot == 4:
            ArrowWorld()
            
            shoot = input("Which room will the arrow fly into? (1/4)\n")
            if shoot == adjRoom1a:
                arrowRoom = adjRoom1a
            elif shoot == adjRoom2a:
                arrowRoom = adjRoom2a
            elif shoot == adjRoom3a:
                arrowRoom = adjRoom3a
            else:
                arrowRoom = choice([adjRoom1a, adjRoom2a, adjRoom3a])

            ArrowWorld()

            if arrowRoom == Wumpus:
                winCon = True
                arrowRoom = None

            ArrowWorld()
            
            shoot = input("Which room will the arrow fly into? (2/4)\n")
            if shoot == adjRoom1a:
                arrowRoom = adjRoom1a
            elif shoot == adjRoom2a:
                arrowRoom = adjRoom2a
            elif shoot == adjRoom3a:
                arrowRoom = adjRoom3a
            else:
                arrowRoom = choice([adjRoom1a, adjRoom2a, adjRoom3a])

            ArrowWorld()

            if arrowRoom == Wumpus:
                winCon = True
                arrowRoom = None

            ArrowWorld()
            
            shoot = input("Which room will the arrow fly into? (3/4)\n")
            if shoot == adjRoom1a:
                arrowRoom = adjRoom1a
            elif shoot == adjRoom2a:
                arrowRoom = adjRoom2a
            elif shoot == adjRoom3a:
                arrowRoom = adjRoom3a
            else:
                arrowRoom = choice([adjRoom1a, adjRoom2a, adjRoom3a])

            ArrowWorld()

            if arrowRoom == Wumpus:
                winCon = True
                arrowRoom = None

            ArrowWorld()
            
            shoot = input("Which room will the arrow fly into? (4/4)\n")
            if shoot == adjRoom1a:
                arrowRoom = adjRoom1a
            elif shoot == adjRoom2a:
                arrowRoom = adjRoom2a
            elif shoot == adjRoom3a:
                arrowRoom = adjRoom3a
            else:
                arrowRoom = choice([adjRoom1a, adjRoom2a, adjRoom3a])

            ArrowWorld()

            if arrowRoom == Wumpus:
                winCon = True
                arrowRoom = None

        elif shoot == 5:
            ArrowWorld()
            
            shoot = input("Which room will the arrow fly into? (1/5)\n")
            if shoot == adjRoom1a:
                arrowRoom = adjRoom1a
            elif shoot == adjRoom2a:
                arrowRoom = adjRoom2a
            elif shoot == adjRoom3a:
                arrowRoom = adjRoom3a
            else:
                arrowRoom = choice([adjRoom1a, adjRoom2a, adjRoom3a])

            ArrowWorld()

            if arrowRoom == Wumpus:
                winCon = True
                arrowRoom = None

            ArrowWorld()
            
            shoot = input("Which room will the arrow fly into? (2/5)\n")
            if shoot == adjRoom1a:
                arrowRoom = adjRoom1a
            elif shoot == adjRoom2a:
                arrowRoom = adjRoom2a
            elif shoot == adjRoom3a:
                arrowRoom = adjRoom3a
            else:
                arrowRoom = choice([adjRoom1a, adjRoom2a, adjRoom3a])

            ArrowWorld()

            if arrowRoom == Wumpus:
                winCon = True
                arrowRoom = None

            ArrowWorld()
            
            shoot = input("Which room will the arrow fly into? (3/5)\n")
            if shoot == adjRoom1a:
                arrowRoom = adjRoom1a
            elif shoot == adjRoom2a:
                arrowRoom = adjRoom2a
            elif shoot == adjRoom3a:
                arrowRoom = adjRoom3a
            else:
                arrowRoom = choice([adjRoom1a, adjRoom2a, adjRoom3a])

            ArrowWorld()

            if arrowRoom == Wumpus:
                winCon = True
                arrowRoom = None

            ArrowWorld()
            
            shoot = input("Which room will the arrow fly into? (4/5)\n")
            if shoot == adjRoom1a:
                arrowRoom = adjRoom1a
            elif shoot == adjRoom2a:
                arrowRoom = adjRoom2a
            elif shoot == adjRoom3a:
                arrowRoom = adjRoom3a
            else:
                arrowRoom = choice([adjRoom1a, adjRoom2a, adjRoom3a])

            ArrowWorld()

            if arrowRoom == Wumpus:
                winCon = True
                arrowRoom = None

            ArrowWorld()
            
            shoot = input("Which room will the arrow fly into? (5/5)\n")
            if shoot == adjRoom1a:
                arrowRoom = adjRoom1a
            elif shoot == adjRoom2a:
                arrowRoom = adjRoom2a
            elif shoot == adjRoom3a:
                arrowRoom = adjRoom3a
            else:
                arrowRoom = choice([adjRoom1a, adjRoom2a, adjRoom3a])

            ArrowWorld()

            if arrowRoom == Wumpus:
                winCon = True
                arrowRoom = None

        elif shoot == 0:
            print("\"I quess I won't shoot yet.\"")
            Act()
        else:
            print("Arrows can't fly that far.")
            Shoot()
            
        Arrow = Arrow - 1
        if winCon == False:
            Wumpus == randint(1,20)
            print("You missed! You hear the Wumpus awake as it moves to a new room.")

        print("You have " + str(Arrow) + " arrows left.")

    except ValueError:
        Shoot()


### DEATH LOSSES FUNCTIONS ###
def loseArrow():
    global turnCount
    
    print()
    print("You have run out of arrows and have no way to kill the Wumpus now.\nYour adventure is at an end.")
    print("————————————————————————————")
    print()
    print("YOU HAVE LOST THE GAME.")
    print()
    if turnCount == 1:
        print("You only adventured for 1 turn.")
    else:
        print("You adventured for " + str(turnCount) + " turns.")
    print()
    print("Would you like to start a new game? (y/n/i)")
    StartMenu()


def loseShoot():
    global turnCount

    print()
    print("\"Ow! I've been shot!\"")
    print("You somehow managed to shoot yourself with a Crooked Arrow!")
    print()
    print("YOU ARE DEAD.")
    print()
    if turnCount == 1:
        print("You survived for 1 turn.")
    else:
        print("You survived for " + str(turnCount) + " turns.")
    print()
    print("Would you like to start a new game? (y/n/i)")
    StartMenu()

    
def losePit():
    global turnCount
    
    print()
    print("\"WAAAAAAAAAAAAAAAAAAAAAAaaaaaaahhhhhhh!...\"")
    print("You have fallen into a bottomless pit with no escape. Your adventure is at an end.")
    print()
    print("YOU ARE DEAD.")
    print()
    if turnCount == 1:
        print("You survived for 1 turn.")
    else:
        print("You survived for " + str(turnCount) + " turns.")
    print()
    print("Would you like to start a new game? (y/n/i)")
    StartMenu()


def loseWumpus():
    global turnCount

    print()
    print("As you enter the room, you hear a loud growling, and realize your mistake as a Wumpus awakes and eats you alive.")
    print()
    print("YOU ARE DEAD.")
    print()
    if turnCount == 1:
        print("You survived for 1 turn.")
    else:
        print("You survived for " + str(turnCount) + " turns.")
    print()
    print("Would you like to start a new game? (y/n/i)")
    StartMenu()


def loseQuit():
    global turnCount
    
    print()
    print("Cracking under the pressure, you decide to end it all rather than face your inevitable death via Wumpus.")
    print()
    print("YOU ARE DEAD.")
    print()
    if turnCount == 1:
        print("You survived for 1 turn.")
    else:
        print("You survived for " + str(turnCount) + " turns.")
    print()
    print("Would you like to start a new game? (y/n/i)")
    StartMenu()


def Win():
    global turnCount
    
    print()
    print("You successfully located and killed the Wumpus! This deed will be sung of for generations.")
    print()
    print("CONGRATULATIONS! YOU HAVE WUM!")
    print()
    if turnCount == 1:
        print("You won in 1 turn!!!!!!!!!!!!!!!!!!! You are officially on the leaderboard for the top Wumpus Hunters. (WiP)")
    else:
        print("You won in " + str(turnCount) + " turns.")
    print()
    print("Would you like to start a new game? (y/n/i)")
    StartMenu()

       
## TELLS THE PLAYER IF THERE IS A DANGER ADJACENT ###    
def Danger():
    global currentRoom
    global Arrow
    global arrowRoom
    global adjRoom1
    global adjRoom1a
    global adjRoom2
    global adjRoom2a
    global adjRoom3
    global adjRoom3a
    global winCon
    global turnCount
    global Bat1
    global Bat2
    global Pit1
    global Pit2
    global Wumpus
    
    if Bat1 in [adjRoom1,adjRoom2,adjRoom3]:
        print()
        print("There is a rustling of wings nearby.")
    elif Bat2 in [adjRoom1,adjRoom2,adjRoom3]:
        print()
        print("There is a rustling of wings nearby.")
    if Pit1 in [adjRoom1,adjRoom2,adjRoom3]:
        print()
        print("You feel a slight draft.")
    elif Pit2 in [adjRoom1,adjRoom2,adjRoom3]:
        print()
        print("You feel a slight draft.")
    if Wumpus in [adjRoom1,adjRoom2,adjRoom3]:
        print()
        print("\"I smell a Wumpus.\"")
    print()
        
###############################################
print("HUNT THE WUMPUS")
print()
print("Would you like to start a new game? (y/n/i)")
StartMenu()
