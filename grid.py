#!/usr/bin/env python3
#pylint: disable-all

"""
Retrieve altitude on a grid
"""

import urllib
import simplejson
from math import floor 

def convertToDMS(decimalDeg):
    """
    Converts a Coordinate object to degrees, minutes, seconds
    """
    converted = {}
    converted["degrees"] = floor(abs(decimalDeg))
    converted["minutes"] = (abs(decimalDeg)-converted["degrees"])*60
    converted["seconds"] = round((converted["minutes"]-floor(converted["minutes"]))*60,3)
    converted["minutes"] = floor(converted["minutes"])
    return converted
    

class Coordinate:
    """
    Reprensentation of GPS coordinates
    """
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def translateToDMS(self):
        latitude = convertToDMS(self.latitude)
        longitude = convertToDMS(self.longitude)
        return latitude, longitude

    def printAsDMS(self):
        latitude, longitude = self.translateToDMS()
        print("Latitude: {}° {}' {}\"".format(latitude["degrees"],
                                                latitude["minutes"],
                                                latitude["seconds"]))
        print("Longitude: {}° {}' {}\"".format(longitude["degrees"],
                                                 longitude["minutes"],
                                                 longitude["seconds"]))
                             
    def __repr__(self):
        return "Latitude: {}\nLongitude: {}".format(self.latitude, self.longitude)



class Grid:
    """
    Class that supports the grid of elevation points
    """
    def __init__(self, start):
        self.start = start
        self.size = size
        self.lines = lines
        self.columns = columns
        self.grid = [[0 for j in range(columns)] for i in range(lines)]
        self.topCorner = None



        

def main():
    """
    Main function
    """
    test_point = Coordinate(42.339057,13.042602)
    print(test_point)
    test_point.printAsDMS()

if __name__ == "__main__":
    main()
    
