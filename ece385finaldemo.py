import time
import mss
import numpy
import pytesseract
import re
import win32gui, win32con
import os
import jtag_uart

def cleanchars(text):
    print(text)#print the badly read text, next do filtering
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
    return ext#return the filtered text

def takenums(text):
    p=re.compile(r"[+,\-]\d\.\d\d\d")#take stuff in signed decimal format
    v=p.findall(text)
    return v

def bitreturn(num): #return a bit code for the inputs
    if (num==0):
        return str("00")
    elif (num==1):
        return str("01")
    else:
        return str("10")

def write(ju, writearray): #write a bit array through jtag to the fpga
    writedata = bytes() #instantiate the state data
    index = 0 #instantiate the index
    while (index < len(writearray)):
        writedata = bytes() #instantiate the byte data
        for i in range(0, 16 * 2**10): #big number of bits for if you are writing literally everything to memory on FPGA
            writedata += bytes([writearray[index]])  #write the bits in the index
            index += 1 #index up
            if (index == len(writearray)):#end if the index is done
                break
        ju.write(writedata)#write the data through jtag uart

def keyreturn(text): #takes in a bit combination, returns an ascii from a keycode
    keydic={"0000":"s","0100":"d","1000":"a","0001":"w","0101":"e","1001":"q","0010":"x","0110":"c","1010":"z"}
    print(keydic[text]) #for debugging
    return keydic[text] #returns keycode
    
def direction(lis):#takes in numbers from accelerometer from gravity, finds direction to move
    direction=[]
    print(lis)
    try: #to test for index errors
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
        x=str(bitreturn(direction[0])+bitreturn(direction[1]))#list of bits combined into a string
        return keyreturn(x)
    except:
        return("bad read")

def minimize():
        Minimize = win32gui.GetForegroundWindow()#grabs window in foreground
        win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)#minimizes it

def fullscreenselect(handle): #select a window, handle being the encoded name for a window
    minimize() #runs minimize function
    try:
        win32gui.ShowWindow(handle, win32con.SW_MAXIMIZE) #mazimize needed window
    except:
        1
    try:
        win32gui.SetForegroundWindow(handle) #try to set it as top level
    except:
        try:
            win32gui.BringWindowToTop(handle) #if it fails, try it again but in two parts
            win32gui.SetForegroundWindow(handle)
        except:
            print(handle) #if it fails again, print it
    return handle #return the handle you just used

handle1=win32gui.FindWindow(0, 'DSU Controller Test')#set handle for first instance
handle2=win32gui.FindWindow(0, 'lol') #set handle for second instance

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #path for tesseract
custom="c- tessedit_char_whitelist= 0123456789-+" #custom configs
mon = {'top': 313, 'left': 58, 'width': 192, 'height': 18} #location on screen of accelerometer data

time.sleep(5)#give 5 seconds after running to initialize everything, this is an artifact from testing

def main(): 
    ju = jtag_uart.intel_jtag_uart(instance_nr=0) #grab first jtag connection instance
    with mss.mss() as sct: #definining taking a screenshot as sct
        while True: #infinite loop
            fullscreenselect(handle1)#select window one then sleep for timing reasons
            time.sleep(0.1)#could be shorter, I put this time so that I could give the threads and ram on my computer a break
            im = numpy.asarray(sct.grab(mon))#take first screenshot

            text = pytesseract.image_to_string(im, lang="eng", config=custom)#convert image to text
            fullscreenselect(handle2)# do it again
            time.sleep(0.1) #could be shorter, I put this time so that I could give the threads and ram on my computer a break
            im1 = numpy.asarray(sct.grab(mon)) #take second screenshot
            text1 = pytesseract.image_to_string(im1, lang="eng", config=custom)#convert image to text

            a=[ord(c) for c in ((direction(takenums(cleanchars(text))))+(direction(takenums(cleanchars(text1)))))]
            #okay this has a lot going on, first, filter characters for both and take their 
            # numbers for X and Y directions turn the directions into a character put the keycodes
            # into a tuple, for each character in the tuple, put the ascii code into a string called a

            if (a != [98, 97, 100, 32, 114, 101, 97, 100, 98, 97, 100, 32, 114, 101, 97, 100]): #if not a bad read
                write(ju, a) #send it to the fpga
                print(text)#artifact of debugging
                print(text1)#artifact of debugging

            else:
                print(a) #artifact of debugging
                print("bad read") #tell me what is wrong

            for i in a:
                    print(f"{i:02x} ", end="") #print the ascii codes
            print("")#newline for aesthetic
            
if (__name__ == "__main__"): #runnit
    main() #runnitalllllll
    print("success") #artifact of debugging
