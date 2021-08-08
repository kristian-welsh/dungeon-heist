from src.main.game import Game
from src.main.dungeon import Dungeon
from src.main.roomgen import RoomGenerator, RandomFacade

if __name__ == "__main__":
    Game(Dungeon(100, 46, RoomGenerator(RandomFacade(), 100, 46))).start()

