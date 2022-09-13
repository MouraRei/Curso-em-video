import math
#from math import sqrt(ou qualquer outra função)
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
#math.ceil é para arredondar para cima
#math.floor é para arredondar para baixo
print('A raiz de {} é {}'.format(num,math.ceil(raiz)))
