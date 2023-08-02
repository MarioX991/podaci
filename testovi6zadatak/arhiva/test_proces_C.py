from unittest import TestCase
import pandas as pd
import numpy as np
from zadatak2.zadatak2 import broj_uzastopnih_jedinica
from zadatak6.C_od_poslednje_dopune import od_poslednje_dopune

desired_width = 320

pd.set_option('display.width', desired_width)

np.set_printoptions(linewidth=desired_width)

pd.set_option('display.max_columns', 100)

class TestZadatak6C(TestCase):
    """
    Ova klasa sluzi za testiranje zadatka 6 deo C_od_poslednje_dopune.
    """

    def setUp(self) -> None:
        """
        Ovo je deo datafrejma dr_max koji je prosao kroz proces B,
        odnosno sadrzi kolonu 'Postoji_Dopuna'.
        """
        self.df = pd.DataFrame([
            [49378, '15001P', pd.to_datetime('2019-02-06'), 7, 0, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-07'), 7, 0, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-08'), 7, 0, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-09'), 7, 0, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-10'), 7, 0, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-11'), 7, 0, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-12'), 7, 0, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-13'), 7, 0, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-14'), 7, 0, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-15'), 7, 0, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-16'), 7, 0, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-17'), 7, 0, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-18'), 6, 1, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-19'), 5, 1, np.nan],
            [49378, '15001P', pd.to_datetime('2019-02-20'), 10, 0, 5.],
            [49378, '15001P', pd.to_datetime('2019-02-21'), 10, 0, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-06'), 0, 0, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-07'), 19, 0, 19.],
            [49378, '15002P', pd.to_datetime('2019-02-08'), 19, 0, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-09'), 19, 0, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-10'), 19, 0, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-11'), 19, 0, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-12'), 19, 1, 1.],
            [49378, '15002P', pd.to_datetime('2019-02-13'), 19, 1, 1.],
            [49378, '15002P', pd.to_datetime('2019-02-14'), 18, 1, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-15'), 15, 3, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-15'), 15, 3, 3.],
            [49378, '15002P', pd.to_datetime('2019-02-17'), 15, 0, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-18'), 15, 0, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-19'), 15, 0, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-20'), 15, 0, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-21'), 15, 0, np.nan]
        ],
            columns=['ORGJED_SIFRA', 'ARTIKAL_ID', 'DATUM', 'Kolicina_Zaliha', 'Kolicina_Prodaja',
                     'Postoji_Dopuna'])


    def tearDown(self) -> None:
        del self.df


    def test_od_poslednje_dopune(self):
        """
        Test za funkciju od_posjednje_dopune.
        Proverava da li je dodata kolona 'BROJ_PERIODA_OD_POSLEDNJE_DOPUNE'
        i da li je dobro popunjena.
        """

        df = od_poslednje_dopune(self.df)

        print(df.drop(['Kolicina_Zaliha', 'Kolicina_Prodaja'], axis=1))

        self.assertTrue('BROJ_PERIODA_OD_POSLEDNJE_DOPUNE' in df.columns)
        self.assertEqual(df.iloc[22]['BROJ_PERIODA_OD_POSLEDNJE_DOPUNE'], 5.)
        self.assertEqual(df['BROJ_PERIODA_OD_POSLEDNJE_DOPUNE'].isnull().sum(), 29)
        self.assertTrue(np.isnan(df.iloc[14]['BROJ_PERIODA_OD_POSLEDNJE_DOPUNE'] ) )

        # self.df.to_csv('dr_max_treci_test.csv')

