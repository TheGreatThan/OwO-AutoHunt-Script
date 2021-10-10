//you can change what ever you want in the [auto.write('your commands here')]
//do not change the auto.write('owoh') or it won't work!
//dont paste the ('//')
//u can change the time in the n, s, x and d its just generate a random numbers in randrange 0 to what ever u want i mean if u input it 50 it will
//generate a number around 0 to 50!
//thank for using my script! hope u like it!

import pyautogui as auto
import time
import random
import datetime

count = 1

time.sleep(9)
while True:
    n = random.randrange(12)
    s = random.randrange(60)
    x = random.randrange(2)
    d = random.randrange(10)
    auto.write('owoh')
    auto.press('enter')
    time.sleep(20)
    if n == 1:
        if x == 1:
            auto.write('owo cf 10 heads')
            auto.press('enter')
        elif x == 0:
            auto.write('owo cf 10 tails')
            auto.press('enter')
    elif n == 2:
        auto.write('owo s ' + '5')
        auto.press('enter')
    elif n == 3:
        auto.write('owo s ' + '15')
        auto.press('enter')
    elif n == 4:
        if x == 1:
            auto.write('owo cf 100 heads')
            auto.press('enter')
        elif x == 0:
            auto.write('owo cf 100 tails')
            auto.press('enter')
    elif n == 5:
        auto.write('owo s ' + '30')
        auto.press('enter')
    elif n == 6:
        auto.write('owo s ' + '12')
        auto.press('enter')
    elif n == 7:
        if x == 1:
            auto.write('owo cf 8 heads')
            auto.press('enter')
        elif x == 0:
            auto.write('owo cf 8 tails')
            auto.press('enter')
    elif n == 8:
        auto.write('owo s ' + '2')
        auto.press('enter')
    elif n == 9:
        auto.write('owo s ' + '1')
        auto.press('enter')
    elif n == 10:
        if x == 1:
            auto.write('owo cf 50 heads')
            auto.press('enter')
        elif x == 0:
            auto.write('owo cf 50 tails')
            auto.press('enter')
    elif n == 0:
        if x == 1:
            auto.write('owo sell c')
            auto.press('enter')
            time.sleep(d)
            auto.write('owo sell r')
            auto.press('enter')
            time.sleep(d)
            auto.write('owo sell u')
            auto.press('enter')
            time.sleep(d)
            auto.write('owo sell e')
            auto.press('enter')
            time.sleep(d)
            auto.write('owo sell l')
            auto.press('enter')
            time.sleep(d)
            auto.write('owo sell g')
            auto.press('enter')
            time.sleep(d)
            auto.write('owo sell m')
            auto.press('enter')
            time.sleep(d)
        elif x == 0:
            auto.write('owo sacrifice c')
            auto.press('enter')
            time.sleep(d)
            auto.write('owo sacrifice r')
            auto.press('enter')
            time.sleep(d)
            auto.write('owo sacrifice u')
            auto.press('enter')
            time.sleep(d)
            auto.write('owo sacrifice e')
            auto.press('enter')
            time.sleep(d)

    elif n == 11:
        auto.write('owob')
        auto.press('enter')
    print(count)
    count = count + 1
    datetime.datetime.now()
    datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
    print(datetime.datetime.now())
    time.sleep(s)
