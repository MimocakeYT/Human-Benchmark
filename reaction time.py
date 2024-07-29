import pyautogui
from time import sleep

sleep(4)
for i in range(5):
    pyautogui.click(1100, 293, button="left")
    while True:
        if pyautogui.pixelMatchesColor(1100, 293, (75, 219, 106)):
            pyautogui.click(1100, 293, button="left")
            break
    sleep(0.5)