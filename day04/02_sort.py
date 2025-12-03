#%%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes["qtdePontos"].sort_values()

#%%
clientes.sort_values(by="qtdePontos", ascending=False).head()

#%%

# TOP 5 POR ID
top_5_porId = (clientes.sort_values(by="qtdePontos", ascending=False).head()["idCliente"])
top_5_porId

#%%
#EXEMPLO COM EMPATE

exemplo = pd.DataFrame(
    {
        "nome": ["teo","patrick","andressa","cardoso",],
        "idade": [1,28,30,25,],
        "salario": [2345,4533,3245,4533,]
    }
)
exemplo
#%%

exemplo.sort_values(by=["salario", "idade"], ascending=[False, True])