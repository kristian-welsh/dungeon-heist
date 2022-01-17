from .grid import Grid
from .cells import EnemyCell
from .rect import Rectangle

class Enemy():

    def update(self, addx, addy):
        self.grid.rect.left = self.grid.rect.left + addx
        self.grid.rect.top = self.grid.rect.top + addy
        self.grid.rect.right = self.grid.rect.right + addx
        self.grid.rect.bottom = self.grid.rect.bottom + addy
        self.x = self.x + addx
        self.y = self.y + addy

    def __init__(self, x, y):
        """
        grid is really becoming something like Sprite
        i guess grid is really sprite, and its current default constructor 
        draws a rectangle in that sprite of width by height.
        I guess that means Dungeon isuStage
        """
        player_rect = Rectangle(y, y + 1, x, x + 1)
        self.grid = Grid(player_rect, lambda: EnemyCell())
        self.x = x
        self.y = y
