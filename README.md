# ClashRoyaleAI
[![wakatime](https://wakatime.com/badge/github/Yoyolick/ClashRoyaleAI.svg)](https://wakatime.com/badge/github/Yoyolick/ClashRoyaleAI)

A python program created to play clash royale and (hopefully) win.

# Dependancies
This program is intended to be run on top of the [Blue Stacks](https://www.bluestacks.com/) emulator running clash royale. 

## External Libraries Used:
 - cv2
 - keyboard
 - numpy
 - pyautogui
 - pytesseract
 - win32gui
 - PIL
# Usage
## Setup:
1. Pip install all the dependancies listed above.
2. Replace the path in **tesseractPath.txt** with your own path to your tesseract install.
3. Install bluestacks emulator as well as clash royale inside the emulator.
4. Launch clash royale and get into a training arena match.
5. Run **configure.py** and make sure you are tabbed into the terminal session:
   - Respond to prompts in command line (opt in to verbose and tts which will read out the prompts to you)
   - Hover your mouse over the area on the screen it is asking for and click the enter key.
   - This will generate a **screenPoints.json** file, verify it looks correct
6. You are done with the setup!

## Running:
1. Get into a clash royale game
2. Run **main.py**! Its that easy!

# How It Works
## Observation:
The program will observe your playfield in 5 spots:
 - Your current elixer
 - Your left defense side
 - Your left attack side
 - Your right defense side
 - Your right Attack side

Using the data from these locations it will decide the best course of action in terms of troop attack and defense responses.

The model for the AI decision making is as follows:

![Flowchart (1)](https://user-images.githubusercontent.com/43967290/117589182-1672d580-b0f6-11eb-8b30-dbdda4e958d8.png)


**Clash Royale AI: Ryan Zmuda 2021**
