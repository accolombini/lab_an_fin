# Investidores racionais querem ser capazes de comprar acoes em termos do desempenho da relacao risco-retorno. Eles buscam, maximizar seu retorno minimizando seus riscos => Foi assim que William Sharpe surgiu com o Indice de Sharpe que uma otima maneira de fazer uma comparacao adequada entre acoes e portifolios e decidir qual e melhor entre risco-retorno
# A formula para o calculo do indice de Sharpe e a seguinte => SharpeRatio = (ri -rf) / σi, onde:
# ri - rf <=> excesso de retorno da acao i
# rf => retorno livre de risco
# ri => retorno da acao i
# desvio padrao da acao 'i' => σi desvio padrao da acao i
# Observe que se aumentarmos a taxa de retorno de uma acao o seu indice Sharpe ira aumentar, por outro lado, se aumentarmos o desvio padrao de uma acao σi seu indice Sharpe ira diminuir
# O indice Sharpe nos permite comparar >>= Acao A x Acao B >>= Carteira de investimentos A x Carteira de investimento B

# Partindo do que ja sabemos |||> </>

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

# </> |||> Vamos agora calcular o indice Sharpe em relacao ao mercado aqui representado pelo S&P500 ^GSPC

# Vamos usar a formula >>= Sharpe = (ri - rf) / σi |> observe que estamos falando do desvio padrao anualisado da acao. Usarems o metodo .std() para obtermos a volatilidade

# Podemos usar esse indice calculado quando quisermos comparar com outra acao/portfolio
Sharpe = (PG_er - 0.025) / (sec_returns['PG'].std() * 250 ** 0.5)
print('O indice Sharpe da acao analisada PG e: ', Sharpe)
