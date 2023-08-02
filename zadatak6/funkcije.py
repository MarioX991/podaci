import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
#----------------------***********-------------------------#
#---------------------> SKRIPTA 4 <------------------------#
#----------------------***********-------------------------#

def popunjavanje_kolone_maskom(df, kolona, maska):
    # kada je maska to je true --> 1
    df.loc[maska, kolona] = 1
    df.loc[~maska, kolona] = 0


def brojac(kolona):
    suma = kolona.cumsum()
    kolona *= suma
    kolona = kolona.diff().where(lambda x: x < 0).fillna(method='ffill')
    kolona += suma
    return kolona
