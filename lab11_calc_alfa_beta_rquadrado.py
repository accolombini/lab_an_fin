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

# Vamos agora calcular => Alfa, Beta e R quadrado o modulo statsmodel nos ajudara com a estatistica

# Precisamos de uma variavel, X1 que recebera o valor recem calculado
X1 = sm.add_constant(X)
# A variavel reg recebera o resultado de uma regressao de minimos quadrados OLS
# O metodo .fit() ira aplicar uma tecnica especifica para obter os ajustes para o modelo recem criado
reg = sm.OLS(Y, X1).fit()
# Aqui vamos poder visualizar o resultado da regressao de forma organizada (tres tabelas). Sao muitas as estatisticas, procure focar naquelas que sao relevantes para nosso estudo ate este momento
reg.summary()
print('\nResumo da OLS:')
print(reg.summary())

# Calculo do valor esperado de Y => a partir dos dados extraidos da tabela acima, vamos estimar o valor de uma casa de 1000m^2. Da tabela sabemos que Alfa e = 260800 e Beta = 402 => observe a simulacao a seguir e confira com os resultados no seu grafico. Note na tabela que temos um erro de 65.243 para mais e para menos

print('\nSimulacao considerando Alfa == 260800 e Beta == 402, para uma casa de 1000m^2: ',
      260800 + 402 * 1000)

# Calculo de Alfa, Beta e R^2 ==> olhando para a tabela e extraindo o que nos interessa agora usando a biblioteca scipy (stats.)==> observe a facilidade

slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
print('\nInclinacao da reta => Beta: ', slope)
print('Ponto de interceptacao => Alfa: ', intercept)
print('O valor de R: ', r_value)
print('O valor de R^2: ', r_value ** 2)
print('O valor de p sera explicado em outra aula: ', p_value)
print('O erro padrao: ', std_err)
