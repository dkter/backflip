import subprocess
import os
import platform
import ctypes

def setBG_Windows(img):
    print img #debugging
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, img , 0)
def setBG_Darwin(img):
    SCRIPT = """
    #!/usr/bin/env bash
    sqlite3 ~/Library/Application\ Support/Dock/desktoppicture.db "update data set value =
    '/Library/Desktop\ Pictures/Yosemite\ 5.jpg'";
    killall Dock;
    """
    subprocess.call(SCRIPT, shell=True)

def setBG(img):
    print img #debugging
    system = platform.system()
    exec "setBG_%s(%r)"%(system, img)
