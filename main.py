from players.BasicPlayer import BasicPlayer

def correct_result(results):
    for result in results:
        if result != "2":
            return False
    return True

if __name__ == '__main__':
    player = BasicPlayer()

    quit = 'a'
    result = [0, 0, 0, 0, 0]

    guess_num = 0
    while not correct_result(result):
        result = 'new word'
        i = 0
        while result == "new word":
            print("Selecting guess from: " + str(len(player.words)))
            guess = player.next_guess()
            i += 1
            print("Guess #" + str(guess_num) + " should be: " + guess)

            result = input("Enter your result as a string with 0 being grey, 1 being yellow, 2 being green: ")

        result = [char for char in result]
        player.filter_list(result, guess)
        guess_num += 1