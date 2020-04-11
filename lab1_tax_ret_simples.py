import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt 

PG = wb.DataReader('PG', data_source='yahoo', start='1995-01-01')
print(PG.head())
print(PG.tail())

PG['simple_return'] = (PG['Adj Close']/PG['Adj Close'].shift(1)) - 1
print('HEAD', PG['simple_return'].head(20))
print('TAIL', PG['simple_return'].tail(20))

PG['simple_return'].plot(figsize=(8,5)) # Exibe gráfico de variação média das ações no período
plt.show()
avg_return_d = PG['simple_return'].mean()   # Cálculo da média diária
print('Média diária calculada     ', avg_return_d)

avg_return_a = PG['simple_return'].mean() * 250 # Cálculo da média anual daí os 250 dias
print('Média anual calculada      ', avg_return_a)

print ('Média anual em porcentagem ', str(round(avg_return_a, 5) * 100) + ' %')    # Cálculo da média anual em porcentagem e 5 casas
