#This code automates Google Drive backup.

import pyautogui as rpa
import time

rpa.alert ("The automation is executing. Please don't use the PC".)

rpa.PAUSE = 0.5

rpa.press('winleft')
rpa.write('chrome')
rpa.press('enter')
time.sleep(1)
rpa.write("https://drive.google.com/drive/my-drive")


rpa.hotkey('winleft', 'd')

rpa.moveTo(3704,98) # depends on each monitor resolution
rpa.mouseDown()
rpa.moveTo(2318,1413)
rpa.hotkey('alt', 'tab')
time.sleep(1)
rpa.mouseUp()

time.sleep(5)

rpa.alert ("The automation is finished :)")