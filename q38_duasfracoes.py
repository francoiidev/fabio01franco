# Entrada
numerador1 = int(input('Digite o numerador da primeira fração: '))
denominador1 = int(input('Digite o denominador da primeira fração: '))
numerador2 = int(input('Digite o numerador da segunda fração: '))
denominador2 = int(input('Digite o denominador da segunda fração: '))

# Processamento
# fracao1 = (numerador1/denominador1)
# fracao2 = (numerador2/denominador2)
# soma = fracao1 + fracao2

# Tentativa 2 (método da borboleta):
numerador3 = (numerador1 * denominador2) + (denominador1 * numerador2)
denominador3 = denominador1 * denominador2

# Saída
# print(f'A soma das frações {numerador1}/{denominador1} e {numerador2}/{denominador2} é igual a {soma}.')
print(f'A soma das frações {numerador1}/{denominador1} e {numerador2}/{denominador2} é igual a {numerador3}/{denominador3}.')