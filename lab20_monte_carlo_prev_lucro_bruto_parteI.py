# Usando Monte carlo na previsao do luco bruto >=> acompanhe em Python
# Queremos nesta pratica demonstra como a Simulacao de Monte Carlo pode ser util para projetar receitas e despesas futuras de uma empresa
# Nosso objetivo e prever o Lucro Bruto Futuro de uma empresa >=> precisaremos para isso da Receita esperada e do Custo esperado da Mercadoria Vendida CMV >>= no Brasil e COGS >>= nos EUA. Iremos iteirar 1.000 vezes simulando a receita futura da empresa
# Atencao >>= para essa pratica vamos partir de algum conhecimento historico, por exemplo, vamos considerar que as Receitas esperadas para esse ano serao de 170 milhoes com um desvio padrao de 20 milhoes 


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
