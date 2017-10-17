#!/usr/bin/env python3
#pylint: disable-all

"""
Handles all types of request to the elevation API
"""

from urllib.request import urlopen
import simplejson as json
from coordinate import Coordinate
from time import sleep
from random import random

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
        response = self.requestDecoder(requestURL)
        return response["results"][-1]["elevation"]

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
            response = self.requestDecoder(requestURL)
            return [target["elevation"] for target in response["results"]]
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
            response = self.requestDecoder(requestURL)
            return [point["elevation"] for point in response["results"]]

    def catchError(self, formattedResponse):
        """
        Catches an error in the request
        """
        status = formattedResponse["status"]
        if (status != "OK"):
            print("An error occured with code: {}".format(status))
        return formattedResponse

    def requestDecoder(self, request):
        """
        Posts a request and decodes the response
        """
        response = urlopen(request)
        jsonResponse = json.loads(response.read())
        return self.catchError(jsonResponse)

    def hold(self):
        """
        Handler waits for a random amount of time between requests
        """
        sleep(2*random())
                
    
