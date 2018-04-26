import sys
import random
import os


def getlist_words(path):
    words=[]
    try:
        with open(path, "r") as file:
            for line in file:
                for word in line.split():
                    word.lower()
                    if word.isalpha():
                        words.append(word)
        if len(words) < 1:
            print("There are no words in the doc you pointed me.")
            exit(1)
        return words
    except IOError:
        print("There was a problem in IO action. Try again please.")
        exit(1)


def main():
    if len(sys.argv) < 2:
        print("Give filepath to words")
        exit(1)

    words = getlist_words(sys.argv[1])
    attempts = 0
    if len(words) < 1:
        raise IOError("The document has no words.")
    word = random.choice(words)
    guessed = "_" * len(word)
    tried=[]
    while attempts < 3 and guessed != word:
        guess = input("Guess a letter: ").lower()
        os.system('cls' if os.name == 'nt' else 'clear')

        if guess.isalpha() and len(guess) == 1:
            if guess not in tried:
                tried.append(guess)
                if guess in word:
                    print("Correct! You have guessed one of the letters. You have {} attempts left".format(3-attempts))
                    for index in [pos for pos, letter in enumerate(word) if letter == guess]:
                        guessed = list(guessed)
                        guessed[index] = guess
                        guessed = "".join(guessed)
                else:
                    attempts += 1
                    print("Letter {} is not in the word. Try again, you have {} more attempts.".format(guess, 3-attempts))
            else:
                print("You have already tried this letter!")

            print("This is your guessword: {}".format(guessed))
        else:
            print("Wrong input type, please give me one alphanumeric letter")
    if guessed == word:
        print("You have completed your quest, congrats!")
    else:
        print("You have ran out of attempts,thus failing - too bad.")

if __name__ == '__main__':
    main()