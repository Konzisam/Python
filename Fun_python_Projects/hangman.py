import random

print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
answer = random.choice(words)
# hint = answer[0:3]
guess = list("-" * (len(answer)))


def menu():
    return input("Type \"play\" to play the game, \"exit\" to quit:")


def the_value_of_life():
    # answer = random.choice(words)
    # hint = answer[0:3]
    # guess = list("-" * (len(answer)))
    tries = 8
    fails = 0
    already_tried = []
    # print(already_tried)
    for _ in range(tries):
        while True:
            print("")
            print("".join([str(elem) for elem in guess]))
            word = input("Input a letter: ")
            if len(word) != 1:
                print("You should input a single letter")
            elif not (word.islower()):
                print("Please enter a lowercase English letter")

            elif word in already_tried:
                print("You\'ve already guessed this letter")
                # tries -= 1
                # fails += 1
            elif word in answer:

                for i in range(len(answer)):
                    if answer[i] == word:
                        guess[i] = word
                        # already_tried.append(word)

                        # print(''.join(guess))
                        # print(answer)
                if answer == ''.join(guess):
                    print(f"You guessed the word {answer}!")
                    print("You survived!")
                    return False

            else:
                tries -= 1
                fails += 1
                print("That letter doesn't appear in the word")
            already_tried.append(word)
            # print(already_tried)
            if fails == 8:
                print("You lost!")
                return False


if menu() == 'play':
    the_value_of_life()
elif menu() == 'exit':
    pass
else:
    menu()
