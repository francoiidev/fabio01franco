# Entrada
numero_inicial = int(input('Digite um número inteiro de 4 dígitos: '))

# Processamento
digito_zero = numero_inicial // 1000
digito_um = (numero_inicial % 1000) // 100
digito_dois = (numero_inicial % 100) // 10
digito_tres = numero_inicial % 10

soma = digito_zero + digito_um + digito_dois + digito_tres

# Saída
print(f'A soma dos elementos do número {numero_inicial}, é de {digito_zero} + {digito_um} + {digito_dois} + {digito_tres} = {soma} .')