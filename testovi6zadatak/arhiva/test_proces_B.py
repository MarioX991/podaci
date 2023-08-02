from unittest import TestCase
import pandas as pd
import numpy as np
from zadatak6.pomocne_funkcije import menjanje_nepozitivnih_vrednosti_sa_nan
from zadatak6.B_postoji_dopuna import postoji_dopuna

class TestZadatak6B(TestCase):
    """
    Ova klasa sluzi za testiranje zadatka 6 deo B_postoji_dopuna.
    """

    def setUp(self) -> None:
        """
        Deo datafrejma dr_max koji je prosao kroz proces A, odnosno, sadrzi sve potrebne datume.
        """
        self.pocetni = pd.DataFrame([
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

        self.krajnji = pd.DataFrame([
            [49378, '15001P', pd.to_datetime('2019-02-06'), 7., 0., np.nan],
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
            [49378, '15002P', pd.to_datetime('2019-02-16'), 15, 0, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-17'), 15, 0, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-18'), 15, 0, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-19'), 15, 0, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-20'), 15, 0, np.nan],
            [49378, '15002P', pd.to_datetime('2019-02-21'), 15, 0, np.nan]
        ],
            columns=['ORGJED_SIFRA', 'ARTIKAL_ID', 'DATUM', 'Kolicina_Zaliha', 'Kolicina_Prodaja',
                     'Postoji_Dopuna'])



    def tearDown(self) -> None:

        del self.pocetni
        del self.krajnji


    def test_postoji_dopuna(self):
        """
        Test funkcije postoji_dopuna.
        """

        # Arrange
        df_pocetni = self.pocetni
        df_tacni = self.krajnji

        # Act
        df_promenjeni = postoji_dopuna(df_pocetni)

        # Assert
        self.assertTrue(df_tacni.equals(df_promenjeni))


