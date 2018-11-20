#By Iverson
#This app is to capature screenshot after press any keys. Original implemented to use for auto uploading PowerBI dashboard screenshot

import time
import pyautogui
from PIL import ImageGrab

def keyStroke(key, interval):
    pyautogui.press(key)
    time.sleep(interval)

def screenCapature(id, area, path):
    sc = ImageGrab.grab(area)
    sc.save(path + "z" + str(id) + ".png")

def readParm(file):
    configfile = open(file, mode='r')
    parmlist = {}
    for parm in configfile.readlines():
        rawparmlist = str.split(parm, "=")
        parmlist[rawparmlist[0].strip()] = rawparmlist[1].strip()   #remove empty space
    return parmlist

def main():
    parmlist = readParm('config.txt')
    key = parmlist ['key']
    interval = parmlist['interval']
    area = parmlist['area']
    outputpath = parmlist['outputpath']
    count = parmlist['count']
    while True:
        for i in range (1,int(count)+1):
            keyStroke(key, int(interval))
            screenCapature(i, tuple(eval(area)), outputpath)

if __name__ == '__main__':
    main()