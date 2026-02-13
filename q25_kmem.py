# Entrada
valor_metros = int(input('Digite um valor inteiro em metros: '))

# Processamento
valor_km = valor_metros // 1000
metros = valor_metros % 1000

# Saída 
print(f'O valor inteiro {valor_metros} m, em quilômetros e metros, é de {valor_km} km e {metros} m.')