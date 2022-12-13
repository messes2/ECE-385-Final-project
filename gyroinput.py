# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:46:23 2022

@author: matte
"""
import time
import cv2
import mss
import numpy
import pytesseract
import re
import win32gui, win32con
from pynput import keyboard
def cleanchars(text):
    ext=text.replace('8.', '0.')
    ext=ext.replace('@','0')
    ext=ext.replace('2.','0.')
    ext=ext.replace("20.","0.")
    ext=ext.replace('40', '+0')
    ext=ext.replace('41.','+1.')
    ext=ext.replace('%','00')
    ext=ext.replace('-.','-0.')
    ext=ext.replace('+.','+0.')
    ext=ext.replace('4.','+0.')
    ext=ext.replace('. ', '.')
    return ext
def takenums(text):
    p=re.compile(r"[+,\-]\d\.\d\d\d")
    return p.findall(text)
def bitreturn(num):
    if (num==0):
        return str("00")
    elif (num==1):
        return str("01")
    else:
        return str("10")
def keyreturn(text):
    keydic={"0000":"s","0100":"d","1000":"a","0001":"w","0101":"e","1001":"q","0010":"x","0110":"c","1010":"z"}
    return keydic[text]
def direction(lis):#takes in numbers from accelerometer from gravity, finds direction to move
    direction=[]
    try:
        lisnew=[float(lis[0]), float(lis[1])]
        if (lisnew[0]<-0.3):
            direction.append(2)
        elif (lisnew[0]>0.3):
            direction.append(1)
        else:
            direction.append(0)
        if (lisnew[1]<-0.3):
                direction.append(2)
        elif (lisnew[1]>0.3):
                direction.append(1)
        else:
                direction.append(0)
        x=str(bitreturn(direction[0])+bitreturn(direction[1]))
        return keyreturn(x)
    except:
        return("bad read")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
mon = {'top': 313, 'left': 0, 'width': 200, 'height': 180}
handle1=win32gui.FindWindow(0, 'DSU Controller Test')
handle2=win32gui.FindWindow(0, 'DSU Controller Test2')
def fullscreenselect(handle):
    win32gui.SetForegroundWindow(handle)
    win32gui.ShowWindow(handle, win32con.SW_MAXIMIZE)
with mss.mss() as sct:
    while True:
        fullscreenselect(handle2)
        im = numpy.asarray(sct.grab(mon))
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(im)
        x=(direction(takenums(cleanchars(text))))
        time.sleep(0.001)
        fullscreenselect(handle2)
        im = numpy.asarray(sct.grab(mon))
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(im)
        y=(direction(takenums(cleanchars(text))))

        print(y)

        # two screenshots per second
        time.sleep(0.25)