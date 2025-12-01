#%%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")

df.shape
df.info(memory_usage='deep')
#%%
df.dtypes
#%%
#RENOMEAR UMA COLUNA

renamed_columns = {
    "QtdePontos": "qtPontos",
    "DescSistemaOrigem":"SistemaOrigem"
}

df.rename(columns=renamed_columns, inplace=True)
df
#%%
colunas = ["IdCliente", "qtPontos"]
df[colunas]
#%%
                            #EXEMPLOS COM SQL
# SELECT * FROM df
df
#%%
# SELECT IdCiente FROM df
df[['IdCliente']]
#%%
# SELECT IdCliente, qtPontos FROM df LIMIT 5
df[["IdCliente", "qtPontos"]].head(5)
#%%
# SELECT IdCliente, IdTransacao, qtPontos
# FROM df
# LIMIT 5

df[["IdCliente", "IdTransacao", "qtPontos"]].head(5)
#%%
#ORDENAR EM ORDEM ALFABETICA
colunas = list(df.columns)
colunas.sort()
colunas

df = df[colunas]
df
