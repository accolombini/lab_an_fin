import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


tickers = ['PG', 'BEI.DE']
sec_data = pd.DataFrame()
for t in tickers:
    sec_data[t] = wb.DataReader(
        t, data_source='yahoo', start='2000-01-01')['Adj Close']

print('\nDados da carteira o importante e que todos os tickets tenham mesma quantidade de informacao')
print(sec_data.info())

print('\nOlhando para os dados para uma inspecao aos dados reais')
print(sec_data.head())
print(sec_data.tail())

# Estaremos analisado cada ativo individualmente, para estes casos, o retorno logaritmico e mais interessante

print('Calculo do retorno logaritmico, mais interessante para este tipo de analise')

sec_returns = np.log(sec_data/sec_data.shift(1))
print('O retorno logaritmico dos ativos e: \n')
print(sec_returns)

# Vamos trabalhar com uma carteira balanceada => 50% x 50%
# Devemos salvar os pesos numa matriz numpy => observe abaixo

weights = np.array([0.5, 0.5])

# Calculo da variancia do portfolio
# A seguir fazemos um produto de matrizes (ab)**2 usando numpy => observe a simplicidade quando se usa numpy.dot()

pfolio_var = np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))
print('\nVariancia do Portfolio: ', pfolio_var)

# Calculo da Volatilidade do Protfolio

pfolio_vol = (np.dot(weights.T, np.dot(
    sec_returns.cov() * 250, weights))) ** 0.5
print('\nVolatilidade do Portfolio: ', pfolio_vol)

print('Volatilidade Formatada do Portfolio: ',
      str(round(pfolio_vol, 5) * 100) + '%')
