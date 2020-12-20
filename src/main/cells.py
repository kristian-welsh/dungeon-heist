# -*- coding: utf-8 -*-
class Cell:
    def __str__(self):
        return "null_cell "

class Ground(Cell):
    def __str__(self):
        return "."

class Wall(Cell):
    def __str__(self):
        return "▒"

class PlayerCell(Cell):
    def __str__(self):
        return "@"
# is Player a cell? What is a cell?
