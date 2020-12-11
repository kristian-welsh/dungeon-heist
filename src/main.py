# -*- coding: utf-8 -*-
class Cell:
    def __str__(self):
        return "null_cell "

class Ground(Cell):
    def __str__(self):
        return " "

class Wall(Cell):
    def __str__(self):
        return "▒"

def arr2d(width, height):
    cells = []
    for y in range(height):
        cells.append([])
        for x in range(width):
            cells[y].append(None)
    return cells

class Dungeon:
    """ todo: extract world shard base class
        create method to stamp on on top of other
        params x and y starting point
        dont go over edge of bottom shard """

    def __str__(self):
        output = ""
        for row in self.cells:
            for cell in row:
                output += str(cell)
            output += "\n"
        return output
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = arr2d(width, height)
        self.gen_rock()

    def gen_rock(self):
        for y in range(len(self.cells)):
            for x in range(len(self.cells[y])):
                self.cells[y][x] = Wall()

def print_dungeon():
    height = 25
    width = 50
    print(Dungeon(width, height))

print_dungeon()

