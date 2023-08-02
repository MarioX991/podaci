import pandas as pd
import numpy as np
import warnings
pd.set_option("display.width",320)
pd.set_option('display.max_columns',50)
warnings.filterwarnings("ignore")
from Zadaci.Zadatak6.parametri import osnovne_kolne_df, indeksne_kolone1, kolona_datum, indeksne_kolone2


def izlistavanje_svih_grupa(df):
    """
    Funkcija izslistava grupe u kojima imamo kolicinu zaliha i kolicinu prodaje u nekim redovima vecu od nule
    """

    ceo = df[(df['Kolicina_Prodaja'] > 0) & (df['Kolicina_Zaliha'] > 0) ]

    lista_grupacija = []
    for keys, groups in ceo.groupby(['ORGJED_SIFRA', 'ARTIKAL_ID']):
        # print(f"{keys} {groups.shape}")
        lista_grupacija.append([keys, {groups.shape}])

    return lista_grupacija


def funkcija_za_odabir_grupa(df, listing=[('15001P', 50501),('19005P',67832),('19005P',74905)]):
    """
    Funckija se koristi za odabit odredjenih grupa koje zelimo da izvojimo iz datafrejma.
    :param df
    :param listing - grupe koje zelimo da izdvojimo
    :return df_grupe vraca DataFrejm koje je kreiran od gore prosledjnih grupa
    """

    gruper = df.groupby(indeksne_kolone2)
    df_grupe = pd.concat([groups for (name, groups) in gruper if name in listing])

    return df_grupe


def run(save_file=True):
    fajl = pd.read_csv(r"../../../../podaci/input-data/MLDrmax_beograd.csv",
                       usecols=['ORGJED_SIFRA', 'ARTIKAL_ID', 'DATUM', 'Kolicina_Prodaja', 'Kolicina_Zaliha'],

                       dtype={'ORGJED_SIFRA': str, 'ARTIKAL_ID': int,
                              'DATUM': str, 'Kolicina_Zaliha': float, 'Kolicina_Prodaja': float}, low_memory=False
                       )
    #print(fajl.shape)
    #lista = izlistavanje_svih_grupa(fajl)
    #print(f"Lista grupa koje su adekvatne za kreiranje test skupa: \n {lista}")
    grupe = funkcija_za_odabir_grupa(fajl)
    #print(grupe)

    if save_file==True:
        grupe.to_csv(r'../../../../podaci/input-data/test_grupe.csv')


if __name__ == "__main__":
    run()