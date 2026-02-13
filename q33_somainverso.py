# Entrada
numero_normal = int(input('Digite um número inteiro de três dígitos: '))

# Processamento
digito_zero = numero_normal // 100
digito_um = (numero_normal % 100) // 10
digito_dois = numero_normal % 10

numero_inverso = (digito_dois * 100) + (digito_um * 10) + (digito_zero)
soma = numero_normal + numero_inverso

# Saída
print(f'A soma entre o número {numero_normal} e o seu inverso, {numero_inverso}, é igual a {soma}.')