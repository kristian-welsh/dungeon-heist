from src.main.game import Game
from src.main.dungeon import Dungeon
from src.main.roomgen import RoomGenerator, RandomFacade
import src.main.inputs 

if __name__ == "__main__":
    dungeon = Dungeon(100, 46, RoomGenerator(RandomFacade(), 100, 46))
    keyboard = src.main.inputs.build_keyboard()
    Game(dungeon, keyboard).start()

