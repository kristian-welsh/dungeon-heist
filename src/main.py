class Cell:
    def __str__(self):
        return "null_cell"

class Ground(Cell):
    def __str__(self):
        return "."

class Grid:
    def display(self, x, y):
        return str(self.cells[y][x])

    def __str__(self):
        output = ""
        for y in range(self.height):
            for x in range(self.width):
                output += self.display(x, y)
            output += "\n"
        return output
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.generate_ground()

    def generate_ground(self):
        self.cells = []
        for y in range(self.height):
            self.cells.append([])
            for x in range(self.width):
                self.cells[y].append(Ground())

def print_grid():
    height = 25
    width = 50
    print(Grid(width, height))

print_grid()

