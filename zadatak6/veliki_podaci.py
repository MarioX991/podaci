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



fajl = pd.read_csv(r'../../../../podaci/input-data/deo_podataka.csv')
#print(fajl.columns)
ceo_fajl = fajl[['ORGJED_SIFRA', 'ARTIKAL_ID', 'DATUM', 'Kolicina_Prodaja','Kolicina_Zaliha']]
#ceo_fajl['DATUM'] = pd.to_datetime(ceo_fajl['DATUM'], format='%Y-%m-%d')
ceo_fajl = ceo_fajl.sort_values('DATUM')
ceo_fajl = ceo_fajl.reset_index().drop(axis=1, columns='index')
idx = pd.date_range(ceo_fajl.loc[1, 'DATUM'], ceo_fajl.loc[len(ceo_fajl)-1, 'DATUM'])
idx= str(idx)

#dodaj datume koji fale
ceo_fajl = ceo_fajl.set_index(['ORGJED_SIFRA','ARTIKAL_ID','DATUM'])

#ceo_fajl = ceo_fajl.unstack()
#print(ceo_fajl)
# ceo_fajl['Kolicina_Prodaja']['']= np.nan
#
# frame = ceo_fajl.loc[:,('15046P',52449)]
# frame = frame.append(pd.DataFrame(idx), ignore_index=True)
#
# frame = frame.drop(0,axis=0)
# frame.set_index([0], inplace=True)
# frame.index.names = ['DATUM']
#
# print(frame)

# ceo_fajl = ceo_fajl.append(frame, ignore_index = True)
# ceo_fajl.loc[('15046P',52449)] = ceo_fajl.loc[('15046P',52449)].append(frame)

#df1 = ceo_fajl.loc[('15046P',52449)]
#
# ceo_fajl.merge(frame, on='DATUM', how='iner')

# print(ceo_fajl['Kolicina_Prodaja'].reindex())
# for i in idx:
#     print(i)
#     if i not in ceo_fajl['Kolicina_Prodaja'].columns.values:
#         ceo_fajl['Kolicina_Prodaja']


# imena_prodaje =['Kolicina_Prodaja'] * len(idx)
# Kolicina_Zaliha =['Kolicina_Zaliha'] * len(idx)
# sve_imena = (np.concatenate([imena_prodaje,Kolicina_Zaliha]))
#
# midx = pd.MultiIndex.from_arrays([sve_imena, np.concatenate([idx,idx])], names=['level 0', 'level 1'])
# print(midx)
# print(ceo_fajl._construct_result(midx))


ceo_fajl['Kolicina_Prodaja'].fillna(0, inplace=True)
ceo_fajl['Kolicina_Zaliha'].ffill(inplace=True)
ceo_fajl['Kolicina_Zaliha'].fillna(0, inplace=True)

ceo_fajl = ceo_fajl.stack('DATUM')
maska_prodaja = (ceo_fajl['Kolicina_Prodaja'] < 0)
maska_zalihe = (ceo_fajl['Kolicina_Zaliha'] < 0)

ceo_fajl.loc[maska_prodaja, 'Kolicina_Prodaja'] = 0
ceo_fajl.loc[maska_zalihe, 'Kolicina_Zaliha'] = 0


ceo_fajl['POSTOJI_DOPUNA'] = ceo_fajl['Kolicina_Zaliha'].diff()

maksa1 = (ceo_fajl['POSTOJI_DOPUNA'] < ceo_fajl['Kolicina_Prodaja'])
maska2 = (ceo_fajl['POSTOJI_DOPUNA'] < 0)
ceo_fajl.loc[~maksa1, 'POSTOJI_DOPUNA'] = np.NaN
ceo_fajl.loc[maska2, 'POSTOJI_DOPUNA'] = np.NaN


maskica = ceo_fajl['POSTOJI_DOPUNA'].isna()

ceo_fajl.loc[maskica, 'BROJ_PERIODA_OD_POSLEDNJE_DOPUNE'] = 1
ceo_fajl.loc[~maskica, 'BROJ_PERIODA_OD_POSLEDNJE_DOPUNE'] = 0

kolona_save1 = ceo_fajl['BROJ_PERIODA_OD_POSLEDNJE_DOPUNE']
kolona = ceo_fajl['BROJ_PERIODA_OD_POSLEDNJE_DOPUNE'].cumsum()
ceo_fajl['BROJ_PERIODA_OD_POSLEDNJE_DOPUNE'] = ceo_fajl['BROJ_PERIODA_OD_POSLEDNJE_DOPUNE'].cumsum()
ceo_fajl['BROJ_PERIODA_OD_POSLEDNJE_DOPUNE'] *=kolona_save1

ceo_fajl['BROJ_PERIODA_OD_POSLEDNJE_DOPUNE'] = ceo_fajl['BROJ_PERIODA_OD_POSLEDNJE_DOPUNE'].diff().where(lambda x: x<0).fillna(method='ffill')
ceo_fajl['BROJ_PERIODA_OD_POSLEDNJE_DOPUNE'] += kolona

ceo_fajl['BROJ_PERIODA_OD_POSLEDNJE_DOPUNE'].iloc[1:] = ceo_fajl['BROJ_PERIODA_OD_POSLEDNJE_DOPUNE'].iloc[:len(ceo_fajl) - 1]
ceo_fajl['BROJ_PERIODA_OD_POSLEDNJE_DOPUNE'] *= (~maskica)

ceo_fajl['BROJ_PERIODA_OD_POSLEDNJE_DOPUNE'].replace(0, np.NaN, inplace=True)


#ceo_fajl.loc[maskica, 'BROJ_PERIODA_DO_NESTANKA_ZALIHA'] = np.NaN

nan_od_dopune = ceo_fajl['POSTOJI_DOPUNA'].isna()

ceo_fajl.loc[nan_od_dopune, 'BROJ_DANA_DO_SLEDECE_DOPUNE'] = 1
ceo_fajl.loc[~nan_od_dopune, 'BROJ_DANA_DO_SLEDECE_DOPUNE'] = 0

kolona_save = ceo_fajl['BROJ_DANA_DO_SLEDECE_DOPUNE'].iloc[::-1]

kolona = kolona_save.cumsum()
kolona_save *= kolona
kolona_save = kolona_save.diff().where(lambda x: x < 0).fillna(method='ffill')
kolona_save += kolona
ceo_fajl['BROJ_DANA_DO_SLEDECE_DOPUNE'] = kolona_save.iloc[::-1]

#sada broj dana do nestanka zaliha
maska_zalihe = (ceo_fajl['Kolicina_Zaliha'] == 0)
ceo_fajl.loc[maska_zalihe, 'BROJ_DANA_DO_ISTEKA_ZALIHA'] = 0
ceo_fajl.loc[~maska_zalihe, 'BROJ_DANA_DO_ISTEKA_ZALIHA'] = 1
kolona_isticanje_zaliha = ceo_fajl['BROJ_DANA_DO_ISTEKA_ZALIHA'].iloc[::-1]

kumulativna_suma = kolona_isticanje_zaliha.cumsum()
kolona_isticanje_zaliha *= kumulativna_suma
kolona_isticanje_zaliha = kolona_isticanje_zaliha.diff().where(lambda x: x < 0).fillna(method='ffill')
kolona_isticanje_zaliha += kumulativna_suma

ceo_fajl['BROJ_DANA_DO_ISTEKA_ZALIHA'] = kolona_isticanje_zaliha.iloc[::-1]

# print(ceo_fajl)
