import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


tickers = ['PG', 'BEI.DE']
sec_data = pd.DataFrame()
for t in tickers:
    sec_data[t] = wb.DataReader(t, data_source='yahoo',
                                start='2010-01-01')['Adj Close']

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

# Calculo da media e do desvio padrao das Acoes --> O desvio padrao pode ser chamado de Risco do ativo
# Calculando primeiramente para a PG => Maior desvio padrao, maior a volatilidade do ativo

print('\nA media diaria PG               e: ', sec_returns['PG'].mean())
print('A media anual  PG               e: ', sec_returns['PG'].mean() * 250)
print('O desvio padrao diario da PG    e: ', sec_returns['PG'].std())
print('O desvio padrao da PG           e: ',
      sec_returns['PG'].std() * 250 ** 0.5)

# Calculando agora para a BEI.DE

print('\nA media diaria da BEI.DE         e: ', sec_returns['BEI.DE'].mean())
print('A media anual  da BEI.DE         e: ',
      sec_returns['BEI.DE'].mean() * 250)
print('O desvio padrao diario da BEI.DE e: ', sec_returns['BEI.DE'].std())
print('O desvio padrao da BEI.DE        e: ',
      sec_returns['BEI.DE'].std() * 250 ** 0.5)

# Vamos facilitar nossa analise imprindo as medias e os desvio dos ativos um abaixo do outro => observe

print('\nMedia anual da PG: ', sec_returns['PG'].mean() * 250)
print('Media anual da BEI.DE: ', sec_returns['BEI.DE'].mean() * 250)

# Formas mais elegantes => observe o uso de colchetes duplos [[]]

print('\nMedia anual dos ativos')
print(sec_returns[['PG', 'BEI.DE']].mean() * 250)
print('\nDesvio padrao anual dos ativos')
print(sec_returns[['PG', 'BEI.DE']].mean() * 250 ** 0.5)
