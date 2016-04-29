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


def setBG_Windows(img):
    "Set desktop background - Windows edition."
    print img  # debugging
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, img, 0)


def setBG_Darwin(img):
    "Set desktop background - Mac edition."
    SCRIPT = """
    #!/usr/bin/env bash
    sqlite3 ~/Library/Application\ Support/Dock/desktoppicture.db "update data set value =
    '%s'";
    killall Dock;
    """ % (img)
    subprocess.call(SCRIPT, shell=True)


def setBG(img):
    "Cross-platformization of the desktop background setting."
    print img  # debugging
    system = platform.system()
    exec "setBG_%s(%r)" % (system, img)
