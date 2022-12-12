import time
#import cv2
import mss
import numpy
import pytesseract
import re
import win32gui, win32con
import os
import subprocess
import jtag_uart

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
def write(ju, writearray):
    writedata = bytes()
    index = 0
    while (index < len(writearray)):
        writedata = bytes()
        for i in range(0, 16 * 2**10):
            writedata += bytes([writearray[index]])
            index += 1
            if (index == len(writearray)):
                break
        ju.write(writedata)
def keyreturn(text):
    keydic={"0000":"s","0100":"d","1000":"a","0001":"w","0101":"e","1001":"q","0010":"x","0110":"c","1010":"z"}
    print(keydic[text])
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
time.sleep(5)
def main(): 
    ju = jtag_uart.intel_jtag_uart(instance_nr=0)
    with mss.mss() as sct:
        while True:
            fullscreenselect(handle1)
            time.sleep(0.1)
            im = numpy.asarray(sct.grab(mon))
            # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(im, lang="eng", config=custom)
            fullscreenselect(handle2)
            time.sleep(0.1)
            im1 = numpy.asarray(sct.grab(mon))
            text1 = pytesseract.image_to_string(im1, lang="eng", config=custom)
            a=[ord(c) for c in ((direction(takenums(cleanchars(text))))+(direction(takenums(cleanchars(text1)))))]
            if (a != [98, 97, 100, 32, 114, 101, 97, 100, 98, 97, 100, 32, 114, 101, 97, 100]):
                write(ju, a)
                print(text)
                print(text1)
            else:
                print(a)
                print("bad read")
            for i in a:
                    print(f"{i:02x} ", end="")
            time.sleep(1)
            print("")
if (__name__ == "__main__"):
    main()
    print("success")