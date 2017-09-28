#!/usr/bin/env python3
#pylint: disable-all

"""
Various functions of conversion
"""

from math import floor, pi

def convertToDMS(decimalDeg):
    """
    Converts a Coordinate object to degrees, minutes, seconds
    """
    converted = {}
    converted["degrees"] = floor(abs(decimalDeg))
    converted["minutes"] = (abs(decimalDeg)-converted["degrees"])*60
    converted["seconds"] = round((converted["minutes"]-
                                  floor(converted["minutes"]))*60,3)
    converted["minutes"] = floor(converted["minutes"])
    return converted

def toRadians(decimalDeg):
    """
    Converts degrees to radians
    """
    return decimalDeg*pi/180

def toDegrees(radianAngle):
    """
    Converts radians to degrees
    """
    return 180*radianAngle/pi
