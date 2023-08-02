import pandas as pd

ceo_fajl = pd.read_csv(r'D:\milap\Faza3\podaci\jedna_grupa1.csv')
ceo_fajl.rename(columns = {'qORGJED_SIFRA':'ORGJED_SIFRA'}, inplace =True)

ceo_fajl.set_index(['ORGJED_SIFRA','ARTIKAL_ID'], drop = True, inplace=True)

print(ceo_fajl)

