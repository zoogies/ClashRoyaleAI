# This file is used to configure and auto detect screen settings
# Ryan Zmuda 2021

# TODO
# - add abridged setup for less complex ai behavior?
# - move all other configuration settings here to be read from the json by the main program

import json
import pyautogui
import os
import win32gui, win32con, win32com.client
import pyttsx3

name = ""
engine = pyttsx3.init()

os.system("cls" if os.name == "nt" else "clear")
print("This file will help you setup your screen bounds and coordinate values!")
print("Ryan Zmuda 2021")
print("")

if input("Would you like to enable debug output? y/n: ") == "y":
    debug = True
else:
    debug = False

if input("Would you like to enable tts? y/n :") == "y":
    tts = True
else:
    tts = False


def printHeaderClear():
    os.system("cls" if os.name == "nt" else "clear")
    print("This file will help you setup your screen bounds and coordinate values!")
    print("Ryan Zmuda 2021")
    print("")


def queryForPosition(name):
    printHeaderClear()
    print("Please hover your mouse over the ", name, ", then press enter")
    if tts:
        engine.say(name)
        engine.runAndWait()
    input("Waiting for you to press enter...")
    position = pyautogui.position()
    return position


# .d8888.  .o88b. d8888b. d88888b d88888b d8b   db    .d88b.  d8888b. d888888b  d888b  d888888b d8b   db
# 88'  YP d8P  Y8 88  `8D 88'     88'     888o  88   .8P  Y8. 88  `8D   `88'   88' Y8b   `88'   888o  88
# `8bo.   8P      88oobY' 88ooooo 88ooooo 88V8o 88   88    88 88oobY'    88    88         88    88V8o 88
#   `Y8b. 8b      88`8b   88~~~~~ 88~~~~~ 88 V8o88   88    88 88`8b      88    88  ooo    88    88 V8o88
# db   8D Y8b  d8 88 `88. 88.     88.     88  V888   `8b  d8' 88 `88.   .88.   88. ~8~   .88.   88  V888
# `8888Y'  `Y88P' 88   YD Y88888P Y88888P VP   V8P    `Y88P'  88   YD Y888888P  Y888P  Y888888P VP   V8P

# screen origin and bounds
screenOrigin = queryForPosition("very top left pixel of your clash royale screen")
screenBotRight = queryForPosition("very bottom right pixel of you clash royale screen")


# ask if the screen res looks right


# d8888b. d88888b  .o88b. db   dD    .o88b.  .d8b.  d8888b. d8888b. .d8888.
# 88  `8D 88'     d8P  Y8 88 ,8P'   d8P  Y8 d8' `8b 88  `8D 88  `8D 88'  YP
# 88   88 88ooooo 8P      88,8P     8P      88ooo88 88oobY' 88   88 `8bo.
# 88   88 88~~~~~ 8b      88`8b     8b      88~~~88 88`8b   88   88   `Y8b.
# 88  .8D 88.     Y8b  d8 88 `88.   Y8b  d8 88   88 88 `88. 88  .8D db   8D
# Y8888D' Y88888P  `Y88P' YP   YD    `Y88P' YP   YP 88   YD Y8888D' `8888Y'

# Elixer Text Location
elixerTextCenter = queryForPosition("elixer storage text")

# First Deck Card
card1TextCenter = queryForPosition("elixer value text of your first deck card")

# Second Deck Card
card2TextCenter = queryForPosition("elixer value text of your second deck card")

# Third Deck Card
card3TextCenter = queryForPosition("elixer value text of your third deck card")

# Fourth Deck Card
card4TextCenter = queryForPosition("elixer value text of your fourth deck card")


#  .o88b.  .d8b.  d8888b. d8888b.   .d8888.  .o88b. d8888b. d88888b d88888b d8b   db    .o88b. db      d888888b  .o88b. db   dD   d8888b.  .d88b.  d888888b d8b   db d888888b .d8888.
# d8P  Y8 d8' `8b 88  `8D 88  `8D   88'  YP d8P  Y8 88  `8D 88'     88'     888o  88   d8P  Y8 88        `88'   d8P  Y8 88 ,8P'   88  `8D .8P  Y8.   `88'   888o  88 `~~88~~' 88'  YP
# 8P      88ooo88 88oobY' 88   88   `8bo.   8P      88oobY' 88ooooo 88ooooo 88V8o 88   8P      88         88    8P      88,8P     88oodD' 88    88    88    88V8o 88    88    `8bo.
# 8b      88~~~88 88`8b   88   88     `Y8b. 8b      88`8b   88~~~~~ 88~~~~~ 88 V8o88   8b      88         88    8b      88`8b     88~~~   88    88    88    88 V8o88    88      `Y8b.
# Y8b  d8 88   88 88 `88. 88  .8D   db   8D Y8b  d8 88 `88. 88.     88.     88  V888   Y8b  d8 88booo.   .88.   Y8b  d8 88 `88.   88      `8b  d8'   .88.   88  V888    88    db   8D
#  `Y88P' YP   YP 88   YD Y8888D'   `8888Y'  `Y88P' 88   YD Y88888P Y88888P VP   V8P    `Y88P' Y88888P Y888888P  `Y88P' YP   YD   88       `Y88P'  Y888888P VP   V8P    YP    `8888Y'


