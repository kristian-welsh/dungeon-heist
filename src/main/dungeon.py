from .cells import Wall, Ground
from .grid import Grid
from .player import Player
from .rect import Rectangle
from random import *

class Dungeon:
    """ todo: extract world shard base class
        create method to stamp on on top of other
        params x and y starting point
        dont go over edge of bottom shard
        
        this class will evolve to become the logic for actions
        to perform in the dungeon, manipulated by game.
        There will be a seperate object for generating cells, 
        and a constructor here will accept a grid.
        Think of it like Dungeon is the dungeon as it currently
        exists, inclusive of changes and current state. """

    def __str__(self):
        display = self.grid.add_grids(self.player.grid)
        return str(display)

    def __init__(self, width, height, room_generator):
        self.player = Player(6, 7)
        self.rooms = room_generator.generate()
        self.grid = self.make_grid(width, height)

    def make_grid(self, width, height):
        grid = Grid(width, height, 0, 0, lambda:Wall())
        for room in self.rooms:
            grid = grid.add_grids(room, room.rect.left, room.rect.top)
        return grid


    def update_player(self, addx, addy):
        if not self.collide(addx, addy):
            self.player.update(addx, addy)

    def collide(self, addx, addy):
        new_x = self.player.x + addx
        new_y = self.player.y + addy
        print(self.grid.cells[new_y][new_x])
        return self.grid.cells[new_y][new_x].collides()


class RoomGenerator:
    def __init__(self, width, height):
        self.levelsize = (width, height)
        self.minsize = (int(width/20), int(height/10))
        self.sizefactor = (1/2, 3/4)
        self.roomnum = 9

    def generate(self):
        (levelWidth, levelHeight) = self.levelsize
        emptySectors = [Rectangle(0, levelHeight, 0, levelWidth)]
        rooms = []

        for i in range(self.roomnum):
            # select sector to place a room in
            currentSector = sample(emptySectors, 1)[0]
            (sectorX, sectorY, sectorEndX, sectorEndY) = (currentSector.left, currentSector.top, currentSector.right, currentSector.bottom)

            # calculate desired room dimensions
            (sectorWidth, sectorHeight) = (sectorEndX - sectorX, sectorEndY - sectorY)

            #print("sector X:" + str(sectorX) + " Y:" + str(sectorY))
            #print("sector Width:" + str(sectorWidth) + " Height:" + str(sectorHeight))
            roomWidth = randint(self.minsize[0], max(self.minsize[0], int(self.sizefactor[0] * sectorWidth)))
            roomHeight = randint(self.minsize[1], max(self.minsize[1], int(self.sizefactor[1] * sectorHeight)))
            maxX = sectorEndX - roomWidth
            maxY = sectorEndY - roomHeight
            #print("room Width:" + str(roomWidth) + " Height:" + str(roomHeight))
            #print("max X:" + str(maxX) + " Y:" + str(maxY))
            (startX, startY) = (randint(sectorX, maxX), randint(sectorY, maxY))
            (endX, endY) = (startX + roomWidth, startY + roomHeight)
            #print("start X:" + str(startX) + " Y:" + str(startY))
            #print("end X:" + str(endX) + " Y:" + str(endY))
            #print("---")

            # create room rect and empty sectors
            inner = Rectangle(startY, endY, startX, endX)
            innerSectors = currentSector.cut(inner)

            # isolate the innermost sector as the room, return usable empty space to sector pool
            room = innerSectors[1][1]
            emptyInnerSectors = [sector for subTuple in innerSectors for sector in subTuple]
            tinySectors = [sector for sector in emptyInnerSectors if sector.width() < self.minsize[0] or sector.height() < self.minsize[1]]
            for tiny in tinySectors:
                emptyInnerSectors.remove(tiny)

            emptyInnerSectors.remove(room)
            rooms.append((room, i))
            emptySectors.extend(emptyInnerSectors)
            emptySectors.remove(currentSector)

        return [self.toGrid(room[0], lambda:room[1]) for room in rooms]

    def toGrid(self, rect, lamb=lambda:None):
        width = rect.right - rect.left
        height = rect.bottom - rect.top
        return Grid(width, height, rect.left, rect.top, lamb)

    def available_space(self):
        return (0, 0)
