import random


class Master_mind:

    def __init__(self):
        self._colors = 0
        self._positions = 0
        self._secret_code = []
        self._rounds = 0
        self._game_over = False

    def setup_game(self, colors, positions):
        self._colors = colors
        self._positions = positions
        self._generate_secret_code()
        self._game_over = False
        self._rounds = 0

    def _generate_secret_code(self):
        self._secret_code = [random.randint(1, self._colors) for _ in range(self._positions)]




