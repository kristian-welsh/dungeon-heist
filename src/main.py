# -*- coding: utf-8 -*-
import math

class Cell:
    def __str__(self):
        return "null_cell "

class Ground(Cell):
    def __str__(self):
        return "."

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
        rock = self.gen_rock(width, height)
        room1 = self.gen_room(10, 5)
        room2 = self.gen_room(6, 9)
        room3 = self.gen_room(11, 3)
        self.cells = add_grids(rock, room1, 3, 6)
        self.cells = add_grids(self.cells, room2, 27, 13)
        self.cells = add_grids(self.cells, room3, 20, 5)

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

def add_grids(base_grid, detail_grid, detail_x, detail_y):
    base_right = len(base_grid[0])
    base_bottom = len(base_grid)

    detail_width = len(detail_grid[0])
    detail_height = len(detail_grid)
    detail_right = detail_width + detail_x
    detail_bottom = detail_height + detail_y

    # ends early if we reach edge of base
    addition_right = min(detail_right, base_right)
    addition_bottom = min(detail_bottom, base_bottom)
    
    result = clone(base_grid)
    for y in range(detail_y, addition_bottom):
        for x in range(detail_x, addition_right):
            result[y][x] = detail_grid[y - detail_y][x - detail_x]
    return result

# assumes grid has a height of at least one
def clone(grid):
    copy = arr2d(len(grid[0]), len(grid))
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            copy[y][x] = grid[y][x]
    return copy

def print_dungeon():
    height = 25
    width = 50
    print(Dungeon(width, height))

print_dungeon()

