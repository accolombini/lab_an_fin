# Fronteira Eficiente de Markowitz --> Parte 3
# Nesta fase finalmente iremos plotar o grafico da fronteira eficiente de Markowitz

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

# Retorno esperado do Portfolio => observe o uso do método .sum() do numpy que permite a soma de objetos multidimensionais
print('\nValor anaul medio esperado para o portifolio: ', np.sum(weights * log_returns.mean()) * 250)
# Variancia esperada do Portfolio
print('Variancia padrao anual esperado para o portifolio: ', np.dot(weights.T, np.dot(log_returns.cov() * 250, weights)))

# Volatilidade esperada do Portifolio
print('Volatilidade anual do Portfolio: ', np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))))

# Vamos agora preparar as 1.000 iteracoes -> posteriormente estaremos plotando esse grafico, por hora fique atento ao processo => Estamos aqui considerando 1.000 diferentes combinacoes dos mesmos dois ativos de nossa carteira => A ideia sera comparar os portfolios e encontrar o mais eficiente
# Observe que estamos comecando as duas listas vazias

pfolio_returns = []
pfolio_volatilities = []
for x in range(1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    # Observe que estamos aqui usando as mesmas formulas usadas acima
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))))

print('\nPrimeira forma de tratamento do dados -> vamos gerar duas listas')
print(pfolio_returns, pfolio_volatilities)

# Feito o passo acima, vamos agora melhorar sua exibição explorando mais um pouco o numpy => observe como convertemos as listas acima num arrau numpy

pfolio_returns = []
pfolio_volatilities = []
for x in range(1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    # Observe que estamos aqui usando as mesmas formulas usadas acima
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))))
# Aqui esta o que muda importante <=> fique atento
pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)

print('\nSegunda forma usada para tratar os dados -> vamos gerar duas listas')
print(pfolio_returns, pfolio_volatilities)

# Finalmente vamos plotar a fronteira Eficiente de Markowitz e => Isso vale um premio Nobel em Financas <-> vamos a ele

print('\nVamos comecar criando um objeto do tipo DataFrame contendo duas colunas. Uma coluna para os Retornos e a outra para as respectivas Volatilidades => Esses dados serao chamados de Portifolio')

# Observe que usaremos um dicionario (chave/valor) para compor a estrutura do nosso Portfolio

portfolios = pd.DataFrame({'Return': pfolio_returns, 'Volatility': pfolio_volatilities})

print('\nVamos olhar um pouco mais de perto uma amostra destes dados => head')
print(portfolios.head())
print('\nVamos olhar um pouco mais de perto uma amostra destes dados => tail')
print(portfolios.tail())

print('\nObserve graficamente a fronteira de Markowitz')

front_ef_mark = portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10,6))
plt.title('Fronteira Eficiente de Marcowitz')
plt.xlabel('ExpectedVolatility')
plt.ylabel('Expected Return')
plt.show(front_ef_mark)
