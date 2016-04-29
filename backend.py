"""
backflip
An Unsplash-based desktop background changer.
by David Teresi | 2016

backend.py
Controls all the backend stuff such as getting the pictures,
setting them as the background, etc.
"""

import urllib2
import os
import ctypes
import setBG

THEMES = ("buildings", "food", "nature", "technology", "people")
SETTINGS = ("daily", "weekly", "random")
SPI_SETDESKTOPWALLPAPER = 20


def getImgUrl(screenSize, theme=None, setting="daily"):
    "Uses Unsplash API to find a random image based on specified settings"
    if theme:
        assert theme in THEMES
    assert setting in SETTINGS
    assert len(screenSize) == 2

    url = "https://source.unsplash.com"
    if theme:
        url += "/category/"
        url += theme

#   url += "/" + setting

    url += "/%ix%i" % screenSize

    imgUrlObj = urllib2.urlopen(url)
    imgUrl = imgUrlObj.geturl()

    print url
    print imgUrl

    return imgUrl


def getImg(url):
    "Download image from specified URL and save to img/background.jpg"
    imgData = urllib2.urlopen(url)

    os.chdir("./img")

    with open("background.jpg", 'wb') as imgFile:
        imgFile.write(imgData.read())


def setBackground():
    "Set desktop background to file at img/background.jpg. (Windows/Mac (untested) only)"
    cwd = os.getcwd()
    image = os.path.join(cwd, "background.jpg")
    setBG.setBG(image)
