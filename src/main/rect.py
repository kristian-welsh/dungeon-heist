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
