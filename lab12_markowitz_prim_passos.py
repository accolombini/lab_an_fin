# Fronteira Eficiente de Markowitz --> Parte 1
# Nesta fase estamos desenvolvendo principalmente um processo para gerar valores randomicos que somem 1 para sua carteira . Até aqui não houve preocupação com o número de iterações, na prática, deve-se executar N vezes até que se encontre o ponto ótimo de distrubuição de ativos para sua carteira

import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# Definicao do ticket a ser estudado
# Queremos encontrar a Fronteira Eficiente de Markowitz => usando Python

assets = ['PG', '^GSPC']
pf_data = pd.DataFrame()
for a in assets:
    pf_data[a] = wb.DataReader(
        a, data_source='yahoo', start='2010 - 1 - 1')['Adj Close']
print('\nDados da carteira o importante e que todos os tickets tenham mesma quantidade de informacao')
print(pf_data.info())

print('\nOlhando para os dados para uma inspecao aos dados reais')
print(pf_data.head())
print(pf_data.tail())

# Normaliza-se os dados para a base 100 e plota o grafico para inspecao visual

print(plt.show((pf_data / pf_data.iloc[0] * 100).plot(figsize=(10, 5))))

# Calculo da variacao logaritmica => media anual e covariancia anual

log_returns = np.log(pf_data / pf_data.shift(1))
print('\nRetorno logaritmico: ')
print(log_returns)

print('\nO Retorno medio anual-> Observe a consistencia nos retornos')
print(log_returns.mean() * 250)

print('\nA Covariancia anual -> observe a consistencia no retorno dos ativos >= 30%')
print(log_returns.cov() * 250)

print('\nA correlacao entre os ativos -> observe a diagonal secundaria')
print(log_returns.corr())

# Vamos calcular o numero de ativos da carteira => situacao generica
num_assets = len(assets)
print('\nQuantidade de ativos na carteira: ', num_assets)

# Vamos precisar de pesos para nossa carteira => faremos isso gerando randomicamente -> fique atento, da forma como esta a funcao nào retorna soma 1 e precisamos que a soma dos pesos de nossa carteira sejam 1
arr = np.random.random(2)
print('Array com os pesos gerados randomicamente: ', arr)
print('Soma dos pesos gerados: ', arr[0] + arr[1])
print('Teste soma igual a 1: ', (arr[0] + arr[1]) == 1)

# Forma correta para gerar pesos randomicos para uma carteira de ativos
# Observe que weights e um vetor numpy (e isso fara toda a diferenca nas operacoes a seguir) agora e recebe neste caso dois valores randomicos weights[0] e weights[1]
weights = np.random.random(num_assets)
# Aqui esta o segredo ==> equivale a seguinte operacao: weights = weights/sum(weights) => lembrando que se trata de operacao de matrizes
# Na pratica o comando a seguir aplica a seguinte transformacao chamando weights de w e weights[0] = w1 e weights[1] = w2 temos que: w1/(w1 + w2) + w2/(w1 + w2) = (w1 + w2)/(w1 + w2) = 1. Que e o valor desejado, assim observe
weights /= np.sum(weights)
print('Matriz com os pesos: ', weights)
print('A soma correta dos pesos e: ', weights[0] + weights[1])
print('Teste soma igual a 1: ', (weights[0] + weights[1]) == 1)
