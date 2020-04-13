# Monte Carlo => Discretizacao de Euler Parte II >>= vamos nessa pratica calcular o preco de uma opcao de compra de uma forma mais sofisticada ||> acompanhe |-> usaremos os mesmos dados para que voce possa comparar os resultados com o resultado encontrado na pratica anterior


import numpy as np 
import pandas as pd 
from pandas_datareader import data as wb
from scipy.stats import norm
import matplotlib.pyplot as plt


# Continuamos com a PG
ticker = 'PG'
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source = 'yahoo', start = '2007-1-1', end = '2017-3-21')['Adj Close']
# O metodo .iloc[-1] ira nos trazer o preco atual da acao da PG
S = data.iloc[-1]
print('O valor atual da acao da PG |-> S e: ', S)
# Como estamos trabalhando com uma unica acao e apropriado trabalhar com o retorno logaritmico => lembra disso? ok entao |> acompanhe
log_returns = np.log(1 + data.pct_change())
# Observe que agora estamos usando uma formula mais sofiticada para o calculo da opcao de compra, mais que isso, queremos simular muitas e muitas vezes na busca de melhores resultados >=> observe a seguir. As simulacoes de Monte Carlo podem nose opcao de compra |||> nos poderiamos calcular a media do payoff e desconta-lo para hoje. A formula apresentada a seguir nada mais do que uma outra versao do movimento Browniano => esta abordagem recebe o nome de Discretizacao de Euler
# St = St-1 * e^((r - 0.5 * stdev^2) * δt + stdev * srqt(δt) * Zt)

# Vamos considerar os valores abaixo para as variaveis r e T

r = 0.025
stdev = log_returns.std() * 250 ** 0.5
print('\nO desvio padrao stdev ', stdev)
print('Verificando o tipo de stdev: ', type(stdev))
# lembra de artificio de conversao? Verificamos se se trata de uma serie pandas e queremos que ela seja convertida para um array numpy. object.values >>- transfere o objeto para um array numpy
stdev = stdev.values
print('\nO valor de stdev convertido: ', stdev)
# Como estamos trabalhando com um horizonte de um ano, vamos atribuir a t_intervals o valor de 250 (numero de dias de pregao em um ano tipico)
T = 1.0
t_intervals = 250
delta_t = T / t_intervals
# Vamos iniciar com 10000 iteracoes para encontrarmos nosso valor Z
iterations = 10000
# Observe que estamos gerando numeros randomicos dentro de uma distribuicao normal
Z = np.random.standard_normal((t_intervals + 1, iterations))
# O metodo zeros_like nos permite criar um array de mesma dimensao preenchido com zeros
S = np.zeros_like(Z)
# Usamos o metodo .iloc[-1] para preenchermos a primeira linha da serie com o ultimo valor da Acao
S0 = data.iloc[-1]
S[0] = S0

# Vamos agora compor nossa equacao no Python >>= St = St-1 * e^((r - 0.5 * stdev^2) * δt + stdev * srqt(δt) * Zt)
# Esta simulacao nos dara uma matriz 251 linhas x 10.000 colunas
for t in range(1, t_intervals + 1):
    S[t] = S[t-1] * np.exp((r - 0.5 * stdev ** 2) * delta_t + stdev * delta_t ** 0.5 * Z[t])

print('\nO valor de S simulado >>= S: ', S)

print('\nImprimindo a dimensao de S.shape: ', S.shape)

plt.figure(figsize=(10, 6))
# Observe que : siginifica que estamos plotando as 251 linhas, mas :10 significa que estamos plotando apenas os 10 primeiros resultados das 10.000 colunas >>= e uma forma de restringirmos a dimensao do grafico -> voce podera brincar com isso explorando outros valores, ok
plt.plot(S[:, :10])
plt.show()

# INICIO DA PARTE II
# Monte Carlo => Discretizacao de Euler Parte II => Vamos calular o payoff de uma opcao de compra
# Opcao de Compra => Voce exerce seu direito de Compra se >>= S -K > 0 e => Voce nao exerce seu direito de compra se S - K < 0 sabendo que S => preco da acao e K => preco de exercicio

# Vamos usar o metodo numpy chamado .maximum() que irá criar um array que contem Os ou os numeros iguais as diferencas  ela e necessaria para termos um array de mesma dimensao >>= a esta variavel damos o nome de p de payoff
p = np.maximum(S[-1] - 110, 0)
print('\nA matriz payoff p e: ', p)
p.shape
print('Observe que p e do mesmo comprimento de S : ', p.shape)

# A formula para descontar a media e dado por >>= C = (e^(-r*T) * Σ pi) / iterations
C = np.exp(-r * T) * np.sum(p) / iterations
print('O valor da opcao de compra => C e: ', C)
# Avalie se este metodo e o anterior (formula Browniano original lab_27) divergem tanto assim e tire suas conclusoes a cerca do metodo de calculo a ser utilizado
