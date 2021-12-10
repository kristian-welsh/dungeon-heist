from .rect import Rectangle
from .segment import Segment
from .grid import Grid
from random import *

class RoomGenerator:
    def __init__(self, rand, width, height):
        self.rand = rand
        self.levelsize = (width, height)
        self.minsize = (int(width/20), int(height/10))
        self.sizefactor = (1/2, 3/4)
        self.roomnum = 9

    def generate(self):
        (levelWidth, levelHeight) = self.levelsize
        emptySectors = [Segment(Rectangle(0, levelHeight, 0, levelWidth))]
        rooms = []

        for i in range(self.roomnum):
            currentSector = self.selectSector(emptySectors)
            (room, validSectors) = self.changeGeography(currentSector)
            rooms.append((room, i))
            emptySectors.extend(validSectors)
            emptySectors.remove(currentSector)

        return [self.to_grid(room[0].rect, lambda:room[1]) for room in rooms]

    def changeGeography(self, currentSector):
        roomRect = self.placeRoom(currentSector)
        newSectors = currentSector.replacements(roomRect)
        room = newSectors[2]
        emptySectors = self.removeSmallSectors(newSectors)
        emptySectors.remove(room)
        return (room, emptySectors)

    def removeSmallSectors(self, sectorList):
        tinySectors = [sector for sector in sectorList if self.isTiny(sector.rect)]
        return [sector for sector in sectorList if sector not in tinySectors]

    def isTiny(self, rect):
        return \
        rect.width() < self.minsize[0] or \
        rect.height() < self.minsize[1]

    def selectSector(self, sectors):
        return self.rand.sample(sectors, 1)[0]

########## could extract class

    def placeRoom(self, sector):
        roomSize = self.randomRoomSize(sector.rect)
        startPosition = self.randomStartPosition(sector.rect, roomSize)
        endPosition = self.calculateEndPosition(startPosition, roomSize)

        (startX, startY) = startPosition
        (endX, endY) = endPosition
        return Rectangle(startY, endY, startX, endX)

    def calculateEndPosition(self, startPosition, roomSize):
        (startX, startY) = startPosition
        (roomWidth, roomHeight) = roomSize
        return (startX + roomWidth, startY + roomHeight)

    def randomStartPosition(self, rect, roomSize):
        (minStart, maxStart) = self.startPosBounds(rect, roomSize)
        (minX, maxX) = (minStart[0], maxStart[0])
        (minY, maxY) = (minStart[1], maxStart[1])
        return (self.rand.randint(minX, maxX), self.rand.randint(minY, maxY))

    def startPosBounds(self, rect, roomSize):
        (roomWidth, roomHeight) = roomSize
        minStart = (rect.left, rect.top)
        maxStart = (rect.right - roomWidth, rect.bottom - roomHeight)
        return (minStart, maxStart)

    def randomRoomSize(self, rect):
        rectSize = (rect.right - rect.left, rect.bottom - rect.top)
        (rectWidth, rectHeight) = rectSize
        roomWidth = self.rand.randint(self.minsize[0], self.maxWidth(rectWidth))
        roomHeight = self.rand.randint(self.minsize[1], self.maxHeight(rectHeight))
        return (roomWidth, roomHeight)

    def maxWidth(self, sectorWidth):
        return max(self.minsize[0], int(self.sizefactor[0] * sectorWidth))

    def maxHeight(self, sectorHeight):
        return max(self.minsize[1], int(self.sizefactor[1] * sectorHeight))

########## class end

    def to_grid(self, rect, lamb=lambda:None):
        width = rect.right - rect.left
        height = rect.bottom - rect.top
        return Grid(width, height, rect.left, rect.top, lamb)

class RandomFacade:
    def randint(self, minimum, maximum):
        return randint(minimum, maximum)

    def sample(self, list, numSamples):
        return sample(list, numSamples)
