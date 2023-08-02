import unittest
from zadaci.zadatak6.skripta3 import *
import pandas as pd
class broj_dane_od(unittest.TestCase):

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
                     'POSTOJI_DOPUNA'])

    def tearDown(self) -> None:
        del self.df


    def test_popuni_kolonu(self):

        """
        Test proverava da li je unet tacan broj nula i jedinica u df.
        """

        #arrange
        df_sa_dopunom = self.df
        maska_da_li_ima_dopune = df_sa_dopunom['POSTOJI_DOPUNA'].isna()


        #act
        popunjavanje_kolone_maskom(df_sa_dopunom, 'nova_kolona', maska_da_li_ima_dopune)
        skup = set(df_sa_dopunom['nova_kolona'])


        #assert
        self.assertEqual(df_sa_dopunom['nova_kolona'].sum(), 27)
        self.assertTrue(skup.issubset({0,1}))



    def test_brojac_dana(self):

        """
        Test provereava da li kolona koja se dodaje ispunjava uslove brojenja dana
        """

        #arrange
        niz = pd.DataFrame([1,0,0,0,1,1,0,1,0,0,1])
        resenje = pd.DataFrame([np.NaN,0,0,0,1,2,0,1,0,0,1])

        #act
        kolona = brojac_dana_do_dopune(niz)

        #assert
        self.assertTrue(kolona.equals(resenje))



    def test_dodavanje_kolone_do_poslednje_dopune(self):

        """
        Testiramo da li je u df dodata nova kolona
        """

        #arrange
        df_sa_dopunom = self.df

        #act
        dodaj_br_perioda_do_poslednje_dopune(df_sa_dopunom)

        #assert
        assert 'BROJ_PERIODA_OD_POSLEDNJE_DOPUNE' in df_sa_dopunom.columns
        assert 'pomocna_kolona' not in df_sa_dopunom.columns
        # todo: kako proveriti da li racuna kako treba, pogledaj test za drugi zadatak
