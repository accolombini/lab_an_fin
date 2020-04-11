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
print('\nPeso weights[0]: ', weights[0])
print('Peso weights[1]: ', weights[1])

# Calculo da variancia do portfolio
# A seguir fazemos um produto de matrizes (ab)**2 usando numpy => observe a simplicidade quando se usa numpy.dot()

pfolio_var = np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))
print('\nVariancia do Portfolio: ', pfolio_var)

# Calculo do Risco diversificavel => risc_diver
# Risco diversificavel = variancia do portfolio - variancia anual ponderada

PG_var_a = sec_returns[['PG']].var() * 250
print('\nExibe a variancia da PG ', PG_var_a)
BEI_var_a = sec_returns[['BEI.DE']].var() * 250
print('Exibe a variancia da BEI.DE ', BEI_var_a)
# Fique atento esse foi um artifico para contornar problemas com o numpy => a funcao float() ira transformar o array numpy em um float
print(float(PG_var_a))
# Observe que estaremos usando colchetes simples ['PG'] => queremos um numero decimal, ok
PG_var_a = sec_returns['PG'].var() * 250
print('\nVariancia da PG: ', PG_var_a)
BEI_var_a = sec_returns['BEI.DE'].var() * 250
print('Variancia da BEI_DE: ', BEI_var_a)
# Calculo do Risco diversificavel ou nao sistematico
dr = pfolio_var - (weights[0] ** 2 * PG_var_a) - (weights[1] ** 2 * BEI_var_a)
print('\nO valor do risco diversificavel e: ', dr)
print('Melhorando um pouco a visualizacao do risco diversificavel: ',
      str(round(dr * 100, 3)) + '%')

# Calculo do Risco Sistematico ou Risco Diversificavel
# Temos duas formas para calcular o Risco Sistematico, observe os resultados a seguir

# Primeira forma => Basta subtrair o Risco nao sistematico de toda variancia
n_dr_1 = pfolio_var - dr
print('\nImprime Risco Sist por n_dr_1: ', n_dr_1)
# A outra forma consite na soma ponderada de toda variancia
n_dr_2 = (weights[0] ** 2 * PG_var_a) + (weights[1] ** 2 * BEI_var_a)
print('Imprime Risco Sist por n_dr_2: ', n_dr_2)
print('\nImprime a comparacao das variaveis devemos esperar por True: ', n_dr_1 == n_dr_2)
