# Calculo do retorno esperado de uma acao => emprego do metodo CAPM <=> Para relembrar fixe os conceitos abaixo
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

# O metodo CAPM para o calculo do retorno de um ativo => continuaremos a partir do calculo do indice Beta. Vamos usar a seguinte formula => resperado = rf(taxa_livre_de_risco) + Beta(do_ativo)(rm(taxa_risco_mercado) - rf). Lemre-se => o termo (rm - rf) e tambem chamado de premio (equivale a um premio pelo risco que se esta disposto a correr ao investir no ativo)

# Calculo do retorno esperado por investir no ativo => o valor 0.025 ou 2.5% é o ativo considerado livre de risco escolhido, no caso Titulos do governo americano <=> https://www.bloomberg.com/markets/rates-bonds/government-bonds/us
# Pesquisas academicas mostram com um premio de risco entre 4.5% e 5.5% sao bem razoaveis para um investidor medio, neste caso vamos usar a media entre eles => 5% ou 0.05
PG_er = 0.025 + PG_beta * 0.05
print('O valor do retorno esperado ao investir no ativo PG => PG_er e: ', PG_er)
