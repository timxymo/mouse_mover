import pyautogui as pag
import random
import time

check = True

while check: 
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    pag.moveTo(x, y, 0.5)
    t_minus_one_loc = pag.position()
    time.sleep(2.5)
    curr_loc = pag.position()
    check = (t_minus_one_loc==curr_loc)
