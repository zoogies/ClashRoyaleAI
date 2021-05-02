# TODO this is something that should be included in configure or merged into main

from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import time
import pyautogui
import win32gui
import keyboard
import win32gui, win32com.client


def screenshot(window_title=None):
    if window_title:
        shell = win32com.client.Dispatch("WScript.Shell")  # might work idk
        shell.SendKeys("%")
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


if __name__ == "__main__":
    left = 0
    right = 100
    top = 0
    bottom = 100

    # get a screenshot of the playfield
    im = screenshot("BlueStacks")
    im.save("images/playfield.png")

    while True:
        try:

            # TODO REMOVE left, top, right, bottom
            ix = im.crop(
                (
                    left + int(input("change left: ")),
                    top + int(input("change top: ")),
                    right + int(input("change right: ")),
                    bottom + int(input("change bottom: ")),
                )
            )

            ix.save("images/croptest.png")
            # im.show()

            # emergency abort
            if keyboard.is_pressed("q"):
                print("-> EMERGENCY EXIT")
                exit()
        except:
            print("ERROR - you probably just over extended the image")

        time.sleep(1)