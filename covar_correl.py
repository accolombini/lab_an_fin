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

# O método var() do pandas calcula a variância diretamente

PG_var = sec_returns['PG'].var()

print('\nVariancia PG dia: ', PG_var)
BEI_var = sec_returns['BEI.DE'].var()
print('Variancia BEI dia: ', BEI_var)
PG_var = sec_returns['PG'].var() * 250
print('\nVariancia PG anual: ', PG_var)
BEI_var = sec_returns['BEI.DE'].var() * 250
print('Variancia BEI anual: ', BEI_var)

# Com o método cov() do pandas iremos agora calcular a covariância de pares de colunas
# Para todas as matrizes => preste atenção aos resultados na diagona principal e no caso
# fique atento as outras colunas, no caso, nossa matriz e 2x2 observe a diagonal secundaria
# Como dica => na diagonal principal teremos a variância e na diagonal secundária a covariância
# Para grandes matrizes => o restante da matriz é preenchida com a covariancia entre elas (ativos analisados)

cov_matrix = sec_returns.cov()
print('\nMatriz de covariancia => diaria')
print(cov_matrix)
cov_matrix_a = sec_returns.cov() * 250
print('\nMatriz de covariancia => anual')
print(cov_matrix_a)

# Com o método corr() do pandas estaremos calculando a correlação de pares de colunas
# Atenção! correlação entre preços de ativos e correlação de retorno de ativos possuem resultados diferentes
# Fique atento, você não deve analisar a matriz de correlação e ela não deve ser multiplicada por 250

corr_matrix = sec_returns.corr()
print('\nMatriz de correlacao')
print(corr_matrix)

# Nunca se esqueca => um investidor esta interessado no retorno das acoes e nao nos precos das acoes
# Assim, cabe ao analista a interpretacao dos resultados, isso nao e competência do Python, ok!
