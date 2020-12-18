# -*- coding: utf-8 -*-
import unittest
import main

class TestDungeon(unittest.TestCase):
    def test_init(self):
        # todo
        self.assertTrue(True)

class Utils(unittest.TestCase):
    def test_clone_grid(self):
        self.assertTrue(True)

    def test_arr2d_coppies_dimensions(self):
        foo = main.Grid(2, 5)
        self.assertEquals(len(foo.cells), 5)
        self.assertEquals(len(foo.cells[0]), 2)

    def test_arr2d_fills_with_None(self):
        foo = main.Grid(2, 5)
        self.assert_all_cells_equal(foo, None)

    def test_fill_rect_fills_value_to_cells(self):
        foo = main.Grid(2, 5)
        foo.fill_rect(lambda: 9)
        self.assert_all_cells_equal(foo, 9)

    def assert_all_cells_equal(self, grid, value):
        self.assertEquals(grid.cells[0][0], value)
        self.assertEquals(grid.cells[len(grid.cells)-1][len(grid.cells[0])-1], value)

    def test_arr2d_with_lambda(self):
        foo = main.Grid(2, 4, lambda: 1)
        self.assert_all_cells_equal(foo, 1)

    def assert_grids_equal(self, grida, gridb):
        self.assertEquals(len(grida), len(gridb))
        self.assertEquals(len(grida[0]), len(gridb[0]))
        for y in range(len(grida)):
            for x in range(len(grida[y])):
                self.assertEquals(grida[y][x], gridb[y][x])

    def test_clone(self):
        foo = main.Grid(1, 1, lambda: "spaget")
        bar = foo.clone()
        self.assertEquals(foo.cells, bar.cells)

    def test_clone_doesnt_copy_by_reference(self):
        foo = main.Grid(1, 1)
        bar = foo.clone()
        foo.cells[0][0] = "spaget"
        self.assertNotEquals(foo, bar)

    def test_add_grids(self):
        base = main.Grid(3, 3, lambda: 0)
        detail = main.Grid(2, 2, lambda: 1)
        result = base.add_grids(detail)
        expected = [
                [1, 1, 0],
                [1, 1, 0],
                [0, 0, 0]]
        self.assert_grids_equal(result.cells, expected)

    def test_add_grids_doesnt_crash_on_overhang(self):
        base = main.Grid(3, 3, lambda: 0)
        detail = main.Grid(2, 2, lambda: 1)
        result = base.add_grids(detail, 2, 2)
        expected = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 1]]
        self.assert_grids_equal(result.cells, expected)

    def test_add_grids_doesnt_crash_on_underhang(self):
        base = main.Grid(3, 3, lambda: 0)
        detail = main.Grid(2, 2, lambda: 1)
        result = base.add_grids(detail, -1, -1)
        expected = [
                [1, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        self.assert_grids_equal(result.cells, expected)

class Cells(unittest.TestCase):
    def test_wall(self):
        self.assertEquals(str(main.Wall()), "▒")

    def test_ground(self):
        self.assertEquals(str(main.Ground()), ".")

    def test_cell(self):
        self.assertEquals(str(main.Cell()), "null_cell ")

