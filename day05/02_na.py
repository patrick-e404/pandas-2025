#%%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv",sep=";")
clientes

#%%
#RETIRA TODOS NA EM UMA LINHA
clientes.dropna(how="any")
#%%

df = pd.DataFrame({
    "nome": ["Teo", None, "Andressa", "Patrick" ],
    "idade": [None, None, 28, 30],
    "salario": [3453, 4324, None, 5423]
})

df.dropna(how="any", subset=["idade", "salario"])
#%%

df["idade"] = df["idade"].fillna(0)
df
#%%

df.fillna({"nome": "alguém", "idade": 0})
#%%
#SUBSTITUIR NA POR UMA MÉDIA

medias = df[["idade", "salario"]].mean()
df.fillna(medias)