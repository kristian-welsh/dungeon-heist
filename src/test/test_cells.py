# -*- coding: utf-8 -*-
import unittest
from src.main.cells import Wall, Ground, Cell

class TestCells(unittest.TestCase):
    def test_wall(self):
        self.assertEqual(str(Wall()), "▒")

    def test_ground(self):
        self.assertEqual(str(Ground()), ".")

    def test_cell(self):
        self.assertEqual(str(Cell()), "null_cell ")

