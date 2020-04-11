# Calculo do Beta de uma acao => analisando a volatilidade dos ativos
# Beta = 0 => não sofre interferencia do mercado
# Beta <= 1 => ativo de baixo risco (pouco volátil)
# 1 < Beta <= 2 => ativo de alto risco (mais volatil quanto mais se aproxima de 2)
# O Beta normalmente é medido com base nos dados dos últimos 5 anos => ele mede ate que ponto o preco de um ativo esta relacionado com a flutuacao do mercado
# o Beta e uma fracao dada por => Beta = (cov(PG, mkt))/(var(mkt)) <=> Nesta simulacao estaremos comparando o ativo PG com o mercado representao pelo S&P500 => ^GSPC


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# Definicao do ticket a ser estudado
# Queremos encontrar o Beta de um ativo => usando Python

tickers = ['PG', '^GSPC']
data = pd.DataFrame()
for t in tickers:
    data[t] = wb.DataReader(
        t, data_source='yahoo', start='2016-1-1', end='2019-12-31')['Adj Close']
print('\nDados da carteira o importante e que todos os tickets tenham mesma quantidade de informacao')
print(data.info())

print('\nOlhando para os dados para uma inspecao aos dados no site')
print(data.head())
print(data.tail())

# Estamos interessados na variancia e na covariancia dos dois ativos => Beta =

sec_returns = np.log(data / data.shift(1))
print('\nRetorno logaritmico: ')
print(sec_returns)

print('\nA Covariancia anual -> queremos criar uma matriz de covariancia entre PG e S&P500 => usamos o metodo cov()')
cov = sec_returns.cov() * 250
print(cov)

# Agora com a ajuda do metodo .iloc() vamos obter a relacao entre a acao PG e o mercado S&P500 com um valor de float => com isso fechamos o calculo do numerador
cov_with_market = cov.iloc[0,1]
print('Relacao entre a PG e o S&P5OO como float: ', cov_with_market) 
# Precisamos agora calcular o denominador de nosso Beta => que e dado pela variancia anualizada do mercado (S&P500)
market_var = sec_returns['^GSPC'].var() * 250
print('Variancia anualizada do mercado S&P500: ', market_var)

# De posse do numerador e denominador => estamos prontos para calcular o valor de Beta da PG => sempre verifique o valor encontrado com o valor no site <-> importante para validar seu trabalho

PG_beta = cov_with_market / market_var
print('O valor calculado de Beta para a PG: ', PG_beta)
