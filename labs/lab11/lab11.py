"""
Name: <Christopher Hamilton, II>
<lab11>.py
"""


from random import randint


def play():
    w = words("wordlist.txt")
    secret = random_word(w)
    incorrect = 0
    guess = []
    current = "_" * len(secret)
    while incorrect != 7 and not won(secret, current):
        display = fill(secret, guess)
        print(display)
        print(guess)
        letter = input("Guess a letter: ")
        while letter in guess:
            letter = input("Guess a letter: ")
        guess.append(letter)
        display = fill(secret, guess)
        if display == current:
            incorrect += 1
        else:
            current = display
    if incorrect == 7:
        print("player 456 has been eliminated")
    else:
        print("Go easier on the easygoing you easy-goer")


def words(itn):
    infile = open(itn, "r")
    contents = infile.read()
    return contents.split("\n")


def random_word(ist):
    return ist[randint(0, len(ist) - 1)]


def won(word, letters):
    x = fill(word, letters)
    if word == x:
        return True


def fill(word, letters):
    secret = ["_"] * len(word)
    for letter in letters:
        for i in range(len(word)):
            if letter == word[i]:
                secret[i] = letter
    return "".join(secret)


def main():
    # add other function calls here
    play()
    pass


main()
