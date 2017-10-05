#!/usr/bin/env python3
#pylint: disable-all

"""
Retrieve altitude on a grid
"""


from coordinate import Coordinate
from requestHandler import Handler
from conversion import hashCoordinate

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
        

if __name__ == "__main__":
    test_point = Coordinate(42.339057,13.042602)
    print(test_point)
    test_point.printAsDMS()
    new_point = test_point.travel(0, 50000)
    print(new_point)
    #newHandler = Handler()
    #print(newHandler.getElevation(test_point))
    print(hashCoordinate(-179.98321))
    
