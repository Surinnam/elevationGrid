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


def hashCoordinate(number):
    """
    Hashes a number to a string for cache storage purposes
    https://developers.google.com/maps/documentation/utilities/polylinealgorithm?hl=fr
    """
    if (number >= 0):
       val=int(number*10**5)<<1
    else:
        val=~(int(number*10**5)<<1)
    bit_groups = []
    while (val != 0):
        bit_groups.append(val&31)
        val = val >> 5
    for i in range(len(bit_groups)-1):
        bit_groups[i] |= 32
    return ''.join([chr(group+63) for group in bit_groups])
    
