from src.main.game import Game
from src.main.dungeon import Dungeon
from src.main.roomgen import RoomGenerator

if __name__ == "__main__":
    Game(Dungeon(210, 46, RoomGenerator(210, 46))).start()

