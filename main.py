import pyautogui
import win32gui
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import keyboard
import pytesseract as tess
from datetime import datetime
import re
import time

# defualts
elixerStoreValue = 0

firstCardCost = 0
secondCardCost = 0
thirdCardCost = 0
fourthCardCost = 0

# set playfield screen coordinates
gameOrigin = (2475, 42)
# aboveLeftTower = (125, 608)
# aboveRightTower = (475, 608)
# middleHigh = (310, 608) TODO COMMENTED OUT BECAUSE HAVING EXTRA MULTIPLICATION MIGHT BE COSTLY
aboveLeftTower = (gameOrigin[0] + 125, gameOrigin[1] + 608)
aboveRightTower = (gameOrigin[0] + 475, gameOrigin[1] + 608)
middleHigh = (gameOrigin[0] + 310, gameOrigin[1] + 608)

# set card click coords on screen
firstCardCoords = (gameOrigin[0] + 200, gameOrigin[1] + 988)
secondCardCoords = (gameOrigin[0] + 315, gameOrigin[1] + 988)
thirdCardCoords = (gameOrigin[0] + 425, gameOrigin[1] + 988)
fourthCardCoords = (gameOrigin[0] + 555, gameOrigin[1] + 988)

# tell program we dont know any of our deck cards
usedFC = True
usedSC = True
usedTC = True
usedFTHC = True

# set tesseract path
with open("tesseractPath.txt", "r") as tessPath:
    tess.pytesseract.tesseract_cmd = tessPath.read()


def screenshot(window_title=None):
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
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


def filterImage(img):
    # condensed filtering to grayscale binary image for easier recognition
    img = (
        img.convert("L")
        .filter(ImageFilter.MedianFilter())
        .point(lambda x: 0 if x < 220 else 255)
    )
    return img


# TODO might need to put num filter back idk 4 is fucky  -c tessedit_char_whitelist=1234567890


def tessParse(im):
    # parse our text and
    detectedText = tess.image_to_string(im, config="--psm 13")
    # 4 is commonly mistaken for Q in the clash royale font, correct for this
    if "q" in detectedText:
        detectedText = "4"
    # clean detected text for any letters wrongly recognised TODO remove this if i enable the character whitelsit
    # print("detected text:", detectedText)
    detectedText = re.sub(
        "[^0-9]", "", detectedText
    )  # this is regex! wow im so god damn smart >:) totally didnt copy it from somewhere

    # return detected text corrected for recognition errors
    return detectedText


# TODO REMOVE left, top, right, bottom


def parseStaticValues(
    elixerStoreValue,
    usedFirstCardSinceLastCheck,
    usedSecondCardSinceLastCheck,
    usedThirdCardSinceLastCheck,
    usedFourthCardSinceLastCheck,
    firstCardCost,
    secondCardCost,
    thirdCardCost,
    fourthCardCost,
):

    parseValuesElapsedTime = datetime.now()

    # TODO TEST FILTERING ONE TIME FOR EFFICIENCY

    with Image.open("images/playfield.png") as im:

        # update current elixer store value based off playfield image
        elixerStoreImg = im.crop((170, 1050, 200, 1090))
        elixerStoreImg = filterImage(elixerStoreImg)
        # elixerStoreImg.show()
        # defualt to last known value if we dont know our current
        tmp = tessParse(elixerStoreImg)
        if tmp != "":
            elixerStoreValue = tmp

        print("elixer store value:", elixerStoreValue)

        # only check for card values if we know we have a different card

        if usedFirstCardSinceLastCheck:
            # update first card elixer value
            firstCardPriceImg = im.crop((180, 1030, 210, 1055))
            firstCardPriceImg = filterImage(firstCardPriceImg)
            # firstCardPriceImg.show()
            tmp = tessParse(firstCardPriceImg)
            if tmp != "":
                firstCardCost = tmp

            print("first card price:", firstCardCost)
            usedFirstCardSinceLastCheck = False

        if usedSecondCardSinceLastCheck:
            # update second card elixer value
            secondCardPriceImg = im.crop((300, 1030, 320, 1055))
            secondCardPriceImg = filterImage(secondCardPriceImg)
            # secondCardPriceImg.show()
            tmp = tessParse(secondCardPriceImg)
            if tmp != "":
                secondCardCost = tmp

            print("second card price:", secondCardCost)
            usedSecondCardSinceLastCheck = False

        if usedThirdCardSinceLastCheck:
            # update third card elixer value
            thirdCardPriceImg = im.crop((420, 1030, 440, 1055))
            thirdCardPriceImg = filterImage(thirdCardPriceImg)
            # thirdCardPriceImg.show()
            tmp = tessParse(thirdCardPriceImg)
            if tmp != "":
                thirdCardCost = tmp

            print("third card price:", thirdCardCost)
            usedThirdCardSinceLastCheck = False

        if usedFourthCardSinceLastCheck:
            # update fourth card elixer value
            fourthCardPriceImg = im.crop((530, 1030, 550, 1055))
            fourthCardPriceImg = filterImage(fourthCardPriceImg)
            # fourthCardPriceImg.show()
            tmp = tessParse(fourthCardPriceImg)
            if tmp != "":
                fourthCardCost = tmp

            print("fourth card price:", fourthCardCost)
            usedFourthCardSinceLastCheck = False

    print("elapsed static parse time:", datetime.now() - parseValuesElapsedTime)


