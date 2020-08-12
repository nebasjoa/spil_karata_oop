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
        self.promesaj()
        a = random.randint(4, 40)
        deo_za_talon = self.karte[0:a]
        deo_za_deljenje = self.karte[a:]
        talon = []
        # print(deo_za_talon)
        talon.append(random.sample(deo_za_talon, 4))
        print(talon)
        

    def deli(self):
        pass


novi_spil = Spil()
#print(novi_spil.karte)
# novi_spil.podeli()
novi_spil.podeli()

