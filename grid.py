#!/usr/bin/env python3
#pylint: disable-all

"""
Retrieve altitude on a grid
"""


from coordinate import Coordinate
from requestHandler import Handler
from conversion import hashCoordinate
from math import pi, sqrt

class Grid:
    """
    Class that supports the grid of elevation points
    """
    def __init__(self, start, handler, size, lines, columns):
        self.centerPoint = start
        self.size = size
        self.lines = lines
        self.columns = columns
        self.grid = [[0 for j in range(columns)] for i in range(lines)]
        self.topCorner = None
        self.gridHandler = handler

    def isTopCornerSet(self):
        return self.topCorner is not None;

    def fillGrid(self):
        """
        Fills the grid defined with given dimensions centered on given point
        """
        #TODO: Improve this by creating only one request (snail path)
        self.topCorner = self.centerPoint.travel(7*pi/8, self.size*sqrt(2)/2);
        currentPoint = self.topCorner
        betweenLines = self.size/self.lines
        for i in range(self.lines):
            lineLimits = [currentPoint,
                          currentPoint.travel(pi/2, self.size)]
            self.grid[i] = self.gridHandler.getOnPath(lineLimits, self.columns)
            self.gridHandler.hold()
            currentPoint = currentPoint.travel(pi, betweenLines)

    def writeAsPython(self, fileName=None, gridName="elevationGrid"):
        """
        Writes the grid as a Python 2D list in given file
        If no filename is provided default output will be stdout
        """
        gridString = "{}=".format(gridName)
        for i in range(self.lines):
            gridString+="["
            for j in range(self.columns):
                gridString+="{},".format(self.grid[i][j])
            gridString = gridString[:-1]+"],"
        gridString[-1] = "]"
        if (fileName is None):
            print(gridString)
        else:
            openFile = open(fileName, 'w')
            openFile.write(gridString)
            openFile.close()
            
        
    
        

if __name__ == "__main__":
    test_point = Coordinate(42.339057,13.042602)
    print(test_point)
    test_point.printAsDMS()
    new_point = test_point.travel(0, 50000)
    print(new_point)
    newHandler = Handler()
    #print(newHandler.getElevation(test_point))
    print(hashCoordinate(-179.98321))
    targetList = [Coordinate(17.7391536, -25.9847034),
                  Coordinate(-11.455556, 37.866667)]
    print(newHandler.getMultipleElevations(targetList))
    print(newHandler.getOnPath(targetList, 10))
    test_grid = Grid(test_point, newHandler, 1000, 10, 10)
    test_grid.fillGrid()
    test_grid.writeAsPython()
