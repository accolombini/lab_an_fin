import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt 

PG = wb.DataReader('PG', data_source='yahoo', start='1995-01-01')
print(PG.head())
print(PG.tail())

PG['log_return'] = np.log(PG['Adj Close'] / PG['Adj Close'].shift(1))
print('Taxa logaritmica de retorno', PG['log_return'])

PG['log_return'].plot(figsize=(8,5)) # Exibe gráfico de variação logaritmica das ações no período
plt.show()

log_return_d = PG['log_return'].mean()   # Cálculo da média logaritmica diária
print('Média diária logaritmica calculada     ', log_return_d)

log_return_a = PG['log_return'].mean() * 250 # Cálculo da média logaritmica anual daí os 250 dias
print('Média anual logaritmica calculada      ', log_return_a)

print ('Média anual logaritmica em porcentagem ', str(round(log_return_a, 5) * 100) + ' %')     # Cálculo da média anual 
                                                                                                # em porcentagem e 5 casas
