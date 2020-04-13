# Monte Carlo => Black-Scholes-Merton >>= Nosso objetivo nesta pratica e calcular uma opcao de compra


import numpy as np 
import pandas as pd 
from pandas_datareader import data as wb
from scipy.stats import norm 

# d1 = (ln(s/K) + (r + stdev^2/2) * t)/ (s * sqrt(t))
# d2 = d1 - s * sqrt(t) = (ln(s/K) + (r - stdev^2/2) * t) / (s * sqrt(t))
# C = SN(d1) - Ke^(-rt) * N(d2)
# S -> Preco da acao; K -> preco de exercicio; r -> taxa livre de risco; stdev -> desvio padrao; T -> intervalo de tempo (anos)

def d1(S, K, r, stdev, T):
    return(np.log(S / K) + (r + stdev ** 2 /2) * T) / (stdev * np.sqrt(T))

def d2(S, K, r, stdev, T):
    return(np.log(S / K) + (r - stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))

# Usaremos aqui a distribuicao normal cumulativa (cdf) que nos mostra como os dados se acumulam no tempo e seu resultado nunca pode ser inferior a zero ou superior a 1 >>= o argumento que se passa para .cdf(arg) nos retorna o que temos abaixo deste valor, observe os exemplos a seguir. Observe especialmente o que acontece quando uso um argumento grande como 9 (poderia ser qualquer valor acima de 1, ok)
print('Valor acumulado abaixo de    0: ', norm.cdf(0))
print('Valor acumulado abaixo de 0.25: ', norm.cdf(0.25))
print('Valor acumulado abaixo de 0.75: ', norm.cdf(0.75))
print('Valor acumulado abaixo de    9: ', norm.cdf(9))

# C = SN(d1) - Ke^(-rt) * N(d2) ||> Vamos agora introduzir a esperada funcao de Black-Scholes-Merton

def BSM(S, K, r, stdev, T):
    return(S * norm.cdf(d1(S, K, r, stdev, T)) - (K * np.exp(-r * T) * norm.cdf(d2(S, K, r, stdev, T))))
# Continuamos com a PG
ticker = 'PG'
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source = 'yahoo', start = '2007-1-1', end = '2017-3-21')['Adj Close']
# O metodo .iloc[-1] ira nos trazer o preco atual da acao da PG
S = data.iloc[-1]
print('O valor atual da acao da PG |-> S e: ', S)
# Para o calculo do desvio padrao usaremos a aproximacao do retorno logaritmico |-> observe
log_returns = np.log(1 + data.pct_change())
stdev = log_returns.std() * 250 ** 0.5
print('O desvio padrao anualizado stdev: ', stdev)
# Vamos manter a taxa livre de Risco em 2.5% >>= vamos assumir que o preco em exercicio e 110 >>= vamos considerar o valor de T = 1
r = 0.025
K = 110.0
T = 1

de1 = d1(S, K, r, stdev, T)
print('\nO valor de d1 e: ', de1)
de2 = d2(S, K, r, stdev, T)
print('O valor de d2 e: ', de2)
bsm = BSM(S, K, r, stdev, T)
print('O valor da opcao de compra  |-> BSM e: ', bsm)
# Observe que ao executar varias vezes encontrara valores diferentes e nao se assuste se sua opcao de compra for um valor muito baixo, lembre-se que ele e uma funcao de varios fatores, normalmente se usa mais estatisitica para melhorar esses resultados, vamos fazer algo na proxima aula >>= nao perca
