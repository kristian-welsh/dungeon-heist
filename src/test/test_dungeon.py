import unittest
from src.main.dungeon import Dungeon, RoomGenerator
from src.main.grid import Grid
from src.main.cells import Wall, Ground

class TestDungeon(unittest.TestCase):
    def test_init(self):
        # todo
        # behaviour tested here will later be extracted to WorldGen
        self.assertTrue(True)

    def test_collision_doesnt_occur(self):
        dungeon = Dungeon(50, 25, FakeRoomGenerator(50, 25))
        player = dungeon.player
        player.x = 6
        player.y = 7

        result = dungeon.collide(1, 0)
        dungeon.update_player(1, 0)

        self.assertFalse(result)
        self.assertEqual(7, player.x)
        self.assertEqual(7, player.y)

    def test_collision_occurs(self):
        """test correctness assumes placement of player in room by dungeon"""
        dungeon = Dungeon(50, 25, FakeRoomGenerator(50, 25))
        dungeon.grid.cells[7][7] = Wall()
        result = dungeon.collide(1, 0)
        self.assertTrue(result)

class FakeRoomGenerator(RoomGenerator):
    def generate(self):
        return [
            Grid(10, 5, 3, 6, lambda:Ground()),
            Grid(6, 9, 20, 5, lambda:Ground()),
            Grid(11, 3, 27, 13, lambda:Ground()),
        ]
