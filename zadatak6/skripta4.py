import pandas as pd
import numpy as np
import warnings


warnings.filterwarnings("ignore")
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 50)
warnings.filterwarnings("ignore")

from zadaci.zadatak6.skripta3 import popunjavanje_kolone_maskom, brojac_dana_do_dopune
from zadaci.zadatak6.parametri import osnovne_kolne_df, indeksne_kolone1, indeksne_kolone2, kolona_datum, kolona_datum


def obrni_pa_vrati(kolona):
    kolona = kolona[::-1]
    kolona = brojac_dana_do_dopune(kolona)
    kolona = kolona[::-1]
    return kolona


def dodaj_broj_daba_do_isteka_zaliha(df):
    assert 'BROJ_DANA_DO_SLEDECE_DOPUNE' not in df.columns
    assert 'BROJ_DANA_DO_ISTEKA_ZALIHA' not in df.columns

    # izdvajam maski kada postoji dopuna je nan
    maska_do_poslednje_dopune = df['POSTOJI_DOPUNA'].isna()
    # pretvaram maksu u 1 i 0
    popunjavanje_kolone_maskom(df, 'BROJ_DANA_DO_SLEDECE_DOPUNE', maska_do_poslednje_dopune)

    # prebrojava u opadajucem poretku na grupama
    df.loc[:, 'BROJ_DANA_DO_SLEDECE_DOPUNE'] = df.groupby(indeksne_kolone2)['BROJ_DANA_DO_SLEDECE_DOPUNE'] \
        .transform(obrni_pa_vrati)
    # maksa za delove kolona_zaliha gde imamo vrenosti koje su razlicite od nule
    maska_zalihe = ~(df['Kolicina_Zaliha'] == 0)
    # prebacujem masku u 1 i nulu
    popunjavanje_kolone_maskom(df, 'BROJ_DANA_DO_ISTEKA_ZALIHA', maska_zalihe)
    # prebrojava u opadajucem poretku na grupama
    df.loc[:, 'BROJ_DANA_DO_ISTEKA_ZALIHA'] = df.groupby(indeksne_kolone2)['BROJ_DANA_DO_ISTEKA_ZALIHA'].transform(
        obrni_pa_vrati)

    # KLJUC ZADATAKA ZA KREIRANJE KOLONE  MASKA
    maska_broj_dana = df['BROJ_DANA_DO_SLEDECE_DOPUNE'] <= df['BROJ_DANA_DO_ISTEKA_ZALIHA']
    df.loc[maska_broj_dana, 'BROJ_DANA_DO_ISTEKA_ZALIHA'] = np.NaN
    # ZBOG POCETNIH NULA DA BI SE PREBACILE U NAN
    df['BROJ_DANA_DO_ISTEKA_ZALIHA'].replace(0, np.NaN, inplace=True)
    df.drop('BROJ_DANA_DO_SLEDECE_DOPUNE', axis=1, inplace=True)


def run4():


    ceo_fajl = pd.read_csv(r'../../../../podaci/internal/C/test_grupe.csv')
    # print(ceo_fajl.columns)
    # ceo_fajl = pd.read_csv(r'D:\milap\Faza3\podaci\internal\s3\jedna_grupa3.csv')

    assert ~ceo_fajl["DATUM"].is_monotonic, "nije sortiran datum"

    dodaj_broj_daba_do_isteka_zaliha(ceo_fajl)
    # print(ceo_fajl.columns)
    assert 'BROJ_DANA_DO_SLEDECE_DOPUNE' not in ceo_fajl.columns
    # print(ceo_fajl)
    # print(obrni_kolonu(ceo_fajl['ORGJED_SIFRA']))

    ceo_fajl.to_csv(r'../../../../podaci/results/kraj.csv')

    # print(ceo_fajl)


if __name__ == "__main__":
    run4()
