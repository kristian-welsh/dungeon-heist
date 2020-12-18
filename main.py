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

class Dungeon:
    """ todo: extract world shard base class
        create method to stamp on on top of other
        params x and y starting point
        dont go over edge of bottom shard """

    def __str__(self):
        return str(self.grid)

    def __init__(self, width, height):
        self.grid = Grid(width, height, lambda:Wall())
        room1 = Grid(10, 5, lambda:Ground())
        room2 = Grid(6, 9, lambda:Ground())
        room3 = Grid(11, 3, lambda:Ground())
        self.grid = self.grid.add_grids(room1, 3, 6)
        self.grid = self.grid.add_grids(room2, 27, 13)
        self.grid = self.grid.add_grids(room3, 20, 5)

class Grid:
    """ todo: accept rectangle in constructor, save and drive behaviour with it """
    def __init__(self, width, height, lamb=lambda:None):
        self.cells = []
        for y in range(height):
            self.cells.append([])
            for x in range(width):
                self.cells[y].append(lamb())

    @classmethod
    def from_cells(cls, cells):
        self = cls(len(cells[0]), len(cells))
        self.cells = cells
        return self

    def __str__(self):
        output = ""
        for row in self.cells:
            for cell in row:
                output += str(cell)
            output += "\n"
        return output

    def clone(self):
        """ assumes self.cells has a height of at least one """
        copy = Grid(len(self.cells[0]), len(self.cells))
        for y in range(len(self.cells)):
            for x in range(len(self.cells[y])):
                copy.cells[y][x] = self.cells[y][x]
        return copy

    def fill_rect(self, cell_lambda):
        for y in range(len(self.cells)):
            for x in range(len(self.cells[y])):
                self.cells[y][x] = cell_lambda()

    def add_grids(self, detail_grid, detail_x=0, detail_y=0):
        """
        does not update in place, returns a brand new grid with result 
        details over edge of base are ignored becuase of addition rect
        """
        my_rect = Rectangle(top=0, bottom=len(self.cells), left=0, right=len(self.cells[0]))
        detail_width = len(detail_grid.cells[0])
        detail_height = len(detail_grid.cells)
        detail_rect = Rectangle(top=detail_y, bottom=detail_height+detail_y, left=detail_x, right=detail_width+detail_x)
        addition = my_rect.union(detail_rect)
        result = self.clone()
        for y in range(addition.top, addition.bottom):
            for x in range(addition.left, addition.right):
                result.cells[y][x] = detail_grid.cells[y - detail_y][x - detail_x]
        return Grid.from_cells(result.cells)

class Rectangle:
    def __init__(self, top, bottom, left, right):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right

    def union(self, other):
        return Rectangle(
            right = min(self.right, other.right),
            bottom = min(self.bottom, other.bottom),
            left = max(self.left, other.left),
            top = max(self.top, other.top))


if __name__ =="__main__":
    height = 25
    width = 50
    print(Dungeon(width, height))

