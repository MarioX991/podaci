import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")


def popunjavanje_kolone_maskom(df, kolona, maska):
    assert kolona not in df.columns
    # kada je maska to je true --> 1
    df.loc[maska, kolona] = 1
    df.loc[~maska, kolona] = 0


def brojac_dana_do_dopune(kolona):
    """
    Prvi dan je NaN zbog oduzimanja susednih redova. Prvi dan je stanje takvo kakvo je.
    """
    suma = kolona.cumsum()
    kolona *= suma
    kolona = kolona.diff().where(lambda x: x < 0).fillna(method='ffill')
    kolona += suma
    return kolona


def dodaj_br_perioda_do_poslednje_dopune(df):
    """
    Funkcija prima df sa kolonama koje sadrze informacije o dopunama i kolicini zaliha.
    Na osnovu njih treba da se napravi kolona koja sadrzi informaciju o broju dana do poslednje dopune.
    """
    assert 'POSTOJI_DOPUNA' in df.columns
    assert 'BROJ_PERIODA_OD_POSLEDNJE_DOPUNE' not in df.columns

    # ako nema dopune, taj dan cemo predstaviti jedinicom jer brojimo dan, a dan kada ima dopune nulom
    # u tom slucaju kada radimo kumulativnu sumu, brojacemo dane unapred, koliko ima dana do dopune
    # da bismo dobili u trenutku koliko je proslo dana od poslednje dopune, sve kolone pomeramo unapred za jednu

    maska_do_poslednje_dopune = df['POSTOJI_DOPUNA'].isna()
    popunjavanje_kolone_maskom(df, 'pomocna_kolona', maska_do_poslednje_dopune)

    df.loc[:, 'BROJ_PERIODA_OD_POSLEDNJE_DOPUNE'] = (df.groupby(['ORGJED_SIFRA', 'ARTIKAL_ID'])['pomocna_kolona']
                                                     .apply(brojac_dana_do_dopune))

    df.drop('pomocna_kolona', axis=1, inplace=True)

    return df


def run3():
    pomocna = r'../../../../podaci/internal/B/test_grupe.csv'
    # ceo_fajl = pd.read_csv(r'D:\milap\Faza3\podaci\internal\s2\podaci_s1_dodavanje.csv')
    ceo_fajl = pd.read_csv(pomocna)
    assert ~ceo_fajl["DATUM"].is_monotonic, "nije sortiran datum"

    ceo_fajl = dodaj_br_perioda_do_poslednje_dopune(ceo_fajl)
    # ceo_fajl.to_csv(r'D:\milap\Faza3\podaci\internal\s3\jedna_grupa3.csv', index = False)
    ceo_fajl.to_csv(r'../../../../podaci/internal/C/test_grupe.csv', index=False)


if __name__ == "__main__":
    run3()
