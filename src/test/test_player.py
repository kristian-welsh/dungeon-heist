import unittest
import mock

from src.main.cells import PlayerCell
from src.main.player import Player

class TestPlayer(unittest.TestCase):
    def test_retains_position(self):
        foo = Player(3, 4)
        self.assertEqual(3, foo.x)
        self.assertEqual(4, foo.y)

    def test_can_update_player_position(self):
        foo = Player(1, 1)
        foo.update(2, 3)
        self.assertEqual(foo.x, 3)
        self.assertEqual(foo.y, 4)

    @mock.patch('src.main.player.Grid')
    def test_retains_grid(self, grid_mock):
        foo = Player(0, 0)
        grid_mock.assert_called()
                                                               
