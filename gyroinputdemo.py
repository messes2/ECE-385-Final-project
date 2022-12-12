# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:46:23 2022

@author: matte
"""
import time
#import cv2
import mss
import numpy
import pytesseract
import re
import pysine
import win32gui, win32con
import os
import subprocess


def cleanchars(text):
    print(text)
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
    v=p.findall(text)
    return v
def bitreturn(num):
    if (num==0):
        return str("00")
    elif (num==1):
        return str("01")
    else:
        return str("10")
def playnote(note):
    notedict= {"+x":494 ,"+y":440.3, "-x":587, "-y":523, "+x+y":698.75 ,"-x-y":880.25, "-x+y":659.40, "+x-y":783.24 }
    try:  
         pysine.sine(frequency=notedict[note], duration=0.5)
    except:
            time.sleep(0.5)
def keyreturn(text):
    keydic={"0000":"center","0100":"+x","1000":"-x","0001":"+y","0101":"+x+y","1001":"-x+y","0010":"-y","0110":"+x-y","1010":"-x-y"}
    return keydic[text]
def direction(lis):#takes in numbers from accelerometer from gravity, finds direction to move
    direction=[]
    print(lis)
    try:
        lisnew=[float(lis[0]), float(lis[1])]
        if (lisnew[0]<-0.4):
            direction.append(2)
        elif (lisnew[0]>0.4):
            direction.append(1)
        else:
            direction.append(0)
        if (lisnew[1]<-0.4):
                direction.append(2)
        elif (lisnew[1]>0.4):
                direction.append(1)
        else:
                direction.append(0)
        x=str(bitreturn(direction[0])+bitreturn(direction[1]))
        return keyreturn(x)
    except:
        return("bad read")
def minimize():
        Minimize = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

def fullscreenselect(handle):
    Minimize = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
    try:
        win32gui.ShowWindow(handle, win32con.SW_MAXIMIZE)
    except:
        1
    try:
        win32gui.SetForegroundWindow(handle)
    except:
        try:
            win32gui.BringWindowToTop(handle)
            win32gui.SetForegroundWindow(handle)
            print(handle)
        except:
            print(handle)
    return handle
handle1=win32gui.FindWindow(0, 'DSU Controller Test')
handle2=win32gui.FindWindow(0, 'lol')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
custom="c- tessedit_char_whitelist= 0123456789-+"
mon = {'top': 313, 'left': 58, 'width': 192, 'height': 18}
with mss.mss() as sct:
    while True:
        fullscreenselect(handle1)
        time.sleep(0.05)
        im = numpy.asarray(sct.grab(mon))
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(im, lang="eng", config=custom)
        text=cleanchars(text)
        y=(direction(takenums(text)))
        print(y)
        playnote(y)
        fullscreenselect(handle2)
        time.sleep(0.05)
        im = numpy.asarray(sct.grab(mon))
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(im, lang="eng", config=custom)
        text=cleanchars(text)
        y=(direction(takenums(text)))
        print(y)
        playnote(y)
