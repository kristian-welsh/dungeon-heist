from src.main.game import Game
from src.main.dungeon import Dungeon, RoomGenerator

if __name__ == "__main__":
    Game(Dungeon(210, 46, RoomGenerator(210, 46))).start()

