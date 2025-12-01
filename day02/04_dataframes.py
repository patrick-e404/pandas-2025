#%%
import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes
#%%
df_clientes.head(n=10)
#%%
df_clientes.tail()
#%%
#AMOSTRA ALEATORIA
df_clientes.sample(10)
#%%
#SHAPE INDICA QUANTAS LINHAS E QUANTAS COLUNAS
df_clientes.shape
#%%
#COLUMNS INFORMA QUAIS SÃO AS COLUNAS
df_clientes.columns
#%%
#INDEX INFORMA QUAIS SÃO OS INDICES
df_clientes.index
#%%
df_clientes.info(memory_usage='deep', max_cols=2)
#%%
#DTYPES É UMA SERIE QUE MOSTRA OS VALORES DA TIPAGEM DE CADA CAMPO/COLUNA
df_clientes.dtypes
