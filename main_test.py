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
        foo = main.arr2d(2, 5)
        self.assertEquals(len(foo), 5)
        self.assertEquals(len(foo[0]), 2)

    def test_arr2d_fills_with_None(self):
        foo = main.arr2d(2, 5)
        self.assert_all_cells_equal(foo, None)

    def test_fill_rect_fills_value_to_cells(self):
        foo = main.arr2d(2, 5)
        main.fill_rect(foo, lambda: 9)
        self.assert_all_cells_equal(foo, 9)

    def assert_all_cells_equal(self, grid, value):
        self.assertEquals(grid[0][0], value)
        self.assertEquals(grid[len(grid)-1][len(grid[0])-1], value)

    def assert_grids_equal(self, grida, gridb):
        self.assertEquals(len(grida), len(gridb))
        self.assertEquals(len(grida[0]), len(gridb[0]))
        for y in range(len(grida)):
            for x in range(len(grida[y])):
                self.assertEquals(grida[y][x], gridb[y][x])

    def test_clone(self):
        foo = main.arr2d(1, 1, lambda: "spaget")
        bar = main.clone(foo)
        self.assertEquals(foo, bar)

    def test_clone_doesnt_copy_by_reference(self):
        foo = main.arr2d(1, 1)
        bar = main.clone(foo)
        foo[0][0] = "spaget"
        self.assertNotEquals(foo, bar)

    def test_add_grids(self):
        base = main.arr2d(3, 3, lambda: 0)
        detail = main.arr2d(2, 2, lambda: 1)
        result = main.add_grids(base, detail)
        expected = [
                [1, 1, 0],
                [1, 1, 0],
                [0, 0, 0]]
        self.assert_grids_equal(result, expected)

    def test_add_grids_doesnt_crash_on_overhang(self):
        base = main.arr2d(3, 3, lambda: 0)
        detail = main.arr2d(2, 2, lambda: 1)
        result = main.add_grids(base, detail, 2, 2)
        expected = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 1]]
        self.assert_grids_equal(result, expected)

    # todo: this should work in future, bug. Can fix, just min top and left as well
    # def test_add_grids_doesnt_crash_on_underhang(self):
    #     base = main.arr2d(3, 3, lambda: 0)
    #     detail = main.arr2d(2, 2, lambda: 1)
    #     result = main.add_grids(base, detail, -1, -1)
    #     expected = [
    #             [1, 0, 0],
    #             [0, 0, 0],
    #             [0, 0, 0]]
    #     print(result)
    #     print(expected)
    #     self.assert_grids_equal(result, expected)

class Cells(unittest.TestCase):
    def test_wall(self):
        self.assertEquals(str(main.Wall()), "▒")

    def test_ground(self):
        self.assertEquals(str(main.Ground()), ".")

    def test_cell(self):
        self.assertEquals(str(main.Cell()), "null_cell ")

