"""
backflip
An Unsplash-based desktop background changer.
by David Teresi | 2016

setBG.py
Sets the desktop background. Has functions for each operating system
"""
import subprocess
import os
import platform
import ctypes
import sys


def setBGWin(img):
    "Set desktop background - Windows edition."
    print img  # debugging
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, img, 0)


def setBGMac(img):
    "Set desktop background - Mac edition."
    SCRIPT = """
    #!/usr/bin/env bash
    sqlite3 ~/Library/Application\ Support/Dock/desktoppicture.db "update data set value =
    '%s'";
    killall Dock;
    """ % (img)
    subprocess.call(SCRIPT, shell=True)



## Desktop Environments ##

def setBGLinuxGnome(img):
    command = "gsettings set org.gnome.desktop.background picture-uri file://%s" % (img)
    print command
    subprocess.call(command, shell=True)



dispatch_linuxde = {
    "gnome": setBGLinuxGnome,
    "budgie-desktop": setBGLinuxGnome,   # gnome method also works for budgie
}

def setBGLinux(img):
    de = os.environ.get('DESKTOP_SESSION')
    if de in dispatch_linuxde:
        dispatch_linuxde[de](img)



dispatch = {  # Dispatch dictionary which stores background-setting functions.
    "Windows": setBGWin,
    "Darwin": setBGMac,
    "Linux": setBGLinux,
}


def setBG(img):
    "Cross-platformization of the desktop background setting."
    print img  # debugging
    system = platform.system()
    if system in dispatch:
        dispatch[system](img)
    else:
        print "Your operating system is not supported."
        sys.exit(0)
