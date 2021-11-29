from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoskori = []

    def tavaroita_korissa(self):
        self.tavaroita = 0
        for ostos in self.ostoskori:
            self.tavaroita += ostos.lukumaara()
        return self.tavaroita

    def hinta(self):
        self._hinta = 0
        for ostos in self.ostoskori:
            self._hinta += ostos.hinta()
        return self._hinta

    def lisaa_tuote(self, lisattava: Tuote):
        self.loytyy = False
        for ostos in self.ostoskori:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                self.loytyy = True
                ostos.muuta_lukumaaraa(1)
        if self.loytyy == False:
            self.ostoskori.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.ostoskori:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() == 0:
                    self.ostoskori.pop()
            else:
                return
            

    def tyhjenna(self):
        self.ostoskori.clear()

    def ostokset(self):
        return self.ostoskori
