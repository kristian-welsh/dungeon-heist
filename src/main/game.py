from main.dungeon import Dungeon
import tty, sys, termios

class Game:
    def start(self):
        self.game_active = True
        self.dungeon = Dungeon(width = 50, height = 25)
        self.render()
        while self.game_active:
            key = self.getkey()
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

    # todo: belongs in class per os
    def getkey(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

