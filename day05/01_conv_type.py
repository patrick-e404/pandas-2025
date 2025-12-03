#%%
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")

#%%
#TROCAR O TIPO
df["qtdePontos"].astype(float)

#%%

#COMO SUBSTITUIR (REPLACE) | PARTE LOGICA

df["DtCriacao"] = df["DtCriacao"].replace({
    "2024-02-01 00:00:00.000": "2025-02-01 00:00:00.000"
})
pd.to_datetime(df["DtCriacao"])
#%%
#É MAIS COMUM VER DESSA FORMA

replace = {"2024-02-01 00:00:00.000": "2025-02-01 00:00:00.000"}
df["DtCriacao"] = pd.to_datetime(df["DtCriacao"].replace(replace))
#%%

df["DtCriacao"].dt.date