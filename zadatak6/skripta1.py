import pandas as pd
import numpy as np
import warnings

from pandas import DataFrame

from zadaci.zadatak6.parametri import osnovne_kolne_df, indeksne_kolone1, kolona_datum

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 50)
warnings.filterwarnings("ignore")


def dodatni_redovi(df: pd.DataFrame) -> pd.DataFrame:
    """
     Funkcija dodaje nedostajuci datume u prosledjeni data frejm.
     :param df - Data Frejem
     :retun doupunjen Data Frejm sa dopunjenim datumima.

    """
    datum_min = df[kolona_datum].min()
    #print(datum_min)
    datum_max = df[kolona_datum].max()
    #print(datum_max)
    novi_data_frejm = pd.DataFrame([], columns=df.columns)
    novi_data_frejm.loc[:, 'DATUM'] = pd.date_range(datum_min, datum_max, freq='D')
    novi_data_frejm.loc[:, 'ARTIKAL_ID'] = 9
    novi_data_frejm.loc[:, 'ORGJED_SIFRA'] = 'Z'
    # novi_data_frejm.loc[:, ['Kolicina_Zaliha', 'Kolicina_Prodaja']] = np.nan
    novi_df = pd.concat([df, novi_data_frejm])
    #print(novi_df.shape)
    novi_df = (novi_df.set_index(indeksne_kolone1)
               .unstack()
               .stack(dropna=False)  #
               .drop("Z", axis=0, level=0))

    return novi_df


def rad_na_kolonama(df: pd.DataFrame) -> pd.DataFrame:
    """
    Funkcija se koristi za:
        - null vrednosti u koloni Kolicina_Prodaje se menjaju sa 0
        - vrsi se dopuna vrednosti Kolicina_Zaliha prvom prethodom ne-null vrednoscu
        - Vrendosti za kolonu Kolicina_Zaliha pre prvog pojavljivanja ne-null vrednsoti
          se postavljaju na nule

    param: df
    result df
    """

    df.loc[:, 'Kolicina_Prodaja'].fillna(0, inplace=True)
    df.loc[:, 'Kolicina_Zaliha'].ffill(inplace=True)
    df.loc[:, 'Kolicina_Zaliha'].fillna(0, inplace=True)

    return df


def priprema_kolone_datum_pre_dopune(df: pd.DataFrame) -> pd.DataFrame:
    """
    Funksija pripreme kolonu datum pre samog unosenja nedostajucih podatak.
    Definisemo format datuma i sortiramo kolonu datum.
    """
    df[kolona_datum] = pd.to_datetime(df[kolona_datum], format='%Y-%m-%d')
    df.sort_values(kolona_datum, inplace=True)

    return df


def run(save_file = True):
    """
    broj_kolona -  BROJ KOLONA KOJE ZELIMO DA UCITAMO IZA CELOG FAJLA

    """
    fajl = pd.read_csv(r'../../../../podaci/input-data/test_grupe.csv',
                       usecols=osnovne_kolne_df,
                       )

    assert "DATUM" in fajl.columns, "Kolona DATUM ne postoji u DataFrejm -u!"
    fajl = priprema_kolone_datum_pre_dopune(fajl)
    assert fajl["DATUM"].is_monotonic, "Kolona DATUM nije sortirana"

    fajl = dodatni_redovi(fajl)
    # print(fajl.shape)
    fajl = rad_na_kolonama(fajl).reset_index()
    print(fajl.shape)

    # ceo_fajl = ceo_fajl.groupby(['ORGJED_SIFRA', 'ARTIKAL_ID']).get_group(('15001P', 50501))

    if save_file:
        fajl.to_csv(r'../../../../podaci/internal/A/test_grupe.csv', index=False)
    #


if __name__ == "__main__":
    run()
#     pocetni = pd.DataFrame(data = [
#             ["A", 1, pd.to_datetime('2019-02-06'), 3.0, 0.0],
#             ["A", 1, pd.to_datetime('2019-02-07'), 7.0, -10.0],
#             ["B", 2, pd.to_datetime('2019-02-09'), 4.0, 0.0],
#             ["B", 2, pd.to_datetime('2019-02-10'), 11.0, 0.0],
#             ["B", 2, pd.to_datetime('2019-02-12'), 3.0, 0.0]],
#              columns = ['ORGJED_SIFRA', 'ARTIKAL_ID', 'DATUM', 'Kolicina_Zaliha', 'Kolicina_Prodaja'])
#     resenje = dodatni_redovi(pocetni)
#     resenje = rad_na_kolonama(resenje)
#     print(resenje.head(15))
