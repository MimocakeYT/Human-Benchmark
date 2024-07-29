import pyautogui
from time import sleep

sleep(4)
pyautogui.click(1270, 530)
sleep(1)
while True:
    list = []
    while True:
        im = pyautogui.screenshot(region=(1082, 237, 380, 380))
        f = 0
        tmp = len(list)
        for y in range(3):
            if f:
                break
            for x in range(3):
                if im.getpixel((10 + x*130, 10 + y*130)) == (255, 255, 255):
                    if len(list) == 0 or list[-1] != x + 3*y:
                        list.append(x + 3*y)
                    f = 1
                    break
        if tmp == len(list) and not f:
            break
    for i in list:
        pyautogui.click(1152 + 130*(i%3), 300 + 130*(i // 3))
    sleep(1.05)
