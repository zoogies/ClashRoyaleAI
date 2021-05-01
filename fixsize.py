import time

import pyautogui
import win32gui


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


if __name__ == "__main__":
    while True:
        time.sleep(1)
        im = screenshot("BlueStacks")
        im = im.crop((2, 42, 625, 1155))
        # im.show()
        im.save("images/playfield.png")