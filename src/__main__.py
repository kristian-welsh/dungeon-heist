from src.main.game import Game
from src.main.dungeon import Dungeon
from src.main.roomgen import RoomGenerator, RandomFacade

if __name__ == "__main__":
    Game(Dungeon(210, 46, RoomGenerator(RandomFacade(), 210, 46))).start()

