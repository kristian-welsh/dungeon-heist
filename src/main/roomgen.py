from .rect import Rectangle
from .segment import Segment
from .grid import Grid
from random import *

class RoomGenerator:
    def __init__(self, rand, width, height):
        self.roomnum = 9
        self.rand = rand
        self.area_rect = Rectangle(0, height, 0, width)

        self.minsize = (int(width/20), int(height/10))
        sizefactor = (8/9, 5/7)
        self.rectgen = RectangleGenerator(rand, (width, height), self.minsize, sizefactor)

    def generate(self):
        emptySectors = [Segment(self.area_rect)]
        rooms = []

        for i in range(self.roomnum):
            currentSector = self.selectSector(emptySectors)
            (room, validSectors) = self.changeGeography(currentSector)
            rooms.append((room, i))
            emptySectors.extend(validSectors)
            emptySectors.remove(currentSector)

        return [self.to_grid(room[0].rect, lambda:room[1]) for room in rooms]

    def changeGeography(self, currentSector):
        roomRect = self.rectgen.generateRectangle(currentSector.rect)
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

    def to_grid(self, rect, lamb=lambda:None):
        return Grid(rect.width(), rect.height(), rect.left, rect.top, lamb)

class RectangleGenerator:
    def __init__(self, rand, levelsize, minsize, sizefactor):
        self.rand = rand
        self.levelsize = levelsize
        self.minsize = minsize
        self.sizefactor = sizefactor

    def generateRectangle(self, bounds):
        size = self.randomSize(bounds)
        (x, y) = self.randomStartPosition(bounds, size)
        (width, height) = size
        return Rectangle(y, y + height, x, x + width)

    def randomSize(self, bounds):
        (widthMin, heightMin) = self.minsize
        (widthMax, heightMax) = self.maxSize((bounds.width(), bounds.height()))
        width = self.rand.randint(widthMin, widthMax)
        height = self.rand.randint(heightMin, heightMax)
        return (width, height)

    def maxSize(self, boundSize):
        (widthMax, heightMax) = boundSize
        (widthMin, heightMin) = self.minsize
        (widthFactor, heightFactor) = self.sizefactor
        width = max(widthMin, int(widthFactor * widthMax))
        height = max(heightMin, int(heightFactor * heightMax))
        return (width, height)

    def randomStartPosition(self, bounds, size):
        startBounds = self.startPosBounds(bounds, size)
        x = self.rand.randint(startBounds.left, startBounds.right)
        y = self.rand.randint(startBounds.top, startBounds.bottom)
        return (x, y)

    def startPosBounds(self, bounds, size):
        (width, height) = size
        (right, bottom) = (bounds.right - width, bounds.bottom - height)
        return Rectangle(bounds.top, bottom, bounds.left, right)

class RandomFacade:
    def randint(self, minimum, maximum):
        return randint(minimum, maximum)

    def sample(self, list, numSamples):
        return sample(list, numSamples)