# first card position
card1position = queryForPosition("position of your first deck card")


# second card position
card2position = queryForPosition("position of your second deck card")


# third card position
card3position = queryForPosition("position of your third deck card")


# fourth card position
card4position = queryForPosition("position of your fourth deck card")


# d88888b .88b  d88.  .d88b.  d888888b d88888b .d8888.
# 88'     88'YbdP`88 .8P  Y8. `~~88~~' 88'     88'  YP
# 88ooooo 88  88  88 88    88    88    88ooooo `8bo.
# 88~~~~~ 88  88  88 88    88    88    88~~~~~   `Y8b.
# 88.     88  88  88 `8b  d8'    88    88.     db   8D
# Y88888P YP  YP  YP  `Y88P'     YP    Y88888P `8888Y'

emoteMenu = queryForPosition("button to open the emote menu")
favoriteEmote = queryForPosition("emote you want the ai to use")


# db       .d8b.  d8b   db d88888b   d8888b.  .d88b.  db    db d8b   db d8888b. .d8888.
# 88      d8' `8b 888o  88 88'       88  `8D .8P  Y8. 88    88 888o  88 88  `8D 88'  YP
# 88      88ooo88 88V8o 88 88ooooo   88oooY' 88    88 88    88 88V8o 88 88   88 `8bo.
# 88      88~~~88 88 V8o88 88~~~~~   88~~~b. 88    88 88    88 88 V8o88 88   88   `Y8b.
# 88booo. 88   88 88  V888 88.       88   8D `8b  d8' 88b  d88 88  V888 88  .8D db   8D
# Y88888P YP   YP VP   V8P Y88888P   Y8888P'  `Y88P'  ~Y8888P' VP   V8P Y8888D' `8888Y'


leftDefOrigin = queryForPosition("top left defense bound")
leftDefOrigin2 = queryForPosition("bottom left defense bound")

rightDefOrigin = queryForPosition("top right defense bound")
rightDefOrigin2 = queryForPosition("bottom right defense bound")

leftAttOrigin = queryForPosition("top left attack bound")
leftAttOrigin2 = queryForPosition("bottom left attack bound")

rightAttOrigin = queryForPosition("top right attack bound")
rightAttOrigin2 = queryForPosition("bottom right attack bound")


#    d88b .d8888.  .d88b.  d8b   db   d8888b.  .d8b.  d8888b. .d8888. d88888b
#    `8P' 88'  YP .8P  Y8. 888o  88   88  `8D d8' `8b 88  `8D 88'  YP 88'
#     88  `8bo.   88    88 88V8o 88   88oodD' 88ooo88 88oobY' `8bo.   88ooooo
#     88    `Y8b. 88    88 88 V8o88   88~~~   88~~~88 88`8b     `Y8b. 88~~~~~
# db. 88  db   8D `8b  d8' 88  V888   88      88   88 88 `88. db   8D 88.
# Y8888P  `8888Y'  `Y88P'  VP   V8P   88      YP   YP 88   YD `8888Y' Y88888P


jsonContents = {
    # screen origin point
    "screenOrigin": (screenOrigin[0], screenOrigin[1]),
    "screenBotRight": (screenBotRight[0], screenBotRight[1]),
    # center of card elixer price text
    "elixerTextCoords": (elixerTextCenter[0], elixerTextCenter[1]),
    "card1textCoords": (card1TextCenter[0], card1TextCenter[1]),
    "card2textCoords": (card2TextCenter[0], card2TextCenter[1]),
    "card3textCoords": (card3TextCenter[0], card3TextCenter[1]),
    "card4textCoords": (card4TextCenter[0], card4TextCenter[1]),
    # card click points on screen
    "card1position": (card1position[0], card1position[1]),
    "card2position": (card2position[0], card2position[1]),
    "card3position": (card3position[0], card3position[1]),
    "card4position": (card4position[0], card4position[1]),
    # emotes
    "emoteMenuCoords": (emoteMenu[0], emoteMenu[1]),
    "emoteCoords": (favoriteEmote[0], favoriteEmote[1]),
    # observation bounds for lanes
    "leftDefOrigin": (leftDefOrigin[0], leftDefOrigin[1]),
    "leftDefOrigin2": (leftDefOrigin2[0], leftDefOrigin2[1]),
    "rightDefOrigin": (rightDefOrigin[0], rightDefOrigin[1]),
    "rightDefOrigin2": (rightDefOrigin2[0], rightDefOrigin2[1]),
    "leftAttOrigin": (leftAttOrigin[0], leftAttOrigin[1]),
    "leftAttOrigin2": (leftAttOrigin2[0], leftAttOrigin2[1]),
    "rightAttOrigin": (rightAttOrigin[0], rightAttOrigin[1]),
    "rightAttOrigin2": (rightAttOrigin2[0], rightAttOrigin2[1]),
}

# if debug print the object and then the dumped json
if debug:
    print(jsonContents)
    print(json.dumps(jsonContents))

# dump the object into a json
with open("screenPoints.json", "w") as outfile:
    json.dump(jsonContents, outfile)

# end card
printHeaderClear()
print("You have successfully configured the screen points!")
if tts:
    engine.say("complete")
    engine.runAndWait()
