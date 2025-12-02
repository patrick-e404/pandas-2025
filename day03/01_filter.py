#%%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()
#%%
#FORMAS PARA OBTER MAIS DE 50 PONTOS
pontos = [10, 1, 1, 1, 50, 100, 130, 30, 25, 50]
filtro = []

valores_50_mais = []
for i in pontos:
    filtro.append(i>=50)

resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])

resultado
#%%
#LIST COMPREHENSION
valores_50_mais = [i for i in pontos if i >= 50]
#%%
#FILTRANDO NO DATAFRAME
familia = pd.DataFrame(
     {
          "nome": ["teo", "patrick", "andressa"],
          "idade": [1, 28, 30],
          "uf": ["sp", "pr", "rj"]
     }
)

filtro = familia["idade"] <= 18
familia[filtro]
#%%
#FILTRAR POR VALORES MAIORES QUE 50
filtro_50 = df["QtdePontos"] >= 50
df[filtro_50]
#%%
#FILTRAR POR VALORES MAIORES QUE 50 E MENORES QUE 100
filtro_50_100 = (df["QtdePontos"] >= 50) & (df["QtdePontos"] <= 100)
df[filtro_50_100]
#%%
#FILTRAR POR 1 VALOR OU OUTRO
filtro_or = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filtro_or]
#%%
#FILTRAR PONTOS ENTRE 0 E 50 OU DO ANO DE 2025 PARA FRENTE
filtro_xpto = (df["QtdePontos"] > 0) & (df["QtdePontos"]<=50) | (df["DtCriacao"]>="2025-01-01")
df[filtro_xpto]