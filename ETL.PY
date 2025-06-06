# %%
import pandas as pd
import requests

# %% [markdown]
# ###EXTRAÇÃO

# %%
url = "https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome"
resp = requests.get(url)


# %%
deputados = pd.DataFrame(resp.json()['dados'])

# %%
deputados.head()

# %%


# %%
deputados.shape

# %%
gastos = []

for id in deputados.id:
    url_despesa = "https://dadosabertos.camara.leg.br/api/v2/"
    url_despesa = url_despesa + "deputados/"+str(id)+"/despesas?ordem=ASC&ano=2024"
    resposta = requests.get(url_despesa)
    gasto = pd.DataFrame(resposta.json()['dados'])
    gasto['id'] = id
    gastos.append(gasto)

# %%
len(gastos)

# %%
len(gastos[0])

# %% [markdown]
# ###TRANSFORMAÇÃO

# %%
total = pd.concat(gastos)

# %%
total.head()

# %%
total.sample(3)

# %%
total.isnull().sum()

# %%
del total['urlDocumento']

# %%
total.head()

# %%
total.numRessarcimento.value_counts()

# %%
total.shape

# %%
del total['numRessarcimento']

# %%
total.head()

# %%
print(total.shape)
total.drop_duplicates()

# %%
total.info()

# %%
total.describe()

# %%
total.nomeFornecedor.value_counts()

# %% [markdown]
# ###CARGA

# %%
from sqlalchemy import create_engine

# %%
engine = create_engine('sqlite:///dados_abertos.db')

# %%
deputados.to_sql('deputados',engine)


# %%
total.to_sql('despesas_total', engine)



# %%
total = pd.read_sql("select * from despesas_total;", engine)
total.head()

# %%
deputados = pd.read_sql("select * from deputados;", engine)
deputados.head()

# %%
total = total.merge(deputados, on=['id'])

# %%
total.head()

# %%
gastos_deputados = total.groupby(['nome',]).sum()[['valorDocumento', 'valorLiquido']]

# %%
gastos_deputados = gastos_deputados.sort_values('valorDocumento', ascending=False)


# %%
gastos_deputados.head(10).plot(kind='bar')

# %%
gastos_deputados.tail().plot(kind='bar')

# %%q
%matplotlib inline

# %%
total.nomeFornecedor.value_counts()[:10].plot(kind='bar')



