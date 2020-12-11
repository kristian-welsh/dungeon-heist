class Grid:
    def display(self, x, y):
        return "."

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

def print_grid():
    height = 25
    width = 50
    print(Grid(width, height))

print_grid()

