import win32gui, win32con,time
import time
import os
import subprocess
current_dir =r'C:\Users\matte\Downloads\PadTest_1011'
subprocess.Popen(os.path.join(current_dir,"PadTest.exe"))
#os.system(filename+".exe")
time.sleep(1)
handle0=win32gui.FindWindow(0, 'DSU Controller Test')
win32gui.SetWindowText(handle0, 'lol')
print(win32gui.GetWindowText(handle0))
time.sleep(1)
current_dir =r'C:\Users\matte\Downloads\PadTest_1011'
subprocess.Popen(os.path.join(current_dir,"PadTest.exe"))

#fullscreenselect(handle)
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
#fullscreenselect(661204)

#time.sleep(0.001)
#fullscreenselect(12847014)
#win32gui.SetWindowText(handle1, 'lol')