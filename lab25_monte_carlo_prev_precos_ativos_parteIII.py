# Neste laboratorio estaremos finalizando nosso previsor de valores futuros de um ativo utilizado simulacao de Monte Carlo. Nesta pratica continuamos trabalhando com a empresa PG, vamos avaliar como podemos trabalhar nosso previsor para esse ativo


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm

ticker = 'PG'
data = pd.DataFrame()
# Vamos estudar este ativo por 10 anos >=> conhecidos 2007 a 2017
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2007-1-1', end='2017-1-1')['Adj Close']

print('\nVamos fazer uma inspecao visual nos precos das acoes da PG')
print(data.tail())
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

# Nesta segunda parte daremos continuidade ao que estudamos na aula passada e vamos finalizar nosso previsor de precos futuros de um ativo utilizando simulacao de Monte Carlo

# Vamos usar a funcao type pois queremos visualizar que drift e stdev sao series do pandas
print('\nTipo de dado que temos na variavel drift: ', type(drift))
print('Tipo de dado que temos na variavel stdev: ',type(stdev))
# Uma vez que foram confirmados como series do pandas queremos agora converte-los para um array numpy => ao digitarmos .values depois de um objeto estaremos transferido o objeto para um array numpy observe os passos que foram precisos para isso
print('\nValor de drift convertido para array numpy: ', np.array(drift)) # Forma 1
print('Valor de drift convertido para array numpy: ', drift.values) # Forma 2
print('Valor de stdv convertido para array  numpy: ', stdev.values)
# O segundo componente do movimento Browniano e a variavel aletatoria Z que corresponde a distancia entre a media e os eventos, expresso pelo numero de desvios padrao. A funcao norm do scipy nos permite obter esse resultado. Vamos considerar que o evento possui 95% de chance de ocorrer e calcularmos sua distancia a media |=> o rsultado sera o numero de desvios padrao
print('O numero e desvios padrao considerando uma probabilidade de 95% e: ', norm.ppf(0.95))
# Para obter nosso segundo elemento precisaremos de uma matriz 10 x 2 de numeros aleatorios |=> isso nos permitira atribir para cada elemento do vetor acima um componente de x >>= essa matriz sera inserida para o calculo da variavel aleatoria Z
x = np.random.rand(10, 2)
print('\nMatriz de numeros randomicos gerada para os caluclos da variavel aleatoria Z')
print(x)
# O primeiro numero da primeira coluna corresponde a primeira probabilidade do vetor x e assim por diante
print('\nEmprego do modulo norm de scipy para associar as probabilidades linha a linha com a matriz x gerada aleatoriamente')
print(norm.ppf(x))
# O segundo componente do movimento Browniano e a variavel aletatoria Z que corresponde a distancia entre a media e os eventos, expresso pelo numero de desvios padrao. A funcao norm do scipy nos permite obter esse resultado. Observe que para o calculo de Z estamos pegando o rezultado do gerador de numeros aleatorios e aplicando-os ao metodo norm.ppf para o calculo das distancias em relacao a media zero medida pelo numero de desvios padrao
Z = norm.ppf(np.random.rand(10, 2))
print('\nImpressao da matriz de variaveis aleatorias => matriz Z')
print(Z)
# Estamos definindo nosso intervalo em 1000 >=> pois queremos prever o preco da Acao da PG para os proximos 1000 dias => faremos 10 iteracoes em outras palavras teremos 10 series de previsao futura para os precos das acoes
t_intervals = 1000
iterations = 10
# Recordando temos que => a variavel daily_returns = e^r e >>= r = drift + stdev - Z
# Vamos usar para isso a funcao numpy.exp() que calcula >>= e^(expressao) |=> devemos conseguir com isso uma matriz de 10 colunas por 1000 linhas ||> significando 10 previsoes para os proximos 1000 dias
daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
print('\n Impressao da matriz de 1000 x 10 com as previsoes dos precos das acoes da PG para os proximos 1000 dias')
print(daily_returns)

# Vamos agora levantar os precos para a acao da PG para o proximos 1.000 acompanhe

# Para recordar, vaos precisar da seguinte equacao => St = S0*daily_returnt >=> St+1 = St*daily_returnst+1 ...
# Definiremos com preco inicial o ultimo valor visto na aula anterior que corresponde ao valor de mercado no dia de hoje (observe o grafico) |=> por isso o uso do .iloc[-1]
S0 = data.iloc[-1]
print('\nO valor inicial para o nosso previsor S0 e: ', S0)

# Precisamos criar agora uma lista com as mesmas dimensoes da nossa lista anterior e preenche-la com zeros |=> observe como podemos fazer isso facilmente usando o metodo numpy .zeros_like() >>= note que passamos por parametro a variavel daily_return (nossa variavel de retornos diarios de 1000 x 10)
price_list = np.zeros_like (daily_returns)
print('\nPara uma inspecao visual nossa lista preencida com zeros => confira')
print(price_list)

# Agora vamos atribuir a primeira linha de nossa lista o ultimo valor calculado na ultima aula >>= em seguida faremos um loop para preencher essa matriz com os valores esperados para a acao da PG
price_list[0] = S0
print('\nVamos conferir nossa lista')
print(price_list)
for t in range(1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_returns[t]
print('\nFaremos agora uma inspecao visual na nossa lista >>= observe')
print(price_list)
print('\nVamos agora realizar uma inspecao visual no nosso previsor |=>> observe')
plt.figure(figsize=(10, 6))
plt.plot(price_list)
plt.show()
