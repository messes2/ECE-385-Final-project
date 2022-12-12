import os
import subprocess
import time
import win32gui

current_dir =r'C:\Users\matte\Downloads\PadTest_1011'
subprocess.Popen(os.path.join(current_dir,"PadTest.exe"))
time.sleep(1)
handle0=win32gui.FindWindow(0, 'DSU Controller Test')
win32gui.SetWindowText(handle0, 'lol')
time.sleep(1)
current_dir =r'C:\Users\matte\Downloads\PadTest_1011'
subprocess.Popen(os.path.join(current_dir,"PadTest.exe"))