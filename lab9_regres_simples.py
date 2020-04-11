import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = pd.read_excel('D:/teste/FIN_DATA/Housing.xlsx')
print('Imprime o data como pandas')
print(data)
data[['House Price', 'House Size (sq.ft.)']]

# Calculo da Regressao monovariavel
# Vamos trabalhar com o modulo de regressao dos minimos multiplos quadrados ordinarios => OLS

# X sera nossa variavel independente => tamanho da casa
X = data['House Size (sq.ft.)']
# Y sera nossa variavel dependente => preco da casa
Y = data['House Price']

# Resumindo => queremos a partir da variavel tamanho da casa encontrar seu preco

print('\nO valor da variavel X: ')
print(X)
print('O valor da variavel Y: ')
print(Y)

# Com o matplotlib vamos plotar o grafico de dispersao => interessante para nosso estudo

# Importante => observe que testei várias impressoes de graficos, isso e importante, pois em algum momento podemos ser enganados a respeito da decisao a tomar => fique atento

print(plt.show(plt.scatter(X, Y)))

plt.scatter(X, Y)
plt.axis([0, 2500, 0, 1500000])
print(plt.show())

plt.scatter(X, Y)
plt.axis([0, 2500, 0, 1500000])
plt.ylabel('House Price')
plt.xlabel('House Size (sq.ft.)')
print(plt.show())
