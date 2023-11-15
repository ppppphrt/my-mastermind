import random


class Mastermind:

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

    def _get_hint(self, guess):
        correct_positions = 0
        correct_colors = 0
        temp_code = self._secret_code.copy()
        temp_guess = guess[:]

        # First pass to find correct positions
        for i in range(self._positions):
            if temp_guess[i] == temp_code[i]:
                correct_positions += 1
                temp_code[i] = temp_guess[i] = None

        # Second pass to find correct colors
        for i in range(self._positions):
            if temp_guess[i] and temp_guess[i] in temp_code:
                correct_colors += 1
                temp_code[temp_code.index(temp_guess[i])] = None

        return '*' * correct_positions + 'o' * correct_colors

    def _get_user_guess(self):
        while True:
            guess = input(f"Enter your guess ({self._positions} digits) or end: ")
            if guess == "end":
                self.dump_game_state()

            elif len(guess) == self._positions:
                try:
                    converted_guess = [int(i) for i in guess]
                    return converted_guess
                except ValueError:
                    print("Invalid input. Please enter only numeric digits.")
            else:
                print(f"Incorrect number of digits. Please enter exactly {self._positions} digits.")

    def dump_game_state(self):
        if not self._game_over:
            print(f"Secret code: {self._secret_code}")
            print(f"Total rounds played: {self._rounds}")
            exit()
        else:
            print('Still playing')

    def playing_game(self):
        print(f"Starting Mastermind with {self._colors} colors and {self._positions} positions.")
        while not self._game_over:
            guess = self._get_user_guess()
            self._rounds += 1
            hint = self._get_hint(guess)
            self._display_hint(hint)
            self._game_over = self._is_game_finished(hint)

    def _display_hint(self, hint):
        print(f"Hint: {hint}")

    def _is_game_finished(self, hint):
        return hint == '*' * self._positions


game = Mastermind()
game.setup_game(colors=6, positions=4)
game.playing_game()
game.dump_game_state()

