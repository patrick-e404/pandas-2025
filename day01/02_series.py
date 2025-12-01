#%%
idades = [
    32,38,30,30,31,
    35,25,29,31,37,
    27,23,36,33,32,
]

media = sum(idades) / len(idades)
print("Media: ",media)

diffs = 0
for i in idades:
    diffs += (i - idades) ** 2

variancia = diffs / (len(idades) - 1)
print("Variância:", variancia)
#POR ISSO LISTAS NÃO SÃO A MELHOR FORMA DE SE TRABALHAR COM DADOS
#%%

#CONHECENDO SERIES
import pandas as pd

series_idades = pd.Series(idades)
series_idades
#%%
series_idades.mean()
var_idades = series_idades.var()
var_idades
summary = series_idades.describe()
summary
