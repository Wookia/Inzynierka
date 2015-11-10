#!/usr/bin/python
import math
import copy

class ShortestPath:
    road = [[]]
    globalDistance = 0
    localDistance = 0
    def __init__(self, road, globalDistance, localDistance):
        self.road = road
        self.globalDistance = globalDistance
        self.localDistance = localDistance

    def getRoad(self):
        return copy.deepcopy(self.road)

class BestWay:
    pathA = []
    pathB = []

    def __init__(self, pathA, pathB):
        self.pathA = pathA
        self.pathB = pathB
        self.pathMap = [[0 for i in range(len(pathB))] for j in range(len(pathA))]


    def getPathToMe(self, i, j):
        myMistake = self.mistake(i, j)
        if (i==0 and j ==0):
            pathRoad = [[i, j]]
            pathMistake = 1.0*myMistake
        elif (i==0 and j>0):
            path = self.pathMap[i][j - 1]
            pathRoad = path.getRoad()
            pathRoad.append([i, j])
            pathMistake = path.globalDistance + 1.0*myMistake
        elif (i>0 and j==0):
            path = self.pathMap[i-1][j]
            pathRoad = path.getRoad()
            pathRoad.append([i, j])
            pathMistake = path.globalDistance + 1.0*myMistake
        else:
            leftPath = self.pathMap[i-1][j]
            downPath = self.pathMap[i][j-1]
            diagonalPath = self.pathMap[i-1][j-1]
            leftGlobalDistance = leftPath.globalDistance
            downGlobalDistance = downPath.globalDistance
            diagonalGlobalDistance = diagonalPath.globalDistance
            if (leftGlobalDistance<=downGlobalDistance and leftGlobalDistance<=diagonalGlobalDistance):
                pathRoad = leftPath.getRoad()
                pathRoad.append([i, j])
                pathMistake = leftGlobalDistance + 1.0*myMistake
            elif (diagonalGlobalDistance<=downGlobalDistance and diagonalGlobalDistance<=leftGlobalDistance):
                pathRoad = diagonalPath.getRoad()
                pathRoad.append([i, j])
                pathMistake = diagonalGlobalDistance + self.modyficator*myMistake
            elif (downGlobalDistance<=diagonalGlobalDistance and downGlobalDistance<=leftGlobalDistance):
                pathRoad = downPath.getRoad()
                pathRoad.append([i, j])
                pathMistake = downGlobalDistance + 1.0*myMistake
        self.pathMap[i][j] = ShortestPath(pathRoad, pathMistake, myMistake)
        return self.pathMap[i][j]

    def find(self, method):
        if (method == "square"):
            self.modyficator = math.sqrt(2)
        elif (method == "taxi"):
            self.modyficator = 2.0
        elif (method == "infini"):
            self.modyficator = 1.0
        for a in range (len(self.pathA)):
            for b in range (len(self.pathB)):
                self.getPathToMe(a, b)

        pathToEnd = self.pathMap[len(self.pathA)-1][len(self.pathB)-1]
        print (method)
        print (pathToEnd.globalDistance)
        print (pathToEnd.getRoad())

    def mistake(self, i, j):
        sum = 0.0
        for x in range(0, len(self.pathA[i])):
            sum += math.pow(self.pathA[i][x]-self.pathB[j][x], 2)
        return math.sqrt(sum)

class DataGenerator:

    def __init__ (self):
        self.a = 0
    def sinus(self, start, distance, probes):
        data = []
        change = (distance)/(1.0*probes)
        end = start + distance
        while (start < end):

            data.append([math.sin(start)])
            start += change
        return data

dataGenerator = DataGenerator()
a1 = dataGenerator.sinus(0.0, 2.0*math.pi, 100)
b1 = dataGenerator.sinus(0.0, 2.0*math.pi, 100)
bestWay = BestWay(a1, b1)
bestWay.find("square")

bestWay.find("taxi")

bestWay.find("infini")
