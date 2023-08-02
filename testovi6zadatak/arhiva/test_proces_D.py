from unittest import TestCase
import pandas as pd
import numpy as np
from zadatak2.zadatak2 import do_sledece_nule
from zadatak6.D_do_nestanka_zaliha import do_nestanka_zaliha
from zadatak6.pomocne_funkcije import *

desired_width = 320

pd.set_option('display.width', desired_width)

np.set_printoptions(linewidth=desired_width)

pd.set_option('display.max_columns', 100)

class TestZadatak6D(TestCase):
    """
    Ova klasa sluzi za testiranje zadatka 6 deo B_postoji_dopuna.
    """

    def setUp(self) -> None:
        """
        Ovo je deo datafrejma dr_max koji je prosao pripremu za glavnu funkciju u D,
        odnosno, sadrzi kolone 'DO_NESTANKA_ZALIHA',  'DO_SLEDECE_DOPUNE',
        'DO_NESTANKA_ZALIHA < DO_SLEDECE_DOPUNE'.
        """

        self.df = pd.DataFrame([
            [49378, '15001P', pd.to_datetime('2019-02-06'), 7, 0, np.nan, np.nan, 16, 14, 0],
            [49378, '15001P', pd.to_datetime('2019-02-07'), 7, 0, np.nan, np.nan, 15, 13, 0],
            [49378, '15001P', pd.to_datetime('2019-02-08'), 7, 0, np.nan, np.nan, 14, 12, 0],
            [49378, '15001P', pd.to_datetime('2019-02-09'), 7, 0, np.nan, np.nan, 13, 11, 0],
            [49378, '15001P', pd.to_datetime('2019-02-10'), 7, 0, np.nan, np.nan, 12, 10, 0],
            [49378, '15001P', pd.to_datetime('2019-02-11'), 7, 0, np.nan, np.nan, 11, 9, 0],
            [49378, '15001P', pd.to_datetime('2019-02-12'), 7, 0, np.nan, np.nan, 10, 8, 0],
            [49378, '15001P', pd.to_datetime('2019-02-13'), 7, 0, np.nan, np.nan, 9, 7, 0],
            [49378, '15001P', pd.to_datetime('2019-02-14'), 7, 0, np.nan, np.nan, 8, 6, 0],
            [49378, '15001P', pd.to_datetime('2019-02-15'), 7, 0, np.nan, np.nan, 7, 5, 0],
            [49378, '15001P', pd.to_datetime('2019-02-16'), 7, 0, np.nan, np.nan, 6, 4, 0],
            [49378, '15001P', pd.to_datetime('2019-02-17'), 7, 0, np.nan, np.nan, 5, 3, 0],
            [49378, '15001P', pd.to_datetime('2019-02-18'), 6, 1, np.nan, np.nan, 4, 2, 0],
            [49378, '15001P', pd.to_datetime('2019-02-19'), 5, 1, np.nan, np.nan, 3, 1, 0],
            [49378, '15001P', pd.to_datetime('2019-02-20'), 10, 0, 5., np.nan, 2, 3,1],
            [49378, '15001P', pd.to_datetime('2019-02-21'), 10, 0, np.nan, np.nan, 1, 2, 1],

            [49378, '15002P', pd.to_datetime('2019-02-06'), 0, 0, np.nan, np.nan, 4, 1, 0],
            [49378, '15002P', pd.to_datetime('2019-02-07'), 19, 0, 19., np.nan, 3, 5, 1],
            [49378, '15002P', pd.to_datetime('2019-02-08'), 19, 0, np.nan, np.nan, 2, 4, 1],
            [49378, '15002P', pd.to_datetime('2019-02-09'), 19, 19, np.nan, np.nan, 1, 3, 1],
            [49378, '15002P', pd.to_datetime('2019-02-10'), 0, 0, np.nan, np.nan, 1, 2, 1],
            [49378, '15002P', pd.to_datetime('2019-02-11'), 0, 0, np.nan, np.nan, 6, 1, 0],
            [49378, '15002P', pd.to_datetime('2019-02-12'), 19, 1, 1., 5., 5, 1, 0],
            [49378, '15002P', pd.to_datetime('2019-02-13'), 19, 1, 1., 1., 4, 5, 1],
            [49378, '15002P', pd.to_datetime('2019-02-14'), 18, 1, np.nan, np.nan, 3, 4, 1],
            [49378, '15002P', pd.to_datetime('2019-02-15'), 15, 15, np.nan, np.nan, 2, 3, 1],
            [49378, '15002P', pd.to_datetime('2019-02-16'), 15, 15, np.nan, np.nan, 1, 2, 1],
            [49378, '15002P', pd.to_datetime('2019-02-17'), 0, 0, np.nan, np.nan, 4, 1, 0],
            [49378, '15002P', pd.to_datetime('2019-02-18'), 15, 0, 15, 5, 3, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-19'), 15, 0, np.nan, np.nan, 2, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-20'), 15, 15, np.nan, np.nan, 1, np.nan, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-21'), 0, 0, np.nan, np.nan, np.nan, np.nan, np.nan]
        ],
            columns=['ORGJED_SIFRA', 'ARTIKAL_ID', 'DATUM', 'Kolicina_Zaliha', 'Kolicina_Prodaja',
                     'Postoji_Dopuna', 'BROJ_PERIODA_OD_POSLEDNJE_DOPUNE', 'DO_NESTANKA_ZALIHA',  'DO_SLEDECE_DOPUNE',
                     'DO_NESTANKA_ZALIHA < DO_SLEDECE_DOPUNE',])



    def tearDown(self) -> None:
        del self.df


    def test_do_nestanka_zaliha(self):
        """
        Test za funkciju do_nestanka_zalihae.
        Proverava da li je dodata kolona 'BROJ_PERIODA_DO_NESTANKA_ZALIHA'
        i da li je dobro popunjena.
        """

        df = do_nestanka_zaliha(self.df)

        print(df.drop([ 'DATUM', 'BROJ_PERIODA_OD_POSLEDNJE_DOPUNE'], axis=1))

        self.assertTrue('BROJ_PERIODA_DO_NESTANKA_ZALIHA' in df.columns)
        self.assertEqual(df.iloc[17]['BROJ_PERIODA_DO_NESTANKA_ZALIHA'], 3.)
        self.assertEqual(df['BROJ_PERIODA_DO_NESTANKA_ZALIHA'].isnull().sum(), 30)