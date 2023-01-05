class Gallows:
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        if word not in self.words and (self.words == [] or word[0] == self.words[-1][-1]):
            self.words.append(word)
            return self.words

        else:
            self.game_over = True
            return 'game over'

    def restart(self):
        self.words = []
        self.game_over = False
        return 'game restarted'
