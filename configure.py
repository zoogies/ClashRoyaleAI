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

"""def screenshot(window_title=None):
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys("%")

            win32gui.SetForegroundWindow(hwnd)
            x, y, x1, y1 = win32gui.GetClientRect(hwnd)
            x, y = win32gui.ClientToScreen(hwnd, (x, y))
            x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
            im = pyautogui.screenshot(region=(x, y, x1, y1))
            return im
        else:
            print("Window not found!")
    else:
        im = pyautogui.screenshot()
        return im
"""


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


"""
# defualts
confirmedRes = False
while not confirmedRes:
    # printHeaderClear()
    print("Now setting up playfield size and position")

    # screen origin
    screenOrigin = queryForPosition("very top left pixel of your clash royale screen")
    screenBotRight = queryForPosition(
        "very bottom right pixel of you clash royale screen"
    )
    print("screen origin", screenOrigin)
    print("screen bot right", screenBotRight)

    # get size of our current bluestacks window
    im = screenshot("BlueStacks")
    bluestacksSize = im.size
    print("bluestacks size", bluestacksSize)
    screenSize = [
        screenBotRight[0] - screenOrigin[0],
        screenBotRight[1] - screenOrigin[1],
    ]
    print("screen size", screenSize)
    # calculate our crop amounts from our given playfield size and window size
    cropTL = [0, bluestacksSize[1] - screenSize[1]]
    cropBR = [screenSize[0], bluestacksSize[1]]
    print("crop tl", cropTL)
    print("crop br", cropBR)
    im.crop(
        (
            cropTL[0],
            cropTL[1],
            cropBR[0],
            cropBR[1],
        )
    )
    print(
        cropTL[0],
        cropTL[1],
        cropBR[0],
        cropBR[1],
    )
    im.show()

    # printHeaderClear()
    if input("Does this look correct? y/n ") == "y":
        confirmedRes = True TODO finish this maybe idk why it dont work
"""

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


# d8888b. db       .d8b.   .o88b. d88888b   d8888b.  .d88b.  d888888b d8b   db d888888b .d8888.
# 88  `8D 88      d8' `8b d8P  Y8 88'       88  `8D .8P  Y8.   `88'   888o  88 `~~88~~' 88'  YP
# 88oodD' 88      88ooo88 8P      88ooooo   88oodD' 88    88    88    88V8o 88    88    `8bo.
# 88~~~   88      88~~~88 8b      88~~~~~   88~~~   88    88    88    88 V8o88    88      `Y8b.
# 88      88booo. 88   88 Y8b  d8 88.       88      `8b  d8'   .88.   88  V888    88    db   8D
# 88      Y88888P YP   YP  `Y88P' Y88888P   88       `Y88P'  Y888888P VP   V8P    YP    `8888Y'


# above left tower
aboveLeftTower = queryForPosition("any place point (on your side) above the left tower")

# above right tower
aboveRightTower = queryForPosition(
    "any place point (on your side) above the right tower"
)

# pushed left side
leftPushedTower = queryForPosition(
    "any place point on the enemy left side that becomes available when the tower is taken"
)

# pushed right side
rightPushedTower = queryForPosition(
    "any place point on the enemy right side that becomes available when the tower is taken"
)

# TODO add more attack points


# d88888b .88b  d88.  .d88b.  d888888b d88888b .d8888.
# 88'     88'YbdP`88 .8P  Y8. `~~88~~' 88'     88'  YP
# 88ooooo 88  88  88 88    88    88    88ooooo `8bo.
# 88~~~~~ 88  88  88 88    88    88    88~~~~~   `Y8b.
# 88.     88  88  88 `8b  d8'    88    88.     db   8D
# Y88888P YP  YP  YP  `Y88P'     YP    Y88888P `8888Y'

emoteMenu = queryForPosition("button to open the emote menu")
favoriteEmote = queryForPosition("emote you want the ai to use")


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
    # unit place points
    "aboveRightTower": (aboveRightTower[0], aboveRightTower[1]),
    "aboveLeftTower": (aboveLeftTower[0], aboveLeftTower[1]),
    "leftPushed": (leftPushedTower[0], leftPushedTower[1]),
    "rightPushed": (rightPushedTower[0], rightPushedTower[1]),
    # emotes
    "emoteMenuCoords": (emoteMenu[0], emoteMenu[1]),
    "emoteCoords": (favoriteEmote[0], favoriteEmote[1]),
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

# add getting reference pic here

# points saved for testing purposes:
# {"screenOrigin": [2678, 44], "screenBotRight": [3439, 1392], "elixerTextCoords": [2900, 1347], "card1textCoords": [2912, 1307], "card2textCoords": [3054, 1307], "card3textCoords": [3197, 1306], "card4textCoords": [3339, 1306], "card1position": [2910, 1208], "card2position": [3053, 1198], "card3position": [3180, 1200], "card4position": [3317, 1204], "aboveRightTower": [3254, 795], "aboveLeftTower": [2851, 774], "leftPushed": [2851, 515], "rightPushed": [3253, 517]}

# TODO maybe screenshot show user and ask if it looks good?
# TODO maybe show more emotes?
