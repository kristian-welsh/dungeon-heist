class Grid:
    def display(self, x, y):
        return "."

def generate_grid():
    return Grid()

def print_grid():
    grid = generate_grid()
    output = ""
    height = 25
    width = 50
    for y in range(height):
        for x in range(width):
            output += grid.display(x, y)
        output += "\n"
    print(output)

print_grid()

