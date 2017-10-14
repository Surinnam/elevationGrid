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
        jsonResponse = json.loads(response.read())
        return jsonResponse["results"][-1]["elevation"]

    def getMultipleElevations(self, targets):
        """
        This method is equivalent to calling getElevation several times.
        It will return all elevation for the Coordinate object in targets
        """
        if (targets != []):
            requestURL = self.baseURL+"locations="
            for target in targets:
                requestURL += "{},{}|".format(target.latitude,
                                              target.longitude)
            requestURL = requestURL[:-1]
            response = urlopen(requestURL)
            jsonResponse = json.loads(response.read())
            #print(jsonResponse)
            return [target["elevation"] for target in jsonResponse["results"]]
        else:
            raise ValueError("Targets list is empty")

    def getOnPath(self, targets, nbPoints):
        """
        Gets specified number of points between targets
        """
        if (len(targets)==0 or nbPoints<len(targets)):
            raise ValueError("Invalid arguments")
        else:
            requestURL = self.baseURL+"path="
            for target in targets:
                requestURL+="{},{}|".format(target.latitude,
                                            target.longitude)
            requestURL = requestURL[:-1]+"&samples={}".format(nbPoints)
            response = urlopen(requestURL)
            jsonResponse = json.loads(response.read())
            #print(jsonResponse)
            return [point["elevation"] for point in jsonResponse["results"]]
                
    
