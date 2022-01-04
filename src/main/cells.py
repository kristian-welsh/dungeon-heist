# -*- coding: utf-8 -*-
class Cell:
    def collides(self):
        return False

    def __str__(self):
        return "null_cell "

class Ground(Cell):
    def collides(self):
        return False

    def __str__(self):
        return "."

class Wall(Cell):
    def collides(self):
        return True

    def __str__(self):
        return "▒"

class PlayerCell(Cell):
    def collides(self):
        return True

    def __str__(self):
        return "@"
# is Player a cell? What is a cell?
