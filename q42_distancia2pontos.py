# Entrada
x1 = int(input('Digite o ponto X do primeiro ponto: '))
y1 = int(input('Digite o ponto Y do primeiro ponto: '))
x2 = int(input('Digite o ponto X do segundo ponto: '))
y2 = int(input('Digite o ponto Y do segundo ponto: '))

# Processamento
d = ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2))

# Saída
print(f'A distância entre os pontos 1 ({x1}, {y1}) e 2 ({x2}, {y2}) é de {d}.')