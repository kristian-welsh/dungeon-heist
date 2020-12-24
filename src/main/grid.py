from .rect import Rectangle

class Grid:
    """ todo: accept rectangle in constructor, save and drive behaviour with it """
    def __init__(self, width, height, x=0, y=0, lamb=lambda:None):
        self.rect = Rectangle(y, y + height, x, x + width)
        self.cells = []
        for y in range(height):
            self.cells.append([])
            for x in range(width):
                self.cells[y].append(lamb())

    # unused?
    @classmethod
    def from_cells(cls, cells):
        self = cls(len(cells[0]), len(cells))
        self.cells = cells
        return self

    def __str__(self):
        output = ""
        for row in self.cells:
            for cell in row:
                output += str(cell)
            output += "\n"
        return output

    def clone(self):
        """ assumes self.cells has a height of at least one """
        copy = Grid(len(self.cells[0]), len(self.cells))
        for y in range(len(self.cells)):
            for x in range(len(self.cells[y])):
                copy.cells[y][x] = self.cells[y][x]
        return copy

    def fill_rect(self, cell_lambda):
        for y in range(len(self.cells)):
            for x in range(len(self.cells[y])):
                self.cells[y][x] = cell_lambda()

    def add_grids(self, detail, detail_x=0, detail_y=0):
        """
        does not update in place, returns a brand new grid with result 
        details over edge of base are ignored becuase of addition rect
        """
        addition = self.rect.union(detail.rect)
        result = self.clone()
        # addition makes this hard to understand, better wording or arrangement needed here
        for y in range(addition.top, addition.bottom):
            for x in range(addition.left, addition.right):
                result.cells[y][x] = detail.cells[y - detail.rect.top][x - detail.rect.left]
        return result

