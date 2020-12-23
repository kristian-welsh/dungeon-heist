from src.main.game import Game
from src.main.dungeon import Dungeon

if __name__ == "__main__":
    Game(Dungeon(50, 25)).start()

