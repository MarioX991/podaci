"""
Ovde integracioni test za svaku kontrolnu skriptu

"""

from unittest import TestCase

import pandas as pd

from zadaci.zadatak6.skripta1 import dodatni_redovi


class TestZadatak6A(TestCase):
    """
    Ova klasa sluzi za testiranje zadatka 6 deo A_dodavanje_datuma.
    """

    def setUp(self) -> None:
        """
        Pravi se data frejm za testiranje zadatka 6A dodavalje datuma.
        Datafrejm je otprilike deo datafrejma dr_max
        Pokriva jednu sifru i dva ID-a.
        Unija datuma predstavlja sve datume od prvog do poslednjeg
        koji se pojavljuje, bez jednog preskocenog - 16.2.
        Ubacena je negativna vrednost u treci red.
        Nije sortiran po datumima na poslednja dva mesta, ostalo jeste.
        """


        self.pocetni = pd.DataFrame([
            [49378, '15001P', pd.to_datetime('2019-02-06'), 7.0, 0.0],
            [49378, '15001P', pd.to_datetime('2019-02-07'), 7.0, 0.0],
            [49378, '15001P', pd.to_datetime('2019-02-08'), 7.0, -10.0],
            [49378, '15001P', pd.to_datetime('2019-02-09'), 7.0, 0.0],
            [49378, '15001P', pd.to_datetime('2019-02-17'), 7.0, 0.0],
            [49378, '15001P', pd.to_datetime('2019-02-18'), 6.0, 1.0],
            [49378, '15001P', pd.to_datetime('2019-02-19'), 5.0, 1.0],
            [49378, '15001P', pd.to_datetime('2019-02-20'), 10.0, 0.0],
            [49378, '15001P', pd.to_datetime('2019-02-21'), 10.0, 0.0],

            [49378, '15002P', pd.to_datetime('2019-02-07'), 19.0, 0.0],
            [49378, '15002P', pd.to_datetime('2019-02-08'), 19.0, 0.0],
            [49378, '15002P', pd.to_datetime('2019-02-09'), 19.0, 0.0],
            [49378, '15002P', pd.to_datetime('2019-02-10'), 19.0, 0.0],
            [49378, '15002P', pd.to_datetime('2019-02-11'), 19.0, 0.0],
            [49378, '15002P', pd.to_datetime('2019-02-12'), 19.0, 1.0],
            [49378, '15002P', pd.to_datetime('2019-02-13'), 19.0, 1.0],
            [49378, '15002P', pd.to_datetime('2019-02-15'), 15.0, 3.0],
            [49378, '15002P', pd.to_datetime('2019-02-14'), 18.0, 1.0],

        ],
            columns=['ORGJED_SIFRA', 'ARTIKAL_ID', 'DATUM', 'Kolicina_Zaliha', 'Kolicina_Prodaja'])

        self.krajnji = pd.DataFrame([
            [49378, '15001P', pd.to_datetime('2019-02-06'), 7.0, 0.0],
            [49378, '15001P', pd.to_datetime('2019-02-07'), 7.0, 0.0],
            [49378, '15001P', pd.to_datetime('2019-02-08'), 7.0, 0.0],
            [49378, '15001P', pd.to_datetime('2019-02-09'), 7.0, 0.0],
            [49378, '15001P', pd.to_datetime('2019-02-10'), 7.0, 0.0],
            [49378, '15001P', pd.to_datetime('2019-02-11'), 7.0, 0.0],
            [49378, '15001P', pd.to_datetime('2019-02-12'), 7.0, 0.0],
            [49378, '15001P', pd.to_datetime('2019-02-13'), 7.0, 0.0],
            [49378, '15001P', pd.to_datetime('2019-02-14'), 7.0, 0.0],
            [49378, '15001P', pd.to_datetime('2019-02-15'), 7.0, 0.0],
            [49378, '15001P', pd.to_datetime('2019-02-16'), 7.0, 0.0],
            [49378, '15001P', pd.to_datetime('2019-02-17'), 7.0, 0.0],
            [49378, '15001P', pd.to_datetime('2019-02-18'), 6.0, 1.0],
            [49378, '15001P', pd.to_datetime('2019-02-19'), 5.0, 1.0],
            [49378, '15001P', pd.to_datetime('2019-02-20'), 10.0, 0.0],
            [49378, '15001P', pd.to_datetime('2019-02-21'), 10.0, 0.0],
            [49378, '15002P', pd.to_datetime('2019-02-06'), 0.0, 0.0],
            [49378, '15002P', pd.to_datetime('2019-02-07'), 19.0, 0.0],
            [49378, '15002P', pd.to_datetime('2019-02-08'), 19.0, 0.0],
            [49378, '15002P', pd.to_datetime('2019-02-09'), 19.0, 0.0],
            [49378, '15002P', pd.to_datetime('2019-02-10'), 19.0, 0.0],
            [49378, '15002P', pd.to_datetime('2019-02-11'), 19.0, 0.0],
            [49378, '15002P', pd.to_datetime('2019-02-12'), 19.0, 1.0],
            [49378, '15002P', pd.to_datetime('2019-02-13'), 19.0, 1.0],
            [49378, '15002P', pd.to_datetime('2019-02-14'), 18.0, 1.0],
            [49378, '15002P', pd.to_datetime('2019-02-15'), 15.0, 3.0],
            [49378, '15002P', pd.to_datetime('2019-02-16'), 15.0, 0.0],
            [49378, '15002P', pd.to_datetime('2019-02-17'), 15.0, 0.0],
            [49378, '15002P', pd.to_datetime('2019-02-18'), 15.0, 0.0],
            [49378, '15002P', pd.to_datetime('2019-02-19'), 15.0, 0.0],
            [49378, '15002P', pd.to_datetime('2019-02-20'), 15.0, 0.0],
            [49378, '15002P', pd.to_datetime('2019-02-21'), 15.0, 0.0]
        ],
            columns=['ORGJED_SIFRA', 'ARTIKAL_ID', 'DATUM', 'Kolicina_Zaliha', 'Kolicina_Prodaja'])




    def tearDown(self) -> None:
        del self.pocetni
        del self.krajnji


    def test_dodavanje_datuma(self):
        """
        Test funkcije dodavanje datuma.
        """
        # Arrange
        df_pocetni = self.pocetni
        df_tacni = self.krajnji

        # Act
        df_promenjeni = dodatni_redovi(df_pocetni)
        df_promenjeni.reset_index(inplace=True)

        # Assert
        print(df_promenjeni)

        self.assertTrue(df_tacni.equals(df_promenjeni))



