# -*- coding: utf-8 -*-
import unittest
from src.main.grid import Grid
from src.main.rect import Rectangle

class TestGrid(unittest.TestCase):
    def test_clone_grid(self):
        self.assertTrue(True)

    def test_arr2d_coppies_dimensions(self):
        foo = Grid(Rectangle(0, 5, 0, 2))
        self.assertEqual(len(foo.cells), 5)
        self.assertEqual(len(foo.cells[0]), 2)

    def test_arr2d_fills_with_None(self):
        foo = Grid(Rectangle(0, 5, 0, 2))
        self.assert_all_cells_equal(foo, None)

    def test_fill_rect_fills_value_to_cells(self):
        foo = Grid(Rectangle(0, 5, 0, 2))
        foo.fill_rect(lambda: 9)
        self.assert_all_cells_equal(foo, 9)

    def assert_all_cells_equal(self, grid, value):
        self.assertEqual(grid.cells[0][0], value)
        self.assertEqual(grid.cells[len(grid.cells)-1][len(grid.cells[0])-1], value)

    def test_arr2d_with_lambda(self):
        foo = Grid(Rectangle(0, 4, 0, 2), lamb=lambda: 1)
        self.assert_all_cells_equal(foo, 1)

    def assert_grids_equal(self, grida, gridb):
        self.assertEqual(len(grida), len(gridb))
        self.assertEqual(len(grida[0]), len(gridb[0]))
        for y in range(len(grida)):
            for x in range(len(grida[y])):
                self.assertEqual(grida[y][x], gridb[y][x])

    def test_clone(self):
        foo = Grid(Rectangle(0, 1, 0, 1), lamb=lambda: "spaget")
        bar = foo.clone()
        self.assertEqual(foo.cells, bar.cells)

    def test_clone_doesnt_copy_by_reference(self):
        foo = Grid(Rectangle(0, 1, 0, 1))
        bar = foo.clone()
        foo.cells[0][0] = "spaget"
        self.assertNotEqual(foo, bar)

    def test_add_grids(self):
        base = Grid(Rectangle(0, 3, 0, 3), lamb=lambda: 0)
        detail = Grid(Rectangle(0, 2, 0, 2), lamb=lambda: 1)
        result = base.add_grids(detail)
        expected = [
                [1, 1, 0],
                [1, 1, 0],
                [0, 0, 0]]
        self.assert_grids_equal(result.cells, expected)

    def test_add_grids_doesnt_crash_on_overhang(self):
        base = Grid(Rectangle(0, 3, 0, 3), lamb=lambda: 0)
        detail = Grid(Rectangle(2, 4, 2, 4), lamb=lambda: 1)
        result = base.add_grids(detail)
        expected = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 1]]
        self.assert_grids_equal(result.cells, expected)

    def test_add_grids_doesnt_crash_on_underhang(self):
        base = Grid(Rectangle(0, 3, 0, 3), lamb=lambda: 0)
        detail = Grid(Rectangle(-1, 1, -1, 1), lamb=lambda: 1)
        result = base.add_grids(detail)
        expected = [
                [1, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        self.assert_grids_equal(result.cells, expected)

