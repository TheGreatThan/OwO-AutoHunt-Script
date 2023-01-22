import pyautogui as auto
import time
import random
import datetime

count = 0
reset = 1

time.sleep(9)
while True:
    if count == 80:
        if reset == 1:
            count = 0
            auto.write('Paused for 10 mins')
            auto.write(' The Second pause gonna take 30 minutes')
            reset = reset + 1
            auto.press('enter')
            auto.write('Count Reseted To 1.')
            auto.press('enter')
            time.sleep(600)
        elif reset == 2:
            auto.write('Paused for 30 mins')
            auto.press('enter')
            auto.write('Count Reseted To 1.')
            count = 0
            reset = 1
            auto.press('enter')
            time.sleep(1800)

    n = random.randrange(8)
    s = random.randrange(30)
    x = random.randrange(2)
    d = random.randrange(10)
    a = random.randrange(3)
    num = random.randrange(1000)

    converted_num = "% s" % num

    if a == 0:
        auto.write('owo h')
    elif a == 1:
        auto.write('owoh')
    elif a == 2:
        auto.write('owo hunt')
    auto.press('enter')

    time.sleep(20)

    if n == 1:
        if x == 1:
            auto.write('owo ')
            time.sleep(0.5)
            auto.write('cf ')
            time.sleep(0.5)
            auto.write('10 ')
            time.sleep(0.5)
            auto.write('heads')
            auto.press('enter')
        elif x == 0:
            auto.write('owo ')
            time.sleep(0.5)
            auto.write('cf ')
            time.sleep(0.5)
            auto.write('10 ')
            time.sleep(0.5)
            auto.write('tails')
            auto.press('enter')
    elif n == 2:
        auto.write('owo s ')
        auto.write(converted_num)
        time.sleep(0.25)
        auto.press('enter')
    elif n == 3:
        auto.write('owo s ')
        auto.write(converted_num)
        time.sleep(0.35)
        auto.press('enter')
    elif n == 4:
        if x == 1:
            auto.write('owo ')
            time.sleep(0.5)
            auto.write('cf ')
            time.sleep(0.5)
            auto.write(converted_num)
            time.sleep(0.5)
            auto.write(' heads')
            auto.press('enter')
        elif x == 0:
            auto.write('owo ')
            auto.sleep(0.15)
            auto.write('cf ')
            auto.sleep(0.25)
            auto.write(converted_num)
            auto.write(' tails')
            time.sleep(0.3)
            auto.press('enter')
    elif n == 5:
        auto.write('owo s ')
        time.sleep(0.25)
        auto.write(converted_num)
        auto.press('enter')
    elif n == 6:
        auto.write('owo s ')
        time.sleep(0.25)
        auto.write(converted_num)
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
            auto.write('sell all')
            time.sleep(d)
            auto.press('enter')

    elif n == 7:
        if a == 0:
            auto.write('owob')
        elif a == 1:
            auto.write('owo b')
        elif a == 2:
            auto.write('owo battle')
    auto.press('enter')
    count = count + 1
    tong = 80
    hieu = tong - count
    converted_hieu = "% s" % hieu
    converted_count = "% s" % count
    print(count)
    datetime.datetime.now()
    datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
    print(datetime.datetime.now())
    print(s)
    auto.write('This is the ')
    auto.write(converted_count)
    auto.write(' times and will be halted after ')
    auto.write(converted_hieu)
    auto.write(' more times')
    auto.press('enter')
    time.sleep(s)