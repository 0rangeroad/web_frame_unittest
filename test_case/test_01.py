from time import sleep

import pyautogui

last_pos = pyautogui.position()
try:
    while True:
        new_pos = pyautogui.position()
        if new_pos == (0, 0):
            print("定位完成")
            break
        if new_pos != last_pos:
            sleep(1)
            last_pos = new_pos
    print(last_pos)
except KeyboardInterrupt:
    print('结束')
