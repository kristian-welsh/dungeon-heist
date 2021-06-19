from unittest import TestCase
import mock
from mock import call

from src.main.game import Game
from src.main.dungeon import Dungeon

class TestGame(TestCase):

    @mock.patch('src.main.game.print')
    @mock.patch('src.main.dungeon.Dungeon')
    @mock.patch('src.main.game.src.main.inputs')
    def test_z_halts_running_game(self, input_mock, dungeon_mock, print_mock):
        game = Game(dungeon_mock)
        input_mock.getkey.return_value = 'q'
        # test successful if game.start() does not halt indefinitely.
        game.start()

    @mock.patch('src.main.game.print')
    @mock.patch('src.main.dungeon.Dungeon')
    @mock.patch('src.main.game.src.main.inputs')
    def test_wasd_moves_character(self, input_mock, dungeon_mock, print_mock):
        game = Game(dungeon_mock)
        input_mock.getkey.side_effect = ['w', 'a', 's', 'd', 'q']
        game.start()
        dungeon_mock.update_player.assert_has_calls([
            call(0, -1),
            call(-1, 0),
            call(0, 1),
            call(1, 0)
        ])

