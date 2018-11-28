"""
Libreria di classi e metodi definiti per il gioco 8100

"""

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
        elif dices.count(1) == 3:
            throw_point = throw_point + 1000
            while 1 in dices:
                dices.remove(1)
        elif dices.count(2) == 3:
            throw_point = throw_point + 200
            while 2 in dices:
                dices.remove(2)
        elif dices.count(3) == 3:
            throw_point = throw_point + 300
            while 3 in dices:
                dices.remove(3)
        elif dices.count(4) == 3:
            throw_point = throw_point + 400
            while 4 in dices:
                dices.remove(4)
        elif dices.count(5) == 3:
            throw_point = throw_point + 500
            while 5 in dices:
                dices.remove(5)
        elif dices.count(6) == 3:
            throw_point = throw_point + 600
            while 6 in dices:
                dices.remove(6)
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

