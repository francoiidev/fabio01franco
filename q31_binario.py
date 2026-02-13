# Entrada
binario = int(input('Digite um número binário de 4 dígitos: '))

# Processamento
digito_zero = binario // 1000
digito_um = (binario % 1000) // 100
digito_dois = (binario % 100) // 10
digito_tres = binario % 10

res00 = digito_zero * (2 ** 3)
res01 = digito_um * (2 ** 2)
res02 = digito_dois * (2 ** 1)
res03 = digito_tres * (2 ** 0)
valor_final = res00 + res01 + res02 + res03

# Saída
print(f'O número binário {binario:04d}, em base decimal, equivale a {valor_final}.')