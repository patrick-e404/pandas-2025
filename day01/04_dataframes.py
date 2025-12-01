#%%
import pandas as pd

idades = [
    32,38,30,30,31,
    35,25,29,31,37,
    27,23,36,33,39,
]

nomes = [
    "Patrick","Cardoso","Maria","Jose", "Michael",
    "Gustavo","Dimitri","Mariane","Gabriela", "João",
    "Andressa","Kelly","Luan","Nicolas", "Dosolina"
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)
series_idades
series_nomes
#%%

df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes

#%%

#COMO PEGAR UM INDICE E COLUNA ESPECIFICOS NO DATAFRAME

df.iloc[-1]["nomes"]
df.iloc[-1]["idades"]