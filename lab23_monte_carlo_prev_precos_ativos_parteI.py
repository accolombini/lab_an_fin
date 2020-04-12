# Neste laboratorio estaremos contruindo a primeira parte do previsor de valores futuros de um ativo utilizado simulacao de Monte Carlo. Nesta pratica estaremos trabalhando com a empresa PG, vamos avaliar como podemos trabalhar nosso previsor para esse ativo


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm

ticker = 'PG'
data = pd.DataFrame()
# Vamos estudar este ativo por 10 anos >=> conhecidos 2007 a 2017
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2007-1-1', end='2017-1-1')['Adj Close']

# Agora vamos estimar seu retorno logaritmico historico >=> vamos usar aqui o metodo porcent change .pct_change() <=> este metodo do numpy nos fornece o retorno simples a partir de uma base de dados, no caso nosso data
log_returns = np.log(1 + data.pct_change())
# Analisando os resultados
print('\nVamos visualizar seu retono logaritmco historico')
print(log_returns.tail())

# Agora vamos dar uma olhada graficamente no que temos => neste grafico podemos perceber que os precos da PG vem subindo gradualmente ao longo da decada apesar de uma queda drastica em 2009
data.plot(figsize = (10, 6))
plt.show()
# Neste segundo grafico iremos plotar os retornos logaritmos da PG => observe que este grafico nos diz que o ativo obedece uma distribuicao normal com uma media estavel
log_returns.plot(figsize = (10, 6))
plt.show()
# Na sequencia vamos calcular media variancia drift e desvio padrao |=> necessarios para os calculos do movimento Browniano
u = log_returns.mean()
print('O valor da media u       e: ', u)
var = log_returns.var()
print('O valor da variancia var e: ', var)

# Para o calculo do Drif vamos recordar |=> drift = u -0.5 * var >>= So para recordar o Drift e o melhor retorno das taxas futuras de retorno de uma acao. Observe que nao tentaremos anualizar os resultados => lembra multiplicar por 250? Isso porque queremos prever o preco DIARIO da acao da PG

drift = u - (0.5 * var)
print('O valor do Drift drif    e: ', drift)
# A variavel stdev recebera o desvio padrao calculado, assim podemos escrever que o Movimento Browniano e dado por: r = drift + stdev * e^r
stdev = log_returns.std()
print('O desvio padrao stdev    e: ', stdev)
# Nesta pratica criamos o primeiro elemento do movimento Browniano, na proxima aula vamos completar o processo
