import unittest
from src.main.segment import Segment
from src.main.rect import Rectangle

def seg_of(top, bottom, left, right):
    return Segment(Rectangle(top, bottom, left, right), [], [])

# 88: irrelevent
class TestSegment(unittest.TestCase):
    def test_rights_for(self):
        first = seg_of(0, 9, 88, 88)
        second = seg_of(10, 19, 88, 88)
        third = seg_of(20, 29, 88, 88)
        segment = Segment(Rectangle(88, 88, 88, 88), [first, second, third],[])

        two = segment.rights_for(Rectangle(15, 20, 88, 88))
        one_in_boundaries = segment.rights_for(Rectangle(2, 5, 88, 88))
        one_on_boundaries = segment.rights_for(Rectangle(10, 19, 88, 88))

        self.assertEqual([first], one_in_boundaries)
        self.assertEqual([second, third], two)
        self.assertEqual([second], one_on_boundaries)

    def test_downs_for(self):
        first = seg_of(88, 88, 0, 9)
        second = seg_of(88, 88, 10, 19)
        third = seg_of(88, 88, 20, 29)
        segment = Segment(Rectangle(88, 88, 88, 88), [],[first, second, third])

        two = segment.downs_for(Rectangle(88, 88, 15, 20))
        one_in_boundaries = segment.downs_for(Rectangle(88, 88, 2, 5))
        one_on_boundaries = segment.downs_for(Rectangle(88, 88, 10, 19))

        self.assertEqual([first], one_in_boundaries)
        self.assertEqual([second, third], two)
        self.assertEqual([second], one_on_boundaries)

    def test_cut(self):
        segment = Segment(Rectangle(0, 100, 0, 100), [],[])
        position = Rectangle(25, 75, 25, 75)

        result = segment.cut_rects(position)

        self.assertRectEqual(Rectangle(0, 25, 0, 100), result[0])
        self.assertRectEqual(Rectangle(25, 75, 0, 25), result[1])
        self.assertRectEqual(Rectangle(25, 75, 75, 100), result[2])
        self.assertRectEqual(Rectangle(75, 100, 0, 100), result[3])

    def assertRectEqual(self, exp, actual):
        self.assertEqual((exp.top, exp.bottom, exp.left, exp.right), 
                (actual.top, actual.bottom, actual.left, actual.right))

    def test_replacements(self):
        middle_rect = Rectangle(25, 75, 25, 75)
        segment = Segment(Rectangle(0, 100, 0, 100), [],[])

        result = segment.replacements(middle_rect)

        self.assertRectEqual(Rectangle(0, 25, 0, 100), result[0].rect)
        self.assertRectEqual(Rectangle(25, 75, 0, 25), result[1].rect)
        self.assertRectEqual(Rectangle(25, 75, 25, 75), result[2].rect)
        self.assertRectEqual(Rectangle(25, 75, 75, 100), result[3].rect)
        self.assertRectEqual(Rectangle(75, 100, 0, 100), result[4].rect)

