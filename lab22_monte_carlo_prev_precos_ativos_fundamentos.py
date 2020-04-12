# Vamos entender conceitualmente como a Simulacao de Mote Carlo pode ser usada para modelar a evolucao dos precos dos ativos. O preco de uma acao e algo que observamos olhando para tras, mas nos nao abemos nada sobre como eles irao se comportar no futuro, assim, o que podemos fazer sao inferencias sobre os precos passados, vamos olhar para a equacao abaixo que descreve o preco de um ativo
# Preco de Hoje = Preco de ontem * e^r >=> onde r e o retorno logaritmico entre o preco da acao de ontem e de hoje |=> sabemos que e^(ln(x)) = x como <=> r = ln(Preco de Hoje / Preco de Ontem) => podemos entao reescrever nossa equacao da seguinte forma >=> Preco de Hoje = Preco de ontem x e^(ln(Preco de Hoje / Preco de Ontem)). Muito bem, o preco de ontem ok nos sabemos, mas e o valor de r? r e uma variavel aleatoria, entao como podemos trabalhar com ela?
# Podemos usar o movimento Browniano que e um conceito adequado para modelar esse tipo de aleatoriedade para os calculos precisaremos de dois conceitos, sao eles |=>> 1 - Drift e 2 - Volatilidade da acao
# 1 Drift >=> e a direcao que as taxs de retorno tivera no passado >>= ln(Preco de Hoje / Preco de Ontem) e a melhor aproximacao do futuro que temos => A direcao que as taxas de retorno tiveram no passado, atraves do calculo da media, desvio-padrao e variancia dos retornos diarios ao longo do periodo historico analisado nos da o Drift =>> Drift = (µ - 0.5 * σ^2) <=> sabendo que o µ e o retorno medio diario e σ e a variancia (0.5 x pela variancia nos fornece a aleatoriedade futura). O Drift em palavras e o retorno diario esperado da acao
# 2 Volatilidade >=> o segundo elemento de um movimento Browniano e a variavel aleatoria para a qual podemos escrever >=> Random variable = σ * Z(Rand(0;1)) |=> σ e a volatilidade aleatoria multiplica por Z(Rand(0;1)) que e um numero aleatorio entre 0 e 1 >>= um numero aleatorio entre 0 e 1 e um percentual, se assumirmos que o retorno futuro esperado tem uma distribuicao normal o retorno Z vai nos dar o numero de desvios padrao em relacao a media, sendo a Probabilidade de 100% correspondente a +/- 4σ, 99.7% corresponde a +/1 3σ, 96% corresponde a +/- 2σ e a probabilidade de 68% corresponde a +/- 1σ 
# Assim podemos escrever que o preco de uma acao hoje pode ser expresso por >>= Price Today = Price Yesterday * e^[(μ - 0.5σ^2) + σZ[Rand(0;1)]] >=> se repetirmos esse calculo, por exemplo, 1.000 vezes seremos capazes de simular a evolucao do preco da acao amanha e avaliar a probabilidade de que ira seguir um certo padrao <=> alem disso essa e uma otima oportunidade para avaliarmos os pros e contras do investimento ja que obtivemos um limite inferior e superior ao usarmos a Simulacao de Monte Carlo