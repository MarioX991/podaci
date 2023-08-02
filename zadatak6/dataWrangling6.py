import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
# postavke da se vide sve kolone
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 50)
# -------------------------------------

#fajl = pd.read_csv("deo_podataka.csv",usecols= ['Kolicina_Prodaja','Kolicina_Zaliha','ORGJED_SIFRA','ARTIKAL_ID','DATUM'])
fajl = pd.read_csv(r"../../../../podaci/input-data/deo_podataka.csv")

# sredjivanje i sortiranje datuma
fajl['DATUM'] = pd.to_datetime(fajl['DATUM'], format='%Y-%m-%d')
fajl = fajl.sort_values('DATUM')
fajl = fajl.reset_index(drop = True).drop("Unnamed: 0", axis = 1)
print(fajl.set_index(["ORGJED_SIFRA", "ARTIKAL_ID", "DATUM"]).unstack().shape) # 8717 rows x 958
fajl_1 = fajl.set_index(["ORGJED_SIFRA", "ARTIKAL_ID", "DATUM"])


def koliko_datuma_nedostaje(df:pd.DataFrame, colona:str = "DATUM")->int:
    min_dat = df[colona].min()
    max_dat = df[colona].max()
    idx = pd.date_range(min_dat, max_dat, freq="D")
    df[colona] = pd.to_datetime(df[colona], format="%Y%m%d" )

    return len(idx)-len(fajl["DATUM"].unique())


#print(koliko_datuma_nedostaje(fajl, "DATUM"))

def koji_nedostaju(df, colona = "Kolicina_Prodaja"):
    """funckija trazi nedostojauce datume iz kolone datum
    df - mora biti indeksiran
    """

    nedostajuci = []
    # izdvajamo jednu kolonu
    kp = df.unstack()[colona]
    # trazimo max i min datum
    max_dat = kp.stack().index.get_level_values(-1).values.max()
    min_dat = kp.stack().index.get_level_values(-1).values.min()
    # kreiramo sve indekse
    indexi = pd.date_range(min_dat, max_dat, freq='D')
    # pretvaramo indekse u odgovarajuci format
    series = pd.Series(indexi.values)
    dates = pd.to_datetime(series, format='%Y-%m-%d')
    indeksi = dates.strftime('%Y-%m-%d').values

    trenutni = np.unique(kp.columns.values)


    for i in indeksi:
        if i not in trenutni:
            nedostajuci.append(i)

    return nedostajuci






def dopuna_godina(df:pd.DataFrame, colona:str = "DATUM")->pd.DataFrame:
    """
    Funckija unosi datume koji su izostvljeni iz potojeceg Data Frejma.
    param: df DataFrame nad kojem vrsimo dopunu
    param: colona string -  naziv kolone koja sadrzi datume
    """

    min_dat = df[colona].min()
    max_dat = df[colona].max()
    idx = pd.date_range(min_dat, max_dat, freq="D")


    # kreiranje novog DataFrame sa svim datumima
    # novi_df = pd.DataFrame().reindex(columns=df.columns)
    novi_df = pd.DataFrame([],columns=['Kolicina_Prodaja','Kolicina_Zaliha','ORGJED_SIFRA',
                                   'ARTIKAL_ID','DATUM'])
    novi_df.loc[:,'DATUM'] = idx
    novi_df.loc[:,'ORGJED_SIFRA'] ="Z"
    novi_df.loc[:,'ARTIKAL_ID'] =9

    # spajanje postojceg da novim novi_df
    svi_datumi = pd.concat([fajl, novi_df]).reset_index(drop = True)
    # # todo da li asset moze u ovoj funkciji - koliko komplikuje testiranje
    # assert (df.shape[0] != svi_datumi.shape[0]), "nije doslo do dopune datuma"

    return svi_datumi


def dopuna_godina_dodaj_colone(df):
    nedostajuci_datumi =  koji_nedostaju(df)

    kp = df.unstack()['Kolicina_Prodaja']
    kz = df.unstack()['Kolicina_Zaliha']

    for i in nedostajuci_datumi:
        kp.loc[:, i] = np.nan
        kz.loc[:,i] = np.nan

    return pd.concat([kp,kz], axis=1)


#print(dopuna_godina_dodaj_colone(fajl_1))





svi_datumi = dopuna_godina(fajl, "DATUM")[['Kolicina_Prodaja','Kolicina_Zaliha','ORGJED_SIFRA',
                                   'ARTIKAL_ID','DATUM']]
print(svi_datumi)

assert (fajl.shape[0] != svi_datumi.shape[0]), "nije doslo do dopune datuma"
assert ~svi_datumi["DATUM"].is_monotonic ,"nije sortiran datum"

svi_datumi = svi_datumi.set_index(["ORGJED_SIFRA", "ARTIKAL_ID", "DATUM"])
print(svi_datumi.reset_index().shape) #(10000, 5)
svi_datumi = svi_datumi.unstack()
print(svi_datumi.shape)

svi_datumi["Kolicina_Prodaja"].fillna(0, inplace = True)
svi_datumi["Kolicina_Zaliha"].ffill(inplace = True)
svi_datumi["Kolicina_Zaliha"].fillna(0, inplace = True)

#print(svi_datumi)
svi_datumi = svi_datumi.stack()
#print(svi_datumi)
svi_datumi = svi_datumi.drop("Z", level =0 , axis = 0)


print(svi_datumi.shape)
maska1 = (svi_datumi["Kolicina_Prodaja"] < 0)
maska2 = (svi_datumi["Kolicina_Zaliha"] < 0)

svi_datumi.loc[maska1 , "Kolicina_Prodaja"] = 0
svi_datumi.loc[maska2, "Kolicina_Zaliha" ] = 0
svi_datumi.reset_index(inplace = True)

#svi_datumi.to_csv(r"../../podaci/internal/B/deo_1.csv", index = False)







#
# print(svi_datumi)
# #masksa ako su neke vrednost kolicina proidaje zaliha negativne idu na nulu
#
# maska = (svi_datumi["Kolicina_Prodaja"]<0)
# # print(maska.values)
# # print(np.unique(maska.values, return_counts=True))
# svi_datumi.loc[maska, "Kolicina_Prodaja"] = 0
# maska = (svi_datumi["Kolicina_Zaliha"]<0)
# svi_datumi.loc[maska, "Kolicina_Zaliha"] = 0
#
# razlika_tr_preth = svi_datumi['Kolicina_Zaliha'].diff()
# maska1 = (razlika_tr_preth < svi_datumi["Kolicina_Prodaja"])
# maksa2 = (razlika_tr_preth<0)
# svi_datumi.loc[~maska, "POSTOJI_DOPUNA"]= np.NaN





#

