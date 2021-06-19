from .dungeon import Dungeon
import src.main.inputs

class Game:

    def __init__(self, dungeon):
        self.dungeon = dungeon

    def start(self):
        self.game_active = True
        while self.game_active:
            self.render()
            key = src.main.inputs.getkey()
            self.update(key)

    def update(self, key):
        (x, y) = self.direction(key)
        self.quitcheck(key)
        self.dungeon.update_player(x, y)

    def quitcheck(self, key):
        if key == 'q':
            self.game_active = False

    def direction(self, key):
        x = 0
        y = 0
        if key == 'w':
            y = -1
        elif key == 'a':
            x = -1
        elif key == 's':
            y = 1
        elif key == 'd':
            x = 1
        return (x, y)

    def render(self):
        print(self.dungeon)

