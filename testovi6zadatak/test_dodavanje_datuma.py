import unittest
from Zadaci.Zadatak6.skripta1 import *


class dodavanje_datuma(unittest.TestCase):

    def setUp(self) -> None:

        self.pocetni= pd.DataFrame(data = [
            ["A", 1, pd.to_datetime('2019-02-06'), 3.0, 0.0],
            ["A", 1, pd.to_datetime('2019-02-07'), 7.0, -10.0],
            ["B", 2, pd.to_datetime('2019-02-09'), 4.0, 0.0],
            ["B", 2, pd.to_datetime('2019-02-10'), 11.0, 0.0],
            ["B", 2, pd.to_datetime('2019-02-12'), 3.0, 0.0]],
             columns = ['ORGJED_SIFRA', 'ARTIKAL_ID', 'DATUM', 'Kolicina_Zaliha', 'Kolicina_Prodaja'])

        self.krajnji = pd.DataFrame(data = [
            ["A", 1, pd.to_datetime("2019-02-06"), 3.0, 0.0],
            ["A", 1, pd.to_datetime("2019-02-07"), 7.0, -10.0],
            ["A", 1, pd.to_datetime("2019-02-08"), 7.0, 0.0],
            ["A", 1, pd.to_datetime("2019-02-09"), 7.0, 0.0],
            ["A", 1, pd.to_datetime("2019-02-10"), 7.0, 0.0],
            ["A", 1, pd.to_datetime("2019-02-11"), 7.0, 0.0],
            ["A", 1, pd.to_datetime("2019-02-12"), 7.0, 0.0],
            ["B", 2, pd.to_datetime("2019-02-06"), 7.0, 0.0],
            ["B", 2, pd.to_datetime("2019-02-07"), 7.0, 0.0],
            ["B", 2, pd.to_datetime("2019-02-08"), 7.0, 0.0],
            ["B", 2, pd.to_datetime("2019-02-09"), 4.0, 0.0],
            ["B", 2, pd.to_datetime("2019-02-10"), 11.0, 0.0],
            ["B", 2, pd.to_datetime("2019-02-11"), 11.0, 0.0],
            ["B", 2, pd.to_datetime("2019-02-12"), 3.0, 0.0]],
            columns = ['ORGJED_SIFRA', 'ARTIKAL_ID', 'DATUM', 'Kolicina_Zaliha', 'Kolicina_Prodaja'])

    def tearDown(self) -> None:
        del self.pocetni
        del self.krajnji

    def test_novi_datumi(self):

        """
        Testiramo da li su dodati svi datumi izmedju najmanjeg i najveceg koji se nalaze u polaznom df
        :return:
        """

        #arrange
        pocetni = self.pocetni
        krajnji_datumi = self.krajnji

        #act

        #resetovali smo indeks jer je datum ostao kao indeks i nismo mogli da ga testiramo
        resenje = dodatni_redovi(pocetni).reset_index()


        #assert
        self.assertTrue(resenje['DATUM'].equals(krajnji_datumi['DATUM']))


    def test_popunjavanje_kolona(self):

        """
        Proveravamo da li su kolone sa novim datumima pravilno popunjene
        :return:
        """
        # arrange
        pocetni = self.pocetni
        krajnji = self.krajnji

        #act
        resenje = dodatni_redovi(pocetni)
        resenje = rad_na_kolonama(resenje).reset_index()

        #assert
        self.assertTrue(resenje.equals(krajnji))