# card location possibilities:
# - leftAboveTower
# - rightAboveTower
# - leftPushedTower
# - rightPushedTower
# - defendLeftCastle
# - defendRightCastle
# -

# starting this index from 1 because its possibly faster (yes i know, barely if at all)
def placeCard(location, cardIndex):

    # select the card specified
    # bluestacks needs you to spam to recognise it i guess
    # keyboard.press(str(cardIndex)) TODO add back in keyboard support? bluestacks is fucked

    # click on the card we want to use
    if cardIndex == 1:
        pyautogui.click(firstCardCoords[0], firstCardCoords[1])
    elif cardIndex == 2:
        pyautogui.click(secondCardCoords[0], secondCardCoords[1])
    elif cardIndex == 3:
        pyautogui.click(thirdCardCoords[0], thirdCardCoords[1])
    elif cardIndex == 4:
        pyautogui.click(fourthCardCoords[0], fourthCardCoords[1])

    # place the card in our desired location
    if location == "leftAboveTower":
        pyautogui.click(aboveLeftTower[0], aboveLeftTower[1])
    elif location == "rightAboveTower":
        pyautogui.click(aboveRightTower[0], aboveRightTower[1])
    elif location == "leftPushedTower":
        # TODO
        return
    elif location == "rightPushedTower":
        # TODO
        return
    elif location == "defendLeftCastle":
        # TODO
        return
    elif location == "defendRightCastle":
        # TODO
        return

    # let the program know we need to scan for new value in spot of whichever card we just used
    if cardIndex == 1:
        usedFC = True
    elif cardIndex == 2:
        usedSC = True
    elif cardIndex == 3:
        usedTC = True
    elif cardIndex == 4:
        usedFTHC = True


# BASIC STATEGIES

# pick the cheapest presented card at all times and place it
def placeCheapestCard():
    possibleCards = [
        int(firstCardCost),
        int(secondCardCost),
        int(thirdCardCost),
        int(fourthCardCost),
    ]
    # get index of smallest item in list
    cardNumber = (
        possibleCards.index(min(possibleCards)) + 1
    )  # add one because lists start at 0

    placeCard("leftAboveTower", cardNumber)


if __name__ == "__main__":
    while True:
        # get a screenshot of the playfield

        im = screenshot("BlueStacks")
        im = im.crop((2, 42, 625, 1155))
        # im.show()
        im.save("images/playfield.png")

        # parse playfield for elixer store and our four card prices
        parseStaticValues(
            elixerStoreValue,
            usedFC,
            usedSC,
            usedTC,
            usedFTHC,
            firstCardCost,
            secondCardCost,
            thirdCardCost,
            fourthCardCost,
        )
        time.sleep(1)

        placeCheapestCard()

        # emergency abort
        if keyboard.is_pressed("q"):
            print("-> EMERGENCY EXIT")
            exit()


# pyautogui.click(gameOrigin[0], gameOrigin[1])
# keyboard.press("1")

# mental map:
# - variable screen coords for tower location and place points
# - set screen points to scan for health elixer
# - figure out which card from elixer cost, find single digit numbers for rank of enemy units
# - maybe put filters on image one time and crop from that to make easier? wait maybe not due to differing thresholds
# - refactor code, you copy paste like a bitch and this needs to be optimized
# - TODO next step: isolate red pixels on screen to detect enemies
# TODO how costly is transforming to int?

# WHERE I LEFT OFF
# wrote a very basic attack pattern of spamming left lane
# WHAT YOU SHOULD DO:
# write more attack patterns for fun
# start detecting enemies and countering (detect via clusters or something maybe) red filter over playfield
