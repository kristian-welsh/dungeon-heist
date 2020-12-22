from .dungeon import Dungeon
import src.main.inputs

class Game:

    def __init__(self, dungeon):
        self.dungeon = dungeon

    def start(self):
        self.game_active = True
        self.render()
        while self.game_active:
            key = src.main.inputs.getkey()
            self.update(key)
            self.render()

    def update(self, key):
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
        elif key == 'z':
            self.game_active = False
        self.dungeon.update_player(x, y)

    def render(self):
        print(self.dungeon)

