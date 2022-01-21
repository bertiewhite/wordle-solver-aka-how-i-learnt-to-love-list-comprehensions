from english_words import english_words_lower_alpha_set


class Player:

    def __init__(self):
        self.all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.words = [word for word in english_words_lower_alpha_set if len(word) == 5 and word.isalpha()]

    def next_guess(self):
        pass

    def new_guess(self):
        return self.words.pop(0)

    def filter_list(self, result, guess):
        pass
