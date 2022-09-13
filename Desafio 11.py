largura = int(input('Qual a largura? '))
altura = int(input('Qual a altura? '))
area = largura * altura
# 1 litro para cada 2m^2
print('Para pintar essa quantidade em m^2, precisa de {}L de tinta'.format(area/2))
