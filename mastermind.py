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
        guess = input("Enter your guess: ")
        if len(guess) > self._positions:
            print(f"Too many digits. Please enter exactly {self._positions} digits.")

        if len(guess) < self._positions:
            print(f"Not enough digits. Please enter exactly {self._positions} digits.")

        converted_guess = []
        for i in guess[:self._positions]:
            num = int(i)
            converted_guess.append(num)
        return converted_guess

    def dump_game_state(self):
        if self._game_over:
            print(f"Secret code: {self._secret_code}")
            print(f"Total rounds played: {self._rounds}")
        else:
            print("The game is still in progress.")

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

