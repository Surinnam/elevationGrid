#!/usr/bin/env python3
#pylint: disable-all

"""
Handles all types of request to the elevation API
"""

from urllib.request import urlopen
import simplejson as json
from coordinate import Coordinate

API_KEY = ""

class Handler:
    def __init__(self):
        self.cache = {}
        self.baseURL = "https://maps.googleapis.com/maps/api/elevation/json?"

    def getElevation(self, target):
        """ 
        Gets the elevation of the target represented by a Coordinate object
        """
        requestURL = self.baseURL+"locations={},{}&key={}".format(target.latitude, target.longitude, API_KEY)
        response = urlopen(requestURL)
        jsonResponse = json.loads(response.read());
        print(jsonResponse)
    
