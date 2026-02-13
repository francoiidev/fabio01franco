# Entrada
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

# Processamento
r = (numero1 + numero2) ** 2
s = (numero2 + numero3) ** 2

d = (r + s) / 2

# Saída
print(f'O resultado da expressão D é igual a {d}.')