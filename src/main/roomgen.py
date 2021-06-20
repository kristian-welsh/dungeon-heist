from .rect import Rectangle
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
        emptySectors = [Rectangle(0, levelHeight, 0, levelWidth)]
        rooms = []

        for i in range(self.roomnum):
            currentSector = self.selectSector(emptySectors)
            (room, validSectors) = self.changeGeography(currentSector)
            rooms.append((room, i))
            emptySectors.extend(validSectors)
            emptySectors.remove(currentSector)

        return [self.toGrid(room[0], lambda:room[1]) for room in rooms]

    def changeGeography(self, currentSector):
        roomRect = self.placeRoom(currentSector)
        innerSectors = currentSector.cut(roomRect)
        room = innerSectors[1][1]
        
        flatInnerSectors = [sector for subTuple in innerSectors for sector in subTuple]
        validSectors = self.removeSmallSectors(flatInnerSectors)
        validSectors.remove(room)
        return (room, validSectors)

    def removeSmallSectors(self, sectorList):
        tinySectors = [sector for sector in sectorList if self.isTiny(sector)]
        return [sector for sector in sectorList if sector not in tinySectors]

    def isTiny(self, sector):
        return \
        sector.width() < self.minsize[0] or \
        sector.height() < self.minsize[1]

    def selectSector(self, sectors):
        return self.rand.sample(sectors, 1)[0]

    def placeRoom(self, sector):
        roomSize = self.randomRoomSize(sector)
        startPosition = self.randomStartPosition(sector, roomSize)
        endPosition = self.calculateEndPosition(startPosition, roomSize)

        (startX, startY) = startPosition
        (endX, endY) = endPosition
        return Rectangle(startY, endY, startX, endX)

    def calculateEndPosition(self, startPosition, roomSize):
        (startX, startY) = startPosition
        (roomWidth, roomHeight) = roomSize
        return (startX + roomWidth, startY + roomHeight)

    def randomStartPosition(self, sector, roomSize):
        (minStart, maxStart) = self.startPosBounds(sector, roomSize)
        (minX, maxX) = (minStart[0], maxStart[0])
        (minY, maxY) = (minStart[1], maxStart[1])
        return (self.rand.randint(minX, maxX), self.rand.randint(minY, maxY))

    def startPosBounds(self, sector, roomSize):
        (roomWidth, roomHeight) = roomSize
        minStart = (sector.left, sector.top)
        maxStart = (sector.right - roomWidth, sector.bottom - roomHeight)
        return (minStart, maxStart)

    def randomRoomSize(self, sector):
        sectorSize = (sector.right - sector.left, sector.bottom - sector.top)
        (sectorWidth, sectorHeight) = sectorSize
        roomWidth = self.rand.randint(self.minsize[0], self.maxWidth(sectorWidth))
        roomHeight = self.rand.randint(self.minsize[1], self.maxHeight(sectorHeight))
        return (roomWidth, roomHeight)

    def maxWidth(self, sectorWidth):
        return max(self.minsize[0], int(self.sizefactor[0] * sectorWidth))

    def maxHeight(self, sectorHeight):
        return max(self.minsize[1], int(self.sizefactor[1] * sectorHeight))

    def toGrid(self, rect, lamb=lambda:None):
        width = rect.right - rect.left
        height = rect.bottom - rect.top
        return Grid(width, height, rect.left, rect.top, lamb)

class RandomFacade:
    def randint(self, minimum, maximum):
        return randint(minimum, maximum)

    def sample(self, list, numSamples):
        return sample(list, numSamples)
