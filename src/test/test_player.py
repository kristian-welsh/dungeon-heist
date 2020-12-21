import unittest
import mock

from src.main.player import Player

class TestPlayer(unittest.TestCase):
    @mock.patch('src.main.grid.Grid')
    def test_retains_position(self, grid_mock):
        foo = Player(3, 4)
        print(grid_mock)
        self.assertEqual(3, foo.x)
        self.assertEqual(4, foo.y)
