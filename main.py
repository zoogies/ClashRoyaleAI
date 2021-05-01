import pyautogui
import win32gui
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import mouse
import keyboard
import pytesseract as tess

# set playfield screen coordinates
gameOrigin = (2475, 42)
aboveLeftTower = (125, 608)
aboveRightTower = (475, 608)
middleHigh = (310, 608)

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


# TODO REMOVE left, top, right, bottom


def filterImage(img):
    # condensed filtering to grayscale binary image for easier recognition
    img = (
        img.convert("L")
        .filter(ImageFilter.MedianFilter())
        .point(lambda x: 0 if x < 200 else 255)
    )
    return img


def tessParse(im):
    # parse our text and
    detectedText = tess.image_to_string(
        im, config="--psm 13 -c tessedit_char_whitelist=1234567890"
    )
    # 4 is commonly mistaken for Q in the clash royale font, correct for this
    if "q" in detectedText:
        detectedText = 4

    # return detected text corrected for recognition errors
    return detectedText


def parseStaticValues():

    # TODO TEST FILTERING ONE TIME FOR EFFICIENCY

    with Image.open("images/playfield.png") as im:
        # update current elixer store value based off playfield image
        elixerStoreImg = im.crop((170, 1050, 200, 1090))
        elixerStoreImg = filterImage(elixerStoreImg)
        elixerStoreImg.show()
        elixerStoreValue = tessParse(elixerStoreImg)
        print("elixer store value:", elixerStoreValue)

        # update first card elixer value
        firstCardPriceImg = im.crop((180, 1030, 210, 1055))
        firstCardPriceImg = filterImage(firstCardPriceImg)
        firstCardPriceImg.show()
        firstCardCost = tessParse(firstCardPriceImg)
        print("first card price:", firstCardCost)

        # update second card elixer value
        secondCardPriceImg = im.crop((300, 1030, 320, 1055))
        secondCardPriceImg = filterImage(secondCardPriceImg)
        secondCardPriceImg.show()
        secondCardCost = tessParse(secondCardPriceImg)
        print("second card price:", secondCardCost)

        # update third card elixer value
        thirdCardPriceImg = im.crop((420, 1030, 440, 1055))
        thirdCardPriceImg = filterImage(thirdCardPriceImg)
        thirdCardPriceImg.show()
        thirdCardCost = tessParse(thirdCardPriceImg)
        print(thirdCardCost)


# 2600 650 left
# 2950 650 right
# 2785 650 mid
"""
im = screenshot("BlueStacks")

if im:
    im = im.crop((2, 42, 625, 1155))
    im.show()
    im.save("images/playfield.png")
"""
parseStaticValues()
# 2475 42

# mouse.move(gameOrigin[0], gameOrigin[1])
# keyboard.press("1")

# mental map:
# - variable screen coords for tower location and place points
# - set screen points to scan for health elixer
# - figure out which card from elixer cost, find single digit numbers for rank of enemy units
# - maybe put filters on image one time and crop from that to make easier? wait maybe not due to differing thresholds
# - refactor code, you copy paste like a bitch and this needs to be optimized