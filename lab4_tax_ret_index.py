import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# TODO Avaliar a questão do índice Bovespa --> Relfetir a respeito

tickers = ['^GSPC', '^IXIC', '^GDAXI', '^RUT', '^BVSP']
ind_data = pd.DataFrame()
for t in tickers:
    ind_data[t] = wb.DataReader(
        t, data_source='yahoo', start='2000-01-01')['Adj Close']

print('\nDados da carteira e importante que todos os tickets tenham mesma quantidade de informacao')
print(ind_data.info())
print(ind_data.head())
print(ind_data.tail())

# Normalizando os dados P1/P0 *100 --> Normalizando para a BASE 100

(ind_data / ind_data.iloc[0] * 100).plot(figsize=(15, 6))
plt.show()

# Efeito da não normalização dos dados --> observe os gráficos (eles não partem da mesma referência)
ind_data.plot(figsize=(15, 6))
plt.show()

# A seguir o cálculo do Retorno Simples dos índeces observados

returns = (ind_data / ind_data.shift(1)) - 1
print(returns.tail())

# Retorno médio anual dos índices analisados

annual_ind_returns = returns.mean() * 250
print('\nExibe o retorno anual dos indices\n')
print(annual_ind_returns)

# VOLTAR AQUI E DEFINIR O VALOR DE RETORNO DOS ÍNDICES COM 3 CASAS DECIMAIS

annual_decimal = str(round(annual_ind_returns, 5) * 100) + '%'
print('\nExibe o retorno anual dos indices de orma mais amigavel em %\n')
print(annual_decimal)

# Feito isso, vamos pegar o preço da ação de uma empresa e vamos compará-lo com um dos índices. Vamos optar pelo SP 500 depois incluir o índice DJ. A empresa será a já conhecida PG

# TODO Avaliar a questão do índice BOVESPA

tickers = ['PG', '^GSPC', '^DJI', '^BVSP']
data_2 = pd.DataFrame()
for t in tickers:
    data_2[t] = wb.DataReader(t, data_source='yahoo',
                              start='2010-1-1')['Adj Close']
print(data_2.tail())

# A seguir vamos normalizar os dados para análise -- BASE 100

(data_2/data_2.iloc[0] * 100).plot(figsize=(15, 6))
plt.show()
