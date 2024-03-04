import random 
import pyautogui as pg 
import time

words=('Msg 1', ' Msg 2', u'\U0001f600')
time.sleep(1)
for i in range(10):
    a=random.choice(words)
    pg.write(a)
    pg.press('enter')
    pg.press('enter')
