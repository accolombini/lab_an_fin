# As regressoes multivariadas extendem a regressao monovariavel e considerar um conjunto maior de variaveis explicativas <=> Ao aumentar o numero de variaveis explicativas queremos entender com maior precisao a influencia das variaveis explicativas no evento que estamos querendo prever
# </> Uma regressao que considera multiplas variaveis deve fornecer uma previsao mais proxima dos resultados reais >>= nem sempre essa e uma tarefa trivial, muitas vezes serao necessarias muitas simulacoes para encontrar o conjunto otimo de variaveis que contribuem/influenciam no preco do ativo que se deseja prever </> Em outras palavras, precisamos encontrar as variaveis certas
# Para relembrar vamos reescrever a formula da Regressao Simples => Yi = ß0 + ß1Xi + εi >>= onde εi e o residuo e temos apenas uma variavel explicativa (X1)
# o que vamos implementar neste laboratorio e >>= Yi = ß0 +ß1X1 + ß2X2 + ß3X3 + εi => equacao para enontrar a regressao multivariada, observe a presenca de multiplos coeficietes beta e muitas variaveis explicativas (X1, X2, X3). |> Cabe ao analista definir o numero e quais sao as variaveis explicativas para o ativo em questao ||> este e um ponto que demanda muita atencao e exercicio/simulacao
# Uma regressao multivariada busca identificar a melhor linha de tendencia que minimiza a soma dos quadados dos residuos em multiplas dimensoes
# Assim como vimos antes o R^2 ira nos ajudar a determinar o quao poderosa a regressao e |||> o R^2 varia de 0 |-> 1 e esperamos que quanto maior o numero de variaveis, maior deva er o valor de R^2
# Ha duas maneiras de avaliar se uma variavel explicativa e util ~~> primeiro realizamos uma regressao com a variavel presente e depois executa-se a mesma regressao sem a presenca da variavel ou com uma variavel diferente e analisar o comportamento do R^2 |||> se ele R^2 for mais alto na primeira vez significa que a variavel tem potencial explicativo  e seu valor contribui para explicar o comportamento da variavel independente => deve-se continuar investigando ~~> na segunda forma, podemos comparar os p-valores dos coeficientes beta (a probabilidade de que os coeficientes beta deveriam ser diferentes). Em estatistica o p-valor e a possibilidade de encontrarmos um valor mais extremo que aquele que obtivemos, em outras palavras, essa e a probabilidade de que os coeficientes ß que estimamos devam ser diferentes ||> um p-valor baixo e uma coisa boa, ele fornece garantia de que o verdadeiro coeficiente ß difere de 0 e nos ajuda a explicar a variavel dependente => em outras palavras, ele indica que ha uma chance pequena dos coeficientes ß que estimamos sejam diferentes </> Como podemos dizer se uma variavel explicativa melhora o poder preditivo de um modelo?|||> um p-valor inferior a 5% nos permite afirmar que podemos estar 95% confiantes de que o coeficiente ß que estimamos e diferente de 0 >>= geralmente aceita-se p-valor inferior a 5%, se for concervador busque por p-valor inferior a 1%
# Coeficiente Beta ß estimados em uma regressao multivariada podem ser interpretados como o impacto marignal da variavel explicativa tem sobre uma variavel dependente, mas isso so sera verdade <=> se todas as outras variaveis permanecerem constantes
# Imagine que numa regressao multipla você encontrou ß1 = 0.8X1 e ß2 = 1.2X2 como podemos interpretar esse resultado? ~~> isso siginifica que para cada 1% de aumento da variavel X1 podemos esperar um ganho de 0.8% de X2 se o crescemento de X2 permanecer o mesmo => neste caso temos uma interrelacao forte entre as variaveis e nao podemos interpretar um sem o outro

# </> Agora vamos avaliar como podemos resolver isso usando Python

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = pd.read_excel('D:/teste/FIN_DATA/Housing.xlsx')
print('Olhando por dentro de nossos dados >=> Housing.xlsx')
print(data)

# Regressao multivariavel >=> House Size, Number of Rooms e Year of construction (variaveis escolhidas para nossa analise)

X = data[['House Size (sq.ft.)', 'Number of Rooms', 'Year of Construction']] # variaveis independetes
Y = data['House Price'] # Variavel dependente

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit() # Regressao de minimos multiplos quadrados
print('O quadro resumo da regressao >=> OLS pode ser visto a seguir')
print(reg.summary())

# Variaveis independetes => House Size (sq.ft.) Number of Rooms

X = data[['House Size (sq.ft.)', 'Number of Rooms']]
Y = data['House Price']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit() # Regressao de minimos multiplos quadrados
print('O quadro resumo da regressao >=> OLS pode ser visto a seguir')
print(reg.summary())

# Variaveis independetes => House Size (sq.ft.) Year of Construction

X = data[['House Size (sq.ft.)', 'Year of Construction']]
Y = data['House Price']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit() # Regressao de minimos multiplos quadrados
print('O quadro resumo da regressao >=> OLS pode ser visto a seguir')
print(reg.summary())

# Variaveis independetes => Number of Rooms Year of Construction

X = data[['Number of Rooms', 'Year of Construction']]
Y = data['House Price']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit() # Regressao de minimos multiplos quadrados
print('O quadro resumo da regressao >=> OLS pode ser visto a seguir')
print(reg.summary())

# Tente interpretar os resultados com base em tudo o que aprendeu
# Algo para refletir => 1- Reunir mais dados sobre mais observacoes pode ser interessante?
# 2- Observe que o p-valor de Tamanho da Casa e Numero de quartos foi igual a zero => o que isso significa?
# 3- Reunir dados sobre outras variaveis explicativas como distância entre o imovel e o centro da cidade; a existencia ou nao nas proximidades de supermercados, escolas, etc. Podem influenciar no preco do imovel?
# 4- Por fim o que voce acha do tamanho da casa como influenciador de seu valor => lhe parece uma boa variavel?
# 5- Por fim uma conclusao => regressoes demandam esforco e podem nos dar uma boa direcao para pesquisas futuras! Analise de regresao pode ser inestimavel quando estudamos o passado para prever um comportamento futuro => portanto, procure nao abrir mao desse recurso a seu favor
