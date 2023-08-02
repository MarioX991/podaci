import unittest

import numpy as np

from Zadaci.Zadatak6.skripta2 import *


class dodavanje_datuma(unittest.TestCase):

    def setUp(self) -> None:
        self.pocetni = pd.DataFrame(data = [
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


        self.krajnji = pd.DataFrame(data = [
            ["A", 1, pd.to_datetime("2019-02-06"), 3.0, 0.0, np.NaN],
            ["A", 1, pd.to_datetime("2019-02-07"), 7.0, 0.0, 4.0],
            ["A", 1, pd.to_datetime("2019-02-08"), 7.0, 0.0, np.NaN],
            ["A", 1, pd.to_datetime("2019-02-09"), 7.0, 0.0, np.NaN],
            ["A", 1, pd.to_datetime("2019-02-10"), 7.0, 0.0, np.NaN],
            ["A", 1, pd.to_datetime("2019-02-11"), 7.0, 0.0, np.NaN],
            ["A", 1, pd.to_datetime("2019-02-12"), 7.0, 0.0, np.NaN],
            ["B", 2, pd.to_datetime("2019-02-06"), 7.0, 0.0, np.NaN],
            ["B", 2, pd.to_datetime("2019-02-07"), 7.0, 0.0, np.NaN],
            ["B", 2, pd.to_datetime("2019-02-08"), 7.0, 0.0, np.NaN],
            ["B", 2, pd.to_datetime("2019-02-09"), 4.0, 0.0, np.NaN],
            ["B", 2, pd.to_datetime("2019-02-10"), 11.0, 0.0, 7.0],
            ["B", 2, pd.to_datetime("2019-02-11"), 11.0, 0.0, np.NaN],
            ["B", 2, pd.to_datetime("2019-02-12"), 3.0, 0.0, np.NaN]],
            columns = ['ORGJED_SIFRA', 'ARTIKAL_ID', 'DATUM', 'Kolicina_Zaliha', 'Kolicina_Prodaja', 'POSTOJI_DOPUNA'])


    def test_negativne_u_nulu(self):

        #arrange
        pocetni = self.pocetni

        #act
        resenje = negativne_vresnoti_u_nulu(pocetni)

        #assert
        self.assertEqual(resenje['Kolicina_Prodaja'].iloc[1], 0)

    def test_kolona_dopune(self):

        #arrange
        pocetni = self.pocetni
        krajnji = self.krajnji

        #act
        resenje = negativne_vresnoti_u_nulu(pocetni)
        resenje = kreiranje_kolone_postoji_dopuna(resenje)

        #assert
        assert 'POSTOJI_DOPUNA' in resenje.columns
        assert 'Razlika_u_kolicini_zaliha' not in resenje.columns
        self.assertTrue(resenje.equals(krajnji))