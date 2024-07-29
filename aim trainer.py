import pyautogui
from time import sleep

sleep(4)
pyautogui.click(1271, 393, button="left")
for i in range(30):
    im = pyautogui.screenshot(region=(845, 180, 900, 480))
    for x in range(845, 1745, 70):
        for y in range(180, 660, 70):
            if im.getpixel((x - 845, y - 180)) != (43, 135, 209):
                pyautogui.click(x, y, button="left")
                break