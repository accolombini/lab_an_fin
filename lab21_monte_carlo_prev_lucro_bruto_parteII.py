# Simulacao de Monte Carlo aplacada na previsao do lucro bruto >=> Parte II


import numpy as np
import matplotlib.pyplot as plt

rev_m = 170 # Receita media
rev_stdev = 20 # Significa o desvio padrao da receita
iterations = 1000 # Quantidade de iteracoes que nos ajudarao em nossa distribuicao normal

# A seguir aplicamos o gerador de receitas futuras (simulando as 1.000 iteracoes) => estaremos usando numpy com o gerador randomico parra isto, observe a seguir. Observe os valores (1.000) que devem estar todos em torno da media
rev = np.random.normal(rev_m, rev_stdev, iterations)
print(rev)

# Para melhor visualizar a variacao dos valores gerados vamos plotar o grafico desses valoeres => observe que os valores devem estar centrados na media de 170 e numa variacao de +/- 20 em relacao a este valor medio o que equivale a media +/- o 1 desvio padrao
plt.figure(figsize=(15,6))
plt.plot(rev)
plt.show()

# Vamos agora avaliar o impacto destes dados no Custo das Mercadorias Vendidas CMV => COGS do Ingles => na pratica uma boa aproximacao seria esperar algo em torno de 60% da receita da empresa => uma empresa bem dimensionada estaria gastando em torno de 60% de sua receita para produzir a mercadoria vendida. Isso e feito levando-se em conta os dados historicos da empresa => nao e um chute. Com base ainda na analise historica podemos considerar a receita media de 60% com um desvio padrao em torno da media de +/- 10%
# Observe que COGS e dinheiro gasto dai o sinal de menos (-) antes do parenteses >=> observe que nao faremos 1.000 iteracoes para o COGS, mas sim vamos atribuilo a cada uma das 1.000 itercoes ja realizadas observe o (rev * np.random.normal(0.6, 0.1)) 0.6 60% (valor esperado da receita) e 0.1 10% (desvio padrao)
COGS = - (rev * np.random.normal(0.6, 0.1))

plt.figure(figsize=(15,6))
plt.plot(COGS)
plt.show()

print('O valor medio de COGS:  ', COGS.mean())
print('O desvio padrao de COGS: ', COGS.std())

# Nosso objetivo e o calculo do lucro bruto => a Receita menos o Custo das Mercadorias Vendidas CMV => COGS do Ingles nos fornece o Lucro bruto, lembre-se que criamos o COGS com sinal negativo (-) para o calculo do Custo das Mercadorias Vendidas, por isso estamos usando o sinal (+) aqui >=> acompanhe />
Gross_Profit = rev + COGS
print('O valor de Gross_Profit </>')
print(Gross_Profit)

plt.figure(figsize=(15,6))
plt.plot(Gross_Profit)
plt.show()

# A seguir vamos calcular os valores maximos, minimos, o valor medio e o desvio padrao do Lucro Bruto => acompanhe
print('O valor maximo do  Lucro Bruto: ', max(Gross_Profit))
print('O valor minimo do  Lucro Bruto: ', min(Gross_Profit))
print('O valor medio do   Lucro Bruto: ', Gross_Profit.mean())
print('O desvio padrao do Lucro Bruto: ', Gross_Profit.std())

# Vamos agora colocar esses resultados num histograma para que possamos observar sua distribuicao >-> acompanhe
plt.figure(figsize=(15, 6))
plt.hist(Gross_Profit, bins = [40, 50, 60, 70, 80, 90,100, 110, 120])
plt.show()
# Se ainda não foi possivel identificar a distribuicao normal, podemos lancar mao de uma distribuicao em frequencia e deixar que o Python faca o trabalho para nos, no caso estamos usando bins = 20, observe o resultado
plt.figure(figsize=(10, 6))
plt.hist(Gross_Profit, bins = 20)
plt.show()
