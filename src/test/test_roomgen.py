import unittest
from src.main.roomgen import RoomGenerator, RectangleGenerator, RandomFacade
from src.main.rect import Rectangle

def roomSized(width, height):
    return Rectangle(0, height, 0, width)

class TestRoomGenerator(unittest.TestCase):
    def test_istiny_returns_true_for_rooms_below_minsize(self):
        roomgen = RoomGenerator(FakeRandomFacade([0]), 0, 0)

        roomgen.minsize = (5, 3)
        equal = roomgen.isTiny(roomSized(5, 3))
        tinyWidth = roomgen.isTiny(roomSized(4, 3))
        tinyHeight = roomgen.isTiny(roomSized(5, 2))

        self.assertEqual(False, equal)
        self.assertEqual(True, tinyWidth)
        self.assertEqual(True, tinyHeight)

    def test_to_grid_makes_correctly_sized_grid(self):
        roomgen = RoomGenerator(FakeRandomFacade([0]), 0, 0)
        room = Rectangle(10, 3, 10, 5)

        result = roomgen.to_grid(room)

        self.assert_rect_equal(room, result.rect)

    def test_to_grid_gives_correct_cell_contents(self):
        roomgen = RoomGenerator(FakeRandomFacade([0]), 0, 0)
        room = Rectangle(0, 1, 0, 1)

        result = roomgen.to_grid(room, lambda:'#')

        self.assertEqual('#', result.cells[0][0])

    def assert_rect_equal(self, expected, actual):
        self.assertEqual(expected.top, actual.top)
        self.assertEqual(expected.bottom, actual.bottom)
        self.assertEqual(expected.left, actual.left)
        self.assertEqual(expected.right, actual.right)

class TestRectangleGenerator(unittest.TestCase):
    def test_maxSize_accounts_for_minsize(self):
        levelsize = (100, 100)
        minsize = (10, 10)
        size_factor = (1, 1)
        rect_gen = RectangleGenerator(FakeRandomFacade([]), levelsize, minsize, size_factor)

        result = rect_gen.maxSize((5, 5))

        self.assertEqual(minsize, result)

    def test_maxSize_accounts_for_size_factor(self):
        levelsize = (100, 100)
        minsize = (10, 10)
        size_factor = (2, 3)
        rect_gen = RectangleGenerator(FakeRandomFacade([]), levelsize, minsize, size_factor)

        result = rect_gen.maxSize((20, 20))

        self.assertEqual((20*2, 20*3), result)

    def test_maxSize_doesnt_cap_at_levelsize(self):
        levelsize = (100, 100)
        minsize = (10, 10)
        size_factor = (1, 1)
        rect_gen = RectangleGenerator(FakeRandomFacade([]), levelsize, minsize, size_factor)

        result = rect_gen.maxSize((200, 200))

        self.assertEqual((200, 200), result)

class FakeRandomFacade(RandomFacade):
    def __init__(self, returnValues):
        self.returnValues = returnValues
        self.currentVal = 0
        self.calls = []

    def randint(self, minN, maxN):
        value = self.returnValues[self.currentVal]
        self.currentVal = self.currentVal + 1
        self.calls.append((minN, maxN))
        return value

