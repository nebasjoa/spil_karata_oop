import random


class Spil():
    znakovi = ['karo', 'pik', 'herc', 'tref']
    brojevi = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']
    karte = []

    # konstruktor
    def __init__(self):
        for i in range(len(self.znakovi)):
            for j in range(len(self.brojevi)):
                self.karte.append([self.brojevi[j], self.znakovi[i]])

    def promesaj(self):
        return random.shuffle(self.karte)

    def izvuci_nasumicno(self):
        return self.karte[random.randint(0, 51)]

    def podeli(self):
        a = random.randint(4, 40)
        deo_za_talon = self.karte[0:a]
        deo_za_deljenje = self.karte[a:]
        talon = []
        for i in range(4):
            if deo_za_talon[i] in talon:
                continue
            else:
                talon.append(deo_za_talon[random.randint(0, len(deo_za_talon)-1)])

        print(talon)

    def deli(self):
        pass


novi_spil = Spil()
novi_spil.promesaj()
novi_spil.podeli()

