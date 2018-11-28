"""
Libreria di classi e metodi definiti per il gioco 8100

"""
from pathlib import Path
import random


# definizione del giocatore
class Player:
    def __init__(self, tot_point, hand_status, game_status):
        self.tot_point = tot_point   # punti totali
        self.hand_status = hand_status  # stato della mano in gioco
        self.game_status = game_status  # stato della partita (vincente o no)

    #definisce quando la mano è finita
    def control_hand(self, status):
        if status == False:
            self.hand_status = False

    #
    def tot_point_calculate(self, handpoint):
        self.tot_point = self.tot_point + handpoint

    def game_winning(self):
        self.game_status = True


# definizione della mano
class Hand:
    def __init__(self, remaining_dice, point, status):
        total_dice = 5
        self.remaining_dice = remaining_dice # dadi rimasti
        self.point = point  # punti accumulati
        self.status = status # stato della mano (true=giocabile, false=persa)

    # Funzione che tira un certo numero di dadi e ritorna il risultato dei tiri
    def dicethrow(self, remaining_dice):
        dices = []
        for dicenumber in range(0, remaining_dice):
            dices.append(random.randint(1, 6))
        return dices

    # Funzione che conta il punteggio di ogni tiro e ritorna punteggio, dadi restanti e validità o meno del tiro
    def throwpoint(self, dices: list):
        dices.sort()
        throw_point = 0
        throw_status = True
        if dices == [1, 2, 3, 4, 5] or dices == [2, 3, 4, 5, 6]:
            throw_point = throw_point + 500
            dices.clear()
        elif dices.count(1) >= 3:
            throw_point = throw_point + 1000
            dices.sort(reverse=True)
            for a in range(3):
                dices.pop()
        elif dices.count(2) >= 3:
            throw_point = throw_point + 200
            dices.sort(reverse=True)
            for a in range(3):
                dices.pop()
        elif dices.count(3) >= 3:
            throw_point = throw_point + 300
            dices.sort(reverse=True)
            for a in range(3):
                dices.pop()
        elif dices.count(4) >= 3:
            throw_point = throw_point + 400
            dices.sort(reverse=True)
            for a in range(3):
                dices.pop()
        elif dices.count(5) >= 3:
            throw_point = throw_point + 500
            dices.sort(reverse=True)
            for a in range(3):
                dices.pop()
        elif dices.count(6) >= 3:
            throw_point = throw_point + 600
            dices.sort(reverse=True)
            for a in range(3):
                dices.pop()
        elif dices.count(1) == 0 and dices.count(5) == 0:
            dices.clear()
            throw_status = False
        while 1 in dices:
            throw_point = throw_point + 100
            dices.remove(1)
        while 5 in dices:
            throw_point = throw_point + 50
            dices.remove(5)
        if not dices: # se non ci sono più dadi, riempie la lista in modo che ce ne siano sempre 5
            dices = [1, 2, 3, 4, 5]
        return throw_point, len(dices), throw_status

    # funzione che domanda se si vuole continuare a tirare i dadi e ritorna la risposta
    def ask_for_throw(self):
        answer = input("Do you wanna throw the remaining dices?(y/n)\n")
        return answer

    # aggiunge i punti fatti nel tiro alla mano
    def calculate_hand_point(self, throw_point):
        self.point = self.point + throw_point


def call_instruction():
    instructions = Path("instructions.txt")
    if instructions.exists():
        instructions_content = open("instructions.txt", "r")
        print(instructions_content.read())
        instructions_content.close()
    else:
        instructions_content = open("instructions.txt", "w")
        instructions_content.write("Welcome to the instructions of 8100.\n"
                                   "It's a simple dice game. You throw 5 dices when is your turn and get some point "
                                   "on the base of what combinations you get.\n"
                                   "Every 5 is worth 50 points, every 1 is worth 100 points.\n"
                                   "A tris is worth 100xdice number. Except a tris of 1 that is worth 1000 points.\n"
                                   "A straight (5 dices on sequence) is worth 500 points.\n"
                                   "Every dice that's not in a combinations can be thrown again; for example if you get"
                                   "a straight you can throw again all 5 dices, instead if you get a tris and a 5"
                                   "only one dice remain to be thrown.\n"
                                   "But beware: if no combinations comes out the hand and every"
                                   " point accumulated until that throw are lost and the player's turn is ended.\n"
                                   "The first player to reach or top 8100 points is the winner.")
        instructions_content.close()
        instructions_content = open("instructions.txt", "r")
        print(instructions_content.read())
        instructions_content.close()
