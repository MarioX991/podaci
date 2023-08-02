import unittest

import numpy as np
import pandas as pd
from zadaci.zadatak6.skripta4 import *

class broj_dane_do(unittest.TestCase):

    def setUp(self) -> None:
        self.pocenti = pd.DataFrame([
            [49378, '15001P', pd.to_datetime('2019-02-06'), 7, 0, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-07'), 7, 0, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-08'), 7, 0, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-09'), 7, 0, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-10'), 7, 0, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-11'), 7, 0, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-12'), 7, 0, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-13'), 7, 0, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-14'), 7, 0, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-15'), 7, 0, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-16'), 7, 0, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-17'), 7, 0, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-18'), 6, 1, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-19'), 5, 1, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-20'), 10, 0, 5., np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-21'), 10, 0, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-06'), 0, 0, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-07'), 19, 0, 19., np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-08'), 19, 0, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-09'), 19, 19, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-10'), 0, 0, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-11'), 0, 0, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-12'), 19, 1, 1., 5.],
            [49378, '15002P', pd.to_datetime('2019-02-13'), 19, 1, 1., 1.],
            [49378, '15002P', pd.to_datetime('2019-02-14'), 18, 1, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-15'), 15, 15, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-16'), 15, 15, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-17'), 0, 0, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-18'), 15, 0, 15, 5],
            [49378, '15002P', pd.to_datetime('2019-02-19'), 15, 0, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-20'), 15, 15, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-21'), 0, 0, np.nan, np.nan]
        ],
            columns=['ORGJED_SIFRA', 'ARTIKAL_ID', 'DATUM', 'Kolicina_Zaliha', 'Kolicina_Prodaja',
                     'POSTOJI_DOPUNA', "BROJ_PERIODA_OD_POSLEDNJE_DONE"])


        self.krajnji = pd.DataFrame([
            [49378, '15001P', pd.to_datetime('2019-02-06'), 7, 0, np.nan, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-07'), 7, 0, np.nan, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-08'), 7, 0, np.nan, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-09'), 7, 0, np.nan, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-10'), 7, 0, np.nan, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-11'), 7, 0, np.nan, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-12'), 7, 0, np.nan, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-13'), 7, 0, np.nan, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-14'), 7, 0, np.nan, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-15'), 7, 0, np.nan, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-16'), 7, 0, np.nan, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-17'), 7, 0, np.nan, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-18'), 6, 1, np.nan, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-19'), 5, 1, np.nan, np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-20'), 10, 0, 5., np.nan, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-21'), 10, 0, np.nan, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-06'), 0, 0, np.nan, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-07'), 19, 0, 19., np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-08'), 19, 0, np.nan, np.nan, 2.0],
            [49378, '15002P', pd.to_datetime('2019-02-09'), 19, 19, np.nan, np.nan, 1.0],
            [49378, '15002P', pd.to_datetime('2019-02-10'), 0, 0, np.nan, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-11'), 0, 0, np.nan, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-12'), 19, 1, 1., 5., np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-13'), 19, 1, 1., 1., np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-14'), 18, 1, np.nan, np.nan,3.0],
            [49378, '15002P', pd.to_datetime('2019-02-15'), 15, 15, np.nan, np.nan, 2.0],
            [49378, '15002P', pd.to_datetime('2019-02-16'), 15, 15, np.nan, np.nan, 1.0],
            [49378, '15002P', pd.to_datetime('2019-02-17'), 0, 0, np.nan, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-18'), 15, 0, 15, 5, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-19'), 15, 0, np.nan, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-20'), 15, 15, np.nan, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-21'), 0, 0, np.nan, np.nan, np.nan]
        ],
            columns=['ORGJED_SIFRA', 'ARTIKAL_ID', 'DATUM', 'Kolicina_Zaliha', 'Kolicina_Prodaja',
                     'POSTOJI_DOPUNA', "BROJ_PERIODA_OD_POSLEDNJE_DONE", "BROJ_DANA_DO_ISTEKA_ZALIHA"])

    def tearDown(self) -> None:
        del self.pocenti
        del self.krajnji

    def test_brojac_dana(self):
        """
        Test provereava da li kolona koja se dodaje ispunjava uslove brojenja dana
        """

        # arrange
        niz = pd.DataFrame([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1])
        resenje = pd.DataFrame([np.NaN, 0, 0, 0, 1, 2, 0, 1, 0, 0, 1])

        # act
        kolona = brojac_dana_do_dopune(niz)

        # assert
        self.assertTrue(kolona.equals(resenje))



    def test_dodaj_broj_daba_do_isteka_zaliha(self):

        # arrange
        pocetni = self.pocenti
        krajnji = self.krajnji

        # act
        dodaj_broj_daba_do_isteka_zaliha(pocetni)

        # assert
        self.assertTrue(pocetni.equals(krajnji))



















