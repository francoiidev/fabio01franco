# Entrada
numero_inicial = int(input('Digite um número de três algarismos: '))

# Processamento
algarismo_um = numero_inicial // 100
algarismo_dois = numero_inicial // 10 - algarismo_um * 10
algarismo_tres = numero_inicial - algarismo_um * 100 - algarismo_dois * 10

numero_final = algarismo_tres * 100 + algarismo_dois * 10 + algarismo_um

# Saída 
print(f'O número {numero_inicial} com seus algarismos na ordem inversa corresponde a {numero_final}.')