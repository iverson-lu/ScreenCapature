import time
import pyautogui
from PIL import ImageGrab

def keyStroke(key, interval):
    pyautogui.press(key)
    time.sleep(interval)

def screenCapature(id, area, path):
    ic = ImageGrab.grab(area)
    ic.save(path + "z" + str(id) + ".png")

def readParm(file):
    config = open(file, mode='r')
    parmlist = {}
    for parm in config.readlines():
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