# This is a sample Python script.
from english_words import english_words_lower_alpha_set


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def next_guess(words, index = 0):
    all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']

    letter_counts = [len([word for word in words if letter in word]) for letter in all_letters]
    word_scores = [sum([letter_counts[all_letters.index(letter)] * (7 - word.count(letter)) for letter in word]) for
                   word in words]
    word_scores, words = zip(*sorted(zip(word_scores, words), reverse=True))
    return words[index]


def filter_list(words, result, guess):
    checked_letters = []
    for i, (result_num, letter) in enumerate(zip(result, guess)):
        if guess.count(letter) == 1:
            if result_num == '0':
                words = [word for word in words if not letter in word]
            if result_num == '1':
                words = [word for word in words if letter in word and not word[i] == letter]
            if result_num == '2':
                words = [word for word in words if word[i] == letter]
        else:
            if letter in checked_letters:
                continue
            guess_occurences = [i for i, guess_letter in enumerate(guess) if guess_letter == letter]
            result_for_letters = [result[i] for i in guess_occurences]

            if "0" in result_for_letters:
                if "1" in result_for_letters or "2" in result_for_letters:
                    words = [word for word in words if word.count(letter) == len(result_for_letters) - 1]
                else:
                    words = [word for word in words if letter not in word]
            else:
                words = [word for word in words if word.count(letter) >= len(result_for_letters)]

            for i, result_instance in enumerate(result_for_letters):
                if result_instance == "1":
                    words = [word for word in words if word[i] != letter]
                elif result_instance == "2":
                    words = [word for word in words if word[guess_occurences[i]] == letter]

        checked_letters.append(letter)

    return words


def correct_result(results):
    for result in results:
        if result != "2":
            return False
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    words = [word for word in english_words_lower_alpha_set if len(word) == 5 and word.isalpha()]

    quit = 'a'
    result = [0, 0, 0, 0, 0]
    guess_num = 0
    while not correct_result(result):
        result = 'new word'
        i = 0
        guess_num += 1
        while result == "new word":
            print("Selecting guess from: " + str(len(words)))
            guess = next_guess(words, i)
            i += 1
            print("Guess #" + str(guess_num) + " should be: " + guess)

            result = input("Enter your result as a string with 0 being grey, 1 being yellow, 2 being green: ")

        result = [char for char in result]
        words = filter_list(words, result, guess)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
