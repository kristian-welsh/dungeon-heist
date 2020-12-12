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
        self.cells = self.gen_rock(width, height)
        self.cells = self.gen_room(10, 5)

    def gen_rock(self, width, height):
        cells = arr2d(width, height)
        fill_rect(cells, lambda : Wall())
        return cells

    def gen_room(self, width, height):
        cells = arr2d(width, height)
        fill_rect(cells, lambda : Ground())
        return cells

def fill_rect(cells, cell_lambda):
    for y in range(len(cells)):
        for x in range(len(cells[y])):
            cells[y][x] = cell_lambda()

def print_dungeon():
    height = 25
    width = 50
    print(Dungeon(width, height))

print_dungeon()

