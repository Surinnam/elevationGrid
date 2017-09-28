#!/usr/bin/env python3
#pylint: disable-all

"""
Coordinate class
"""

from math import floor, asin, sin, cos, atan2, pi
from conversion import convertToDMS, toRadians, toDegrees

# Constants
EARTH_RADIUS = 6378137


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

    def travel(self, bearing, distance):
        """
        Returns a new coordinate object distant et angled from self.
        Bearing is the angle in radians between the destination and a ray pointing to the magnetic north starting from self.
        Distance must be given in meters
        """
        delta = distance/EARTH_RADIUS
        converted_latitude = toRadians(self.latitude)
        converted_longitude = toRadians(self.longitude)
        new_lat = asin(sin(converted_latitude)*cos(delta)+
                       cos(converted_latitude)*sin(delta)*
                       cos(bearing))
        new_long = converted_longitude + atan2(sin(bearing)*sin(delta)*cos(converted_latitude), cos(delta)-sin(converted_latitude)*sin(new_lat))
        return Coordinate(round(toDegrees(new_lat),6), round(toDegrees(new_long),6))
                            
    def __repr__(self):
        return "Latitude: {}\nLongitude: {}".format(self.latitude, self.longitude)
