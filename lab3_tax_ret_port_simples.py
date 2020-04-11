import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


tickers = ['PG', 'MSFT', 'F', 'GE']
mydata = pd.DataFrame()
for t in tickers:
    mydata[t] = wb.DataReader(t, data_source='yahoo',
                              start='1995-01-01')['Adj Close']

print('\nDados da carteira o importante e que todos os tickets tenham mesma quantidade de informacao')
print(mydata.info())
print(mydata.head())
print(mydata.tail())

# Normalizando os dados P1/P0 *100 --> Normalizando para a BASE 100

# iloc[0] o indexador iloc com índice 0 fixa a linha [0] para extrair os dados da primeira linha da tabela
mydata.iloc[0]
(mydata / mydata.iloc[0] * 100).plot(figsize=(15, 6))
plt.show()

# Efeito da não normalização dos dados --> observe os gráficos (eles não partem da mesma referência)
mydata.plot(figsize=(15, 6))
plt.show()

# Requisito para o uso do .loc() precisamos fixar um rótulo de início, o rótulo deve corresponder à primeira linha
mydata.loc['1995-01-03']
# Para usar o .iloc() é preciso indicar a posição de interesse, no caso, 0 ou seja, a primeira linha
mydata.iloc[0]

# A seguir o cálculo do Retorno Simples de um Portifólio de Ações

returns = (mydata / mydata.shift(1)) - 1
print(returns.head())

#   Supondo que os pesos das ações sejam iguais (isso nunca é o caso, mas vale o aprendizado)

# Criação de uma matriz numpy --> a soma dos pesos das ações deve ser 1
weights = np.array([0.25, 0.25, 0.25, 0.25])
# O método numpy.dot permite o cáculo vetorial (não é preciso iterar) de vetores ou matrizes  de matrizes de uma forma bem rápida
np.dot(returns, weights)

# Retorno médio anual

annual_returns = returns.mean() * 250
print('\nExibe o retorno anual das acoes\n')
print(annual_returns)

# Retorno anual com três casas decimais

np.dot(annual_returns, weights)
pfolio_1 = str(round(np.dot(annual_returns, weights), 5) * 100) + "%"
print(
    '\nA taxa de retorno simples do portifolio_1 [PG, MSFT, F, GE] = ', pfolio_1)

# Vamos agora simular uma variação nos pesos desta mesma carteira e avaliar os retornos

weights_2 = np.array([0.4, 0.4, 0.15, 0.05])
pfolio_2 = str(round(np.dot(annual_returns, weights_2), 5) * 100) + "%"

print(
    'A taxa de retorno simples do portifolio_2 [PG, MSFT, F, GE] = ', pfolio_2)
