import pyautogui
from time import sleep

sleep(4)
pyautogui.click(1270, 530)
pyautogui.moveTo(1000)
while True:
    pyautogui.moveTo(1000, 200)
    sleep(1.2)
    im = pyautogui.screenshot(region=(1078, 234, 387, 387))
    gap_cnt = 0
    gap_pix_cnt = 0
    for i in range(20, 370):
        if im.getpixel((i, 10)) == (43, 135, 209):
            gap_pix_cnt += 1
        if (im.getpixel((i, 10)) == (43, 135, 209)) and (im.getpixel((i-1, 10)) != (43, 135, 209)):
            gap_cnt += 1
    sq_cnt = gap_cnt + 1
    sq_size = round((387 - gap_pix_cnt) / sq_cnt)
    gap_size = gap_pix_cnt // gap_cnt
    sleep(1.1)
    for i in range(sq_cnt):
        for j in range(sq_cnt):
            x = int(1078 + sq_size * (i + 0.5) + gap_size * i)
            y = int(234 + sq_size * (j + 0.5) + gap_size * j)
            if im.getpixel((x - 1078, y - 234)) == (255, 255, 255):
                pyautogui.click(x, y)
    sleep(1)