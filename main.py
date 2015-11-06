import math

class Path:
    road = []
    def __init__(self, mistake, distance, road):
        self.mistake = mistake
        self.distance = distance
        self.road = road

class BestWay:
    pathA = []
    pathB = []
    shortest = []

    def __init__(self, pathA, pathB):
        self.pathA = pathA
        self.pathB = pathB
        self.distance = 0.0
        self.scale = 0

    def find(self):
        path = self.shortestDistanceToMe(len(self.pathA)-1, len(self.pathB)-1, "0")
        print ("Global mistake: %f\n Global distance: %f" % (path.mistake, path.distance))
        print (path.road)

    def shortestDistanceToMe(self, i, j, parent):
        if (i==0 and j ==0):
            pathRoad = [[i, j]]
            pathDistance = 0.0
            pathMistake = self.mistake(i, j)
        elif (i==0 and j>0):
            path = self.shortestDistanceToMe(i, j-1, parent+"y")
            pathRoad = path.road
            pathRoad.append([i, j])
            pathDistance = 1 + path.distance
            pathMistake = self.mistake(i, j) + path.mistake
        elif (i>0 and j==0):
            path = self.shortestDistanceToMe(i-1, j, parent+"x")
            pathRoad = path.road
            pathRoad.append([i, j])
            pathDistance = 1 + path.distance
            pathMistake = self.mistake(i, j) + path.mistake
        else:
            leftPath = self.shortestDistanceToMe(i-1, j, parent+"x")
            downPath = self.shortestDistanceToMe(i, j-1, parent+"y")
            diagonalPath = self.shortestDistanceToMe(i-1, j-1, parent+"d")
            whereWhereYou = self.whereWhereYou(leftPath, downPath, diagonalPath)
            if(whereWhereYou == "left"):
                pathRoad = leftPath.road
                pathRoad.append([i, j])
                pathDistance = 1 + leftPath.distance
                pathMistake = self.mistake(i, j) + leftPath.mistake
            elif(whereWhereYou == "diagonal"):
                pathRoad = diagonalPath.road
                pathRoad.append([i, j])
                pathDistance = math.sqrt(2) + diagonalPath.distance
                pathMistake = self.mistake(i, j) + diagonalPath.mistake
            elif(whereWhereYou == "down"):
                pathRoad = downPath.road
                pathRoad.append([i, j])
                pathDistance = 1 + downPath.distance
                pathMistake = self.mistake(i, j) + downPath.mistake

        return Path(pathMistake, pathDistance, pathRoad)

    def whereWhereYou(self, leftPath, downPath, diagonalPath):
        left = 1.0*leftPath.mistake*self.scale + 1.0*leftPath.distance*(1.0-self.scale)
        down = 1.0*downPath.mistake*self.scale + 1.0*downPath.distance*(1.0-self.scale)
        diagonal = 1.0*diagonalPath.mistake*self.scale + 1.0*diagonalPath.distance*(1.0-self.scale)
        if(left<diagonal and left<=down):
            return "left"
        elif(diagonal<=left and diagonal<=down):
            return "diagonal"
        elif(down<diagonal and down<=left):
            return "down"

    def mistake(self, i, j):
        sum = 0.0
        for x in range(0, len(self.pathA[i])):
            sum += math.pow(self.pathA[i][x]-self.pathB[j][x], 2)
        return math.sqrt(sum)

a = [[1],[1],[2],[5]]
b = [[1],[4],[5],[6],[7]]
bestWay = BestWay(a, b)
bestWay.find()
