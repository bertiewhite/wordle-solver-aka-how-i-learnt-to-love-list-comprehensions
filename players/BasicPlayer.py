from players.Player import Player

class BasicPlayer(Player):

    def next_guess(self):
        letter_counts = [len([word for word in self.words if letter in word]) for letter in self.all_letters]
        word_scores = [sum([letter_counts[self.all_letters.index(letter)] * (7 - word.count(letter)) for letter in word]) for
                       word in self.words]
        self.words = [word for _, word in sorted(zip(word_scores, self.words),reverse=True)]

        return self.words.pop(0)

    def filter_list(self, result, guess):
        checked_letters = []
        for i, (result_num, letter) in enumerate(zip(result, guess)):
            if letter in checked_letters:
                continue
            if guess.count(letter) == 1:
                if result_num == '0':
                    self.words = [word for word in self.words if not letter in word]
                if result_num == '1':
                    self.words = [word for word in self.words if letter in word and not word[i] == letter]
                if result_num == '2':
                    self.words = [word for word in self.words if word[i] == letter]
            else:
                guess_occurences = [i for i, guess_letter in enumerate(guess) if guess_letter == letter]
                result_for_letters = [result[i] for i in guess_occurences]

                if "0" in result_for_letters:
                    if "1" in result_for_letters or "2" in result_for_letters:
                        self.words = [word for word in self.words if word.count(letter) == len(result_for_letters) - 1]
                    else:
                        self.words = [word for word in self.words if letter not in word]
                else:
                    self.words = [word for word in self.words if word.count(letter) >= len(result_for_letters)]

                for i, result_instance in enumerate(result_for_letters):
                    if result_instance == "1":
                        self.words = [word for word in self.words if word[i] != letter]
                    elif result_instance == "2":
                        self.words = [word for word in self.words if word[guess_occurences[i]] == letter]

            checked_letters.append(letter)
