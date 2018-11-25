from random import *

parole_possibili = {
    1: "barbagianni",
    2: "onomatopea",
    3: "scientifico",
    4: "assurbanipal",
    5: "postribolo",
    6: "ricchione",
    7: "marcescente",
    8: "porticato",
    9: "mineralogia",
    10: "assurdo"
}
risp = 'y'

while risp != 'n':
    risp = input("Do you wanna play the hangman?(y/n)\n")

    if risp != 'n' and risp != 'y':
        print("sorry, seems like u can't read. Only y or n are allowed as answer.")

    elif risp == 'n':
        print("vabbuò. Cià")

    elif risp == 'y':

        print("So let's play.")
        word = parole_possibili[randint(1, 10)]
        word_lenght = len(word)
        print("Here is the word. Every + is a vowel and every - is a consonant")
        i = 0
        hidden_word = []

        while i < word_lenght:

            if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u':
                hidden_word.append("+")

            else:
                hidden_word.append("-")
            i = i + 1
        hidden_print = ""

        for index2 in hidden_word:
            hidden_print = hidden_print + index2
        print(hidden_print)

        error_count = 0
        error_limit = 8
        lose_game = False
        win_game = False
        status = True

        while not lose_game and not win_game:
            if status:
                if error_count == 0:
                    print("You still got " + str(error_limit - error_count) + " error left")
                elif error_count == 1:
                    print("  \n"
                          "|     \n"
                          "|     \n"
                          "|    \n"
                          "|      \n"
                          "|      \n"
                          "|_\n")
                elif error_count == 2:
                    print(" ______\n"
                          "|     \n"
                          "|      \n"
                          "|    \n"
                          "|    \n"
                          "|     \n"
                          "|_\n")
                elif error_count == 3:
                    print("______ \n"
                          "|    |  \n"
                          "|    o  \n"
                          "|    \n"
                          "|     \n"
                          "|      \n"
                          "|_\n")
                if error_count == 4:
                    print("______ \n"
                          "|    |  \n"
                          "|    o  \n"
                          "|    | \n"
                          "|    |  \n"
                          "|      \n"
                          "|_\n")
                if error_count == 5:
                    print("______ \n"
                          "|    |  \n"
                          "|    o  \n"
                          "|   /| \n"
                          "|    |  \n"
                          "|      \n"
                          "|_\n")
                if error_count == 6:
                    print("______ \n"
                          "|    |  \n"
                          "|    o  \n"
                          "|   /|\ \n"
                          "|    |  \n"
                          "|      \n"
                          "|_\n")
                if error_count == 7:
                    print("______ \n"
                          "|    |  \n"
                          "|    o  \n"
                          "|   /|\ \n"
                          "|    |  \n"
                          "|   /   \n"
                          "|_\n")

            risp2 = input("Do you want to ask for a letter?(y/n)")

            if risp2 == 'n':
                Answer = input("So do you want to try to guess the word? Fine. Try it:")

                if Answer == word:
                    print("Correct! You win!")
                    win_game = True

                else:
                    print("Nope. Try again next time")
                    error_count = error_count + 1

            elif risp2 == 'y':
                letter = input("What letter are you looking for?\n")
                index3 = 0
                control = False

                for word_letter in word:

                    if letter == word_letter:
                        hidden_word[index3] = letter
                        control = True
                    index3 = index3 + 1

                if control:
                    print("There is. Here is the word now.")
                    hidden_print = ""

                    for index2 in hidden_word:
                        hidden_print = hidden_print + index2
                    print(hidden_print)
                    status = False

                else:
                    print("There is no such letter. U got an error.")
                    error_count = error_count + 1
                    status = True

            if error_count == error_limit:
                lose_game = True

        if lose_game:
            print("______ \n"
                  "|    |  \n"
                  "|    o  \n"
                  "|   /|\ \n"
                  "|    |  \n"
                  "|   / \  \n"
                  "|_\n")
            print("You lose, you dumb idiot. The word was " + word)
