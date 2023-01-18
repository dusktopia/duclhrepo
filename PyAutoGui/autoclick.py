import pyautogui as pag
import time

# pos = pag.position()
# print(pos)
# for i in range(5):
#     pag.click(pos)
#     time.sleep(1)

time.sleep(5)
step1 = 'UnikeyIcon.png'
loc = pag.locateOnScreen(step1)
pag.doubleClick(loc)
time.sleep(2)

step2 = 'MaximizeButton.png'
loc = pag.locateOnScreen(step2)
pag.click(loc)
time.sleep(2)

step3 = 'CloseButton.png'
loc = pag.locateOnScreen(step3)
pag.click(loc)
time.sleep(2)
