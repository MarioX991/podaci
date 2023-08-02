import pandas as pd
import numpy as np
import warnings
pd.set_option("display.width",320)
pd.set_option('display.max_columns',50)

warnings.filterwarnings("ignore")
from zadaci.zadatak6.parametri import osnovne_kolne_df, indeksne_kolone1, kolona_datum, indeksne_kolone2

# todo OVO MOZES IZBACITI IZ FUNKCIJE AKO HOCES
def negativne_vresnoti_u_nulu(df: pd.DataFrame) -> pd.DataFrame:
    """
    Funkcija sve negativne vrednosti u kolonama Kolicina_Prodaje i Kolicina_Zaliha prebacuje u nulu
    """

    df.loc[:, 'Kolicina_Prodaja'] = df['Kolicina_Prodaja'].transform(lambda x: 0 if x < 0 else x)
    df.loc[:, 'Kolicina_Zaliha'] = df['Kolicina_Zaliha'].transform(lambda x: 0 if x < 0 else x)

    return df


def kreiranje_kolone_postoji_dopuna(df: pd.DataFrame) -> pd.DataFrame:
    """
    Funkcija kreira kolonu POSTOJI_DOPUNA koja sadrži informaciju o tome da li je taj dan za  kombinaciju artikal-orgjed postojala dopuna, po sledecem pravilu:
    - Dopuna postoji ukoliko je razlika u zalihama izmedju prethodnog i trenutnog  dana manja od prodaje trenutnog dana.
    - Ukoliko postoji dopuna tog dana, kolona POSTOJI_DOPUNA sadrži količinu  kojom su zalihe dopunjene.
    - Ukoliko ne postoji dopuna, kolona sadrži null vrednost.
    :param dd


    """
    assert "Razlika_u_kolicini_zaliha" not in df.columns, "Kolona vec postoji u Data Frejm-u!"
    df.loc[:,"Razlika_u_kolicini_zaliha"] = df.groupby(['ORGJED_SIFRA', 'ARTIKAL_ID'])['Kolicina_Zaliha'].diff()

    print(df)

    # pravimo masku kada nemao dopune
    maksa_nema_dopune = (df["Razlika_u_kolicini_zaliha"] + df['Kolicina_Prodaja'] <= 0)

    #todo STO NAM JE POTREBNA OVA DRUGA MASKA
    maska_negativne_vrednosti = (df["Razlika_u_kolicini_zaliha"]<0)


    df.loc[maksa_nema_dopune, 'POSTOJI_DOPUNA'] = np.NaN

    # za delove gde imamo dopunu tu popunjavamo kolicinom dopune
    df.loc[~maksa_nema_dopune, 'POSTOJI_DOPUNA'] = (df.loc[~maksa_nema_dopune, "Razlika_u_kolicini_zaliha"] +
                                                    df.loc[~maksa_nema_dopune, 'Kolicina_Prodaja'])

    # TODO: DRUGA MASKA
    df.loc[maska_negativne_vrednosti, 'POSTOJI_DOPUNA'] = np.NaN

    df.drop("Razlika_u_kolicini_zaliha", axis = 1, inplace = True)

    return df


def run(save_file= True):
    proba = r'../../../../podaci/internal/A/test_grupe.csv'
    fajl = pd.read_csv(proba)
    # fajl = pd.read_csv(r'../../podaci/input-data/test_grupe.csv',
    #                    usecols=osnovne_kolne_df,
    #                    dtype={'ORGJED_SIFRA': str, 'ARTIKAL_ID': int,
    #                           'DATUM': str, 'Kolicina_Zaliha': float, 'Kolicina_Prodaja': float}, low_memory=False
    #                    )
    print(fajl.shape)

    fajl.sort_values("DATUM", inplace=True)
    assert fajl["DATUM"].is_monotonic, "Kolona DATUM nije sortirana"

    fajl = negativne_vresnoti_u_nulu(fajl)



    #fajl.set_index(indeksne_kolone2, drop=True, inplace=True)

    fajl = kreiranje_kolone_postoji_dopuna(fajl)

    fajl = fajl.sort_values(["ORGJED_SIFRA","ARTIKAL_ID"])



    fajl.to_csv(r'../../../../podaci/internal/B/test_grupe.csv', index=False)

# maska2 = (df['POSTOJI_DOPUNA'] < 0)

    #if save_file:
        #fajl.to_csv(r'../../podaci/internal/A/test_fajl_postoji_dopuna.csv')
#
if __name__ == "__main__":
    run()
