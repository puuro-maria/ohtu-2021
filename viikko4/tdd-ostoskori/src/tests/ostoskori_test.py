import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 2)
        self.kalja = Tuote("Kalja", 3)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)

    def test_ostoskorin_hinta_lisayksen_jalkeen(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), 2)
    
    def test_ostoskorin_maara_lisayksen_jalkeen(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_ostoskorin_hinta_kahden_eri_lisayksen_jalkeen(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.kalja)
        self.assertEqual(self.kori.hinta(), 5)

    def test_ostoskorin_maara_kahden_eri_lisayksen_jalkeen(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.kalja)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_ostoskorin_maara_kahden_saman_lisayksen_jalkeen(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_ostoskorin_hinta_kahden_saman__lisayksen_jalkeen(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), 2*self.maito.hinta())

    def test_lisayksen_jalkeen_sisaltaa_yhden_tuotteen(self):
        self.kori.lisaa_tuote(self.kalja)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kahden_lisayksen_jalkeen_sisaltaa_tuotteet(self):
        self.kori.lisaa_tuote(self.kalja)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kahden_saman_lisayksen_jalkeen_sisaltaa_yhden_ostoksen(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_lisayksen_jalkeen_sisaltaa_sen_tuotteen(self):
        self.kori.lisaa_tuote(self.kalja)
        self.assertEqual(self.kori.ostokset()[0].tuotteen_nimi(), self.kalja.nimi())

    def test_ostoskorista_poistaminen_toimii(self):
        self.kori.lisaa_tuote(self.kalja)
        self.kori.poista_tuote(self.kalja)
        self.assertEqual(len(self.kori.ostokset()), 0)

    def test_kahden_saman_lisayksen_jalkeen_sisaltaa_kaksi_tuotetta_nimella(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.ostokset()[0].tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_poiston_jalkeen_jaa_yksi_tuote(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.kori.poista_tuote(self.maito)
        self.assertEqual(self.kori.ostokset()[0].tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_tyhjenna_toimii(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.kalja)
        self.kori.tyhjenna()
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
