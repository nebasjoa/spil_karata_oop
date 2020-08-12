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
        karte_i1 = []
        karte_i2 = []
        talon = []
        talon.append(random.sample(deo_za_talon, 4))
        karte_i1.append(random.sample(deo_za_deljenje, 6))
        deo_za_deljenje = [x for x in deo_za_deljenje if x not in karte_i1[0]]
        karte_i2.append(random.sample(deo_za_deljenje, 6))
        deo_za_deljenje = [x for x in deo_za_deljenje if x not in karte_i2[0]]
        deo_za_talon = [x for x in deo_za_talon if x not in talon[0]]
        ostale_karte = deo_za_deljenje + deo_za_talon


if __name__ == "__main__":
    novi_spil = Spil()
    novi_spil.podeli()

