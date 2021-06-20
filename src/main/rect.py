class Rectangle:
    def __init__(self, top, bottom, left, right):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right

    def union(self, other):
        return Rectangle(
            top = max(self.top, other.top),
            bottom = min(self.bottom, other.bottom),
            left = max(self.left, other.left),
            right = min(self.right, other.right))

    def cut(self, inner):
        outer = self
        TL = Rectangle(outer.top, inner.top,  outer.left, inner.left)
        TM = Rectangle(outer.top, inner.top,  inner.left, inner.right)
        TR = Rectangle(outer.top, inner.top,  inner.right, outer.right)

        ML = Rectangle(inner.top, inner.bottom,  outer.left, inner.left)
        MM = Rectangle(inner.top, inner.bottom,  inner.left, inner.right)
        MR = Rectangle(inner.top, inner.bottom,  inner.right, outer.right)

        BL = Rectangle(inner.bottom, outer.bottom,  outer.left, inner.left)
        BM = Rectangle(inner.bottom, outer.bottom,  inner.left, inner.right)
        BR = Rectangle(inner.bottom, outer.bottom,  inner.right, outer.right)

        return ((TL, TM, TR),
                (ML, MM, MR),
                (BL, BM, BR))

    def width(self):
        return self.right - self.left

    def height(self):
        return self.bottom - self.top

    def __str__(self):
        return 'Rectangle(' + \
        ' top: ' + str(self.top) + \
        ' bottom: ' + str(self.bottom) + \
        ' left: ' + str(self.left) + \
        ' right: ' + str(self.right) + \
        ' )'
