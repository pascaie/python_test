"""
Gioco di dadi 8100

Numero di giocatori possibili: 1(contro il computer), 2 o 3 (giocatori uno contro l'altro)

Il regolamento è nel file instructions.txt

"""
from time import sleep
from librerie import Player
from librerie import Hand
from librerie import call_instruction

game_on = True
rule_ask = input("Hello There! Welcome to the game of 8100.\n"
                 "Do you know how to play?(y/n)\n")

if rule_ask == "n":
    print("Your ignorance is astounding. Here, read this and learn.\n")
    sleep(0.5)
    call_instruction()

    sleep(5)

sleep(0.5)

play_ask = input("Do you want to play?(y/n)\n")

if play_ask.lower() in "yes":
    game_on = True
elif play_ask.lower() in "no":
    game_on = False
    print("bye")

sleep(1)

while game_on:
    # chiedi numero di giocatori
    players_number = int(input("How many players there are?(from 1 to 3)\n"))

    sleep(1)

    # 1 giocatore vs bot
    if players_number == 1:
        player1 = Player(0, True, False)
        Bot_player = Player(0, False, False)
        p1_hand = Hand(5, 0, True)
        Bot_hand = Hand(5, 0, True)
        print("Proud human, you really think u can beat me?\n")

        sleep(3)

        print("Since i feel generous, I'll let you start.\n")

        sleep(2)

        while not player1.game_status and not Bot_player.game_status:

            print("Player 1, is your turn.\n")
            p1_hand.status = True  # attiva la mano del giocatore di turno

            sleep(1)

            # la mano del giocatore è giocata
            while p1_hand.status:
                p1_throw_result = p1_hand.dicethrow(p1_hand.remaining_dice)  # tiro dei dadi
                print("You threw " + str(p1_hand.remaining_dice) + " dices: " + str(p1_throw_result) + "\n")
                p1_throw = p1_hand.throwpoint(p1_throw_result)  # calcolo del tiro

                sleep(2)

                if not p1_throw[2]:
                    p1_hand.status = False
                    p1_hand.point = 0
                    p1_hand.remaining_dice = 5
                    Bot_hand.status = True
                    print("Sorry, no 1 and no 5. You loose the hand.\n")
                else:
                    print("You got " + str(p1_throw[0]) +
                          " points and u still got " + str(p1_throw[1]) + " dices to throw\n")
                    p1_hand.point = p1_hand.point + p1_throw[0]
                    p1_hand.remaining_dice = p1_throw[1]

                    sleep(2)

                    throw_ask = input("Do you want to keep throwing?(y/n)\n")
                    if throw_ask.lower() in "no":
                        p1_hand.status = False
                        player1.tot_point_calculate(p1_hand.point)
                        p1_hand.point = 0
                        p1_hand.remaining_dice = 5
                        Bot_hand.status = True
                    elif throw_ask.lower() in "yes":
                        sleep(2)
                        print("Ok. Good Luck!\n")
                        sleep(1)

            sleep(1)

            print("Player 1, now you have " + str(player1.tot_point) + " points\n")

            sleep(1)

            print("Now it's my turn.\n")

            sleep(3)

            if player1.tot_point >= 8100:
                print("Congratulations!! I allowed you to win! You are welcome.\n")
                player1.game_status = True
                p1_hand.status = False
                Bot_hand.status = False

            # Turno del computer
            while Bot_hand.status:
                bot_throw_result = Bot_hand.dicethrow(Bot_hand.remaining_dice)  # tiro dei dadi
                print("I threw " + str(Bot_hand.remaining_dice) + " dices: " + str(bot_throw_result) + "\n")
                bot_throw = p1_hand.throwpoint(bot_throw_result)  # calcolo del tiro

                sleep(2)

                if not bot_throw[2]:
                    Bot_hand.status = False
                    Bot_hand.point = 0
                    Bot_hand.remaining_dice = 5
                    p1_hand.status = True
                    print("Damn. Unlucky throw. Neither a 1 or a 5. Your turn.\n")
                else:
                    print("I got " + str(
                        bot_throw[0]) + " points and I still got " + str(bot_throw[1]) + " dices to throw\n")
                    Bot_hand.point = Bot_hand.point + bot_throw[0]
                    Bot_hand.remaining_dice = bot_throw[1]

                    sleep(2)

                    if Bot_hand.point <= 300 and Bot_hand.remaining_dice < 5:
                        print("This amount of point does not satisfy me. I will keep throwing\n")
                    elif Bot_hand.remaining_dice == 5:
                        print("Surely i wont stop whit 5 new dices to throw.\n")
                    elif Bot_hand.point > 600 and Bot_hand.remaining_dice <= 2:
                        print("mmm... I think this is a pretty good amount to stop. Your turn\n")
                        Bot_hand.status = False
                        Bot_player.tot_point_calculate(Bot_hand.point)
                        Bot_hand.point = 0
                        Bot_hand.remaining_dice = 5
                    elif 600 < Bot_hand.point < 1200 and Bot_hand.remaining_dice > 2:
                        print("my luck isn't exhausted yet. Still going Baby.\n")
                    elif Bot_hand.point > 1200 and Bot_hand.remaining_dice > 3:
                        print("This is what I like. And I want more.\n")
                    elif 1200 < Bot_hand.point < 1800 and Bot_hand.remaining_dice > 4:
                        print("Push the luck. Another throw.\n")
                    else:
                        print("Ok. I think i'm stopping here. Good luck to you, human.\n")
                        Bot_hand.status = False
                        Bot_player.tot_point_calculate(Bot_hand.point)
                        Bot_hand.point = 0
                        Bot_hand.remaining_dice = 5
                        p1_hand.status = True
            sleep(2)

            print("Now i have " + str(Bot_player.tot_point) + " points\n")

            sleep(1)

            if Bot_player.tot_point >= 8100:
                print("This means that, as i predicted, you lose.\n\nLike if you could have done anything else ...")
                Bot_player.game_status = True
                p1_hand.status = False
                Bot_hand.status = False
                sleep(0.5)

        if Bot_player.game_status:
            play_ask = input("I had fun. Do you want to play again?(y/n)\n")
            if play_ask in "no":
                sleep(1)
                print("So goodbye, loser...")
                sleep(2)
                game_on = False

            if play_ask in "yes":
                sleep(1)
                print("Just a little advice: train yourself playing against some other shitty human "
                      "before trying again to challenge ME.")
                sleep(3)

        if player1.game_status:
            play_ask = input("This is pure luck. Play again and i will demonstrate you what i mean.\n"
                             "Play Again?(y/n)")
            if play_ask in "no":
                sleep(1)
                print("Coward")
                sleep(2)
                game_on = False
            elif play_ask in "yes":
                sleep(1)
                print("So now choose: do you want to challenge me again and loose or you want to play with some other"
                      " human in a friendly game?")
                sleep(2)

    # 2 giocatori umani 1 vs 1
    elif players_number == 2:
        print("OK! Game on.\n")
        player1 = Player(0, True, False)
        player2 = Player(0, False, False)
        p1_hand = Hand(5, 0, True)
        p2_hand = Hand(5, 0, False)
        sleep(1)

        while not player1.game_status and not player2.game_status:

            print("Player 1, is your turn.\n")
            p1_hand.status = True  # attiva la mano del giocatore di turno

            sleep(1)

            # la mano del giocatore è giocata
            while p1_hand.status:
                p1_throw_result = p1_hand.dicethrow(p1_hand.remaining_dice)  # tiro dei dadi
                print("You threw " + str(p1_hand.remaining_dice) + " dices: " + str(p1_throw_result) + "\n")
                p1_throw = p1_hand.throwpoint(p1_throw_result)  # calcolo del tiro

                sleep(2)

                if not p1_throw[2]:
                    p1_hand.status = False
                    p1_hand.point = 0
                    p1_hand.remaining_dice = 5
                    p2_hand.status = True
                    print("Sorry, no 1 and no 5. You loose the hand.\n")
                else:
                    print("You got " + str(p1_throw[0]) +
                          " points and u still got " + str(p1_throw[1]) + " dices to throw\n")
                    p1_hand.point = p1_hand.point + p1_throw[0]
                    p1_hand.remaining_dice = p1_throw[1]

                    sleep(2)

                    throw_ask = input("Do you want to keep throwing?(y/n)\n")
                    if throw_ask.lower() in "no":
                        p1_hand.status = False
                        player1.tot_point_calculate(p1_hand.point)
                        p1_hand.point = 0
                        p1_hand.remaining_dice = 5
                        p2_hand.status = True
                    elif throw_ask.lower() in "yes":
                        sleep(2)
                        print("Ok. Good Luck!\n")
                        sleep(1)

            sleep(1)

            print("Player 1, now you have " + str(player1.tot_point) + " points\n")

            if player1.tot_point >= 8100:
                print("Congratulations Player 1!! You thrashed your opponent. He must be really bad at this game.\n")
                player1.game_status = True
                p1_hand.status = False
                p2_hand.status = False

            sleep(1)

            print("Player 2, is your turn now.\n")

            sleep(2)

            while p2_hand.status:
                p2_throw_result = p2_hand.dicethrow(p2_hand.remaining_dice)  # tiro dei dadi
                print("You threw " + str(p2_hand.remaining_dice) + " dices: " + str(p2_throw_result) + "\n")
                p2_throw = p2_hand.throwpoint(p2_throw_result)  # calcolo del tiro

                sleep(2)

                if not p2_throw[2]:
                    p2_hand.status = False
                    p2_hand.point = 0
                    p2_hand.remaining_dice = 5
                    p1_hand.status = True
                    print("Sorry, no 1 and no 5. You loose the hand.\n")
                else:
                    print("You got " + str(p2_throw[0]) +
                          " points and u still got " + str(p2_throw[1]) + " dices to throw\n")
                    p2_hand.point = p2_hand.point + p2_throw[0]
                    p2_hand.remaining_dice = p2_throw[1]

                    sleep(2)

                    throw_ask = input("Do you want to keep throwing?(y/n)\n")
                    if throw_ask.lower() in "no":
                        p2_hand.status = False
                        player2.tot_point_calculate(p2_hand.point)
                        p2_hand.point = 0
                        p2_hand.remaining_dice = 5
                        p1_hand.status = True
                    elif throw_ask.lower() in "yes":
                        sleep(2)
                        print("Ok. Good Luck!\n")
                        sleep(1)

            sleep(1)

            print("Player 2, now you have " + str(player2.tot_point) + " points\n")

            if player2.tot_point >= 8100:
                print("Congratulations Player 2!! You crashed him."
                      " Although I'm pretty sure Player 1 was not much of a challenge.\n")
                player2.game_status = True
                p1_hand.status = False
                p2_hand.status = False

            sleep(1)

        if player2.game_status:
            play_ask = input("If you have fun, why don't you play another game?(y/n)\n")
            if play_ask in "no":
                sleep(1)
                print("So goodbye, losers...")
                sleep(2)
                game_on = False

            elif play_ask in "yes":
                sleep(1)
                print("If someone of you two is up for a challenge, i'm here to thrash him.\n" +
                      str(sleep(0.5)) +
                      "Otherwise keep playing between you humans. I don't care.\n")
                sleep(2)

        elif player1.game_status:
            play_ask = input("If you have fun, why don't you play another game?(y/n)\n")
            if play_ask in "no":
                sleep(1)
                print("So goodbye, losers...")
                sleep(2)
                game_on = False

            elif play_ask in "yes":
                sleep(1)
                print("If someone of you two is up for a challenge, i'm here to thrash him.\n" +
                      str(sleep(0.5)) +
                      "Otherwise keep playing between you humans. I don't care.\n")
                sleep(2)

    # 3 giocatori umani 1 vs 1 vs 1
    elif players_number == 3:
        print("OK! Game on.\n")
        player1 = Player(0, True, False)
        player2 = Player(0, False, False)
        player3 = Player(0, False, False)
        p1_hand = Hand(5, 0, True)
        p2_hand = Hand(5, 0, False)
        p3_hand = Hand(5, 0, False)
        sleep(1)

        while not player1.game_status and not player2.game_status:

            print("Player 1, is your turn.\n")
            p1_hand.status = True  # attiva la mano del giocatore di turno

            sleep(1)

            # la mano del giocatore è giocata
            while p1_hand.status:
                p1_throw_result = p1_hand.dicethrow(p1_hand.remaining_dice)  # tiro dei dadi
                print("You threw " + str(p1_hand.remaining_dice) + " dices: " + str(p1_throw_result) + "\n")
                p1_throw = p1_hand.throwpoint(p1_throw_result)  # calcolo del tiro

                sleep(2)

                if not p1_throw[2]:
                    p1_hand.status = False
                    p1_hand.point = 0
                    p1_hand.remaining_dice = 5
                    p2_hand.status = True
                    print("Sorry, no 1 and no 5. You loose the hand.\n")
                else:
                    print("You got " + str(p1_throw[0]) +
                          " points and u still got " + str(p1_throw[1]) + " dices to throw\n")
                    p1_hand.point = p1_hand.point + p1_throw[0]
                    p1_hand.remaining_dice = p1_throw[1]

                    sleep(2)

                    throw_ask = input("Do you want to keep throwing?(y/n)\n")
                    if throw_ask.lower() in "no":
                        p1_hand.status = False
                        player1.tot_point_calculate(p1_hand.point)
                        p1_hand.point = 0
                        p1_hand.remaining_dice = 5
                        p2_hand.status = True
                    elif throw_ask.lower() in "yes":
                        sleep(2)
                        print("Ok. Good Luck!\n")
                        sleep(1)

            sleep(1)

            print("Player 1, now you have " + str(player1.tot_point) + " points\n")

            if player1.tot_point >= 8100:
                print("Congratulations Player 1!! You emerged victorious from the competition."
                      " They must be really bad at this game.\n")
                player1.game_status = True
                p1_hand.status = False
                p2_hand.status = False
                p3_hand.status = False

            sleep(1)

            print("Player 2, is your turn now.\n")

            sleep(2)

            while p2_hand.status:
                p2_throw_result = p2_hand.dicethrow(p2_hand.remaining_dice)  # tiro dei dadi
                print("You threw " + str(p2_hand.remaining_dice) + " dices: " + str(p2_throw_result) + "\n")
                p2_throw = p2_hand.throwpoint(p2_throw_result)  # calcolo del tiro

                sleep(2)

                if not p2_throw[2]:
                    p2_hand.status = False
                    p2_hand.point = 0
                    p2_hand.remaining_dice = 5
                    p3_hand.status = True
                    print("Sorry, no 1 and no 5. You loose the hand.\n")
                else:
                    print("You got " + str(p2_throw[0]) +
                          " points and u still got " + str(p2_throw[1]) + " dices to throw\n")
                    p2_hand.point = p2_hand.point + p2_throw[0]
                    p2_hand.remaining_dice = p2_throw[1]

                    sleep(2)

                    throw_ask = input("Do you want to keep throwing?(y/n)\n")
                    if throw_ask.lower() in "no":
                        p2_hand.status = False
                        player2.tot_point_calculate(p2_hand.point)
                        p2_hand.point = 0
                        p2_hand.remaining_dice = 5
                        p3_hand.status = True
                    elif throw_ask.lower() in "yes":
                        sleep(2)
                        print("Ok. Good Luck!\n")
                        sleep(1)

            sleep(1)

            print("Player 2, now you have " + str(player2.tot_point) + " points\n")

            if player2.tot_point >= 8100:
                print("Congratulations Player 2!! You win this one."
                      " Now be kind and offer your opponents some tissues, because I hear them crying.\n")
                player2.game_status = True
                p1_hand.status = False
                p2_hand.status = False
                p3_hand.status = False

            sleep(1)

            print("Player 3, is your turn now.\n")

            sleep(2)

            while p3_hand.status:
                p3_throw_result = p3_hand.dicethrow(p3_hand.remaining_dice)  # tiro dei dadi
                print("You threw " + str(p3_hand.remaining_dice) + " dices: " + str(p3_throw_result) + "\n")
                p3_throw = p3_hand.throwpoint(p3_throw_result)  # calcolo del tiro

                sleep(2)

                if not p3_throw[2]:
                    p3_hand.status = False
                    p3_hand.point = 0
                    p3_hand.remaining_dice = 5
                    p1_hand.status = True
                    print("Sorry, no 1 and no 5. You loose the hand.\n")
                else:
                    print("You got " + str(p3_throw[0]) +
                          " points and u still got " + str(p3_throw[1]) + " dices to throw\n")
                    p3_hand.point = p3_hand.point + p3_throw[0]
                    p3_hand.remaining_dice = p3_throw[1]

                    sleep(2)

                    throw_ask = input("Do you want to keep throwing?(y/n)\n")
                    if throw_ask.lower() in "no":
                        p3_hand.status = False
                        player3.tot_point_calculate(p3_hand.point)
                        p3_hand.point = 0
                        p3_hand.remaining_dice = 5
                        p1_hand.status = True
                    elif throw_ask.lower() in "yes":
                        sleep(2)
                        print("Ok. Good Luck!\n")
                        sleep(1)

            sleep(1)

            print("Player 3, now you have " + str(player3.tot_point) + " points\n")

            if player3.tot_point >= 8100:
                print("Congratulations Player 3!! You crashed them." +
                      str(sleep(0.5)) +
                      " It was fairly easy, wasn't it?.\n")
                player3.game_status = True
                p1_hand.status = False
                p2_hand.status = False
                p3_hand.status = False

            sleep(1)

        if player2.game_status:
            play_ask = input("If you have fun, why don't you play another game?(y/n)\n")
            if play_ask in "no":
                sleep(1)
                print("So goodbye, losers...")
                sleep(2)
                game_on = False

            elif play_ask in "yes":
                sleep(1)
                print("If someone of you two is up for a challenge, i'm here to thrash him.\n" +
                      str(sleep(0.5)) +
                      "Otherwise keep playing between you humans. I don't care.\n")
                sleep(2)

        elif player1.game_status:
            play_ask = input("If you have fun, why don't you play another game?(y/n)\n")
            if play_ask in "no":
                sleep(1)
                print("So goodbye, losers...")
                sleep(2)
                game_on = False

            elif play_ask in "yes":
                sleep(1)
                print("If someone of you two is up for a challenge, i'm here to thrash him.\n" +
                      str(sleep(0.5)) +
                      "Otherwise keep playing between you humans. I don't care.\n")
                sleep(2)

        elif player3.game_status:
            play_ask = input("If you have fun, why don't you play another game?(y/n)\n")
            if play_ask in "no":
                sleep(1)
                print("So goodbye, losers...")
                sleep(2)
                game_on = False

            elif play_ask in "yes":
                sleep(1)
                print("If someone of you two is up for a challenge, i'm here to thrash him.\n" +
                      str(sleep(0.5)) +
                      "Otherwise keep playing between you humans. I don't care.\n")
                sleep(2)
