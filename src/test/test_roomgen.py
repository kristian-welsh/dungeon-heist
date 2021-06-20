import unittest
from src.main.roomgen import RoomGenerator, RandomFacade
from src.main.rect import Rectangle

def roomSized(width, height):
    return Rectangle(0, height, 0, width)


class TestRoomGenerator(unittest.TestCase):
    def test_init(self):
        self.assertTrue(True)

    def test_istiny_returns_true_for_rooms_below_minsize(self):
        roomgen = RoomGenerator(FakeRandomFacade([0]), 0, 0)

        roomgen.minsize = (5, 3)
        equal = roomgen.isTiny(roomSized(5, 3))
        tinyWidth = roomgen.isTiny(roomSized(4, 3))
        tinyHeight = roomgen.isTiny(roomSized(5, 2))

        self.assertEqual(False, equal)
        self.assertEqual(True, tinyWidth)
        self.assertEqual(True, tinyHeight)

    #def test_toGrid_makes_correctly_sized_grid(self):

class FakeRandomFacade(RandomFacade):
    def __init__(self, returnValues):
        self.returnValues = returnValues
        self.currentVal = 0

    def randint(self):
        value = self.returnValues[self.currentVal]
        self.currentVal = self.currentVal + 1
        return value

