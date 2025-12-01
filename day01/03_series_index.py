#%%
import pandas as pd

idades = [
    32,38,30,30,31,
    35,25,29,31,37,
    27,23,36,33,39,
]

series_idades = pd.Series(idades)
series_idades

series_idades = series_idades.sort_values()
series_idades
#ILOC PARA BUSCAR ASSIM COMO EM LISTAS
series_idades.iloc[-2]

#%%

idades = [
    32,38,30,30,31,
    35,25,29,31,37,
    27,23,36,33,39,
]

indexs = [
    "Patrick","Cardoso","Maria","Jose", "Michael",
    "Gustavo","Dimitri","Mariane","Gabriela", "João",
    "Andressa","Kelly","Luan","Nicolas", "Dosolina"
]

series_idades = pd.Series(idades, index=indexs)
series_idades
