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

