# Entrada
valor_inicial = int(input('Digite um valor em minutos: '))

# Processamento
valor_horas = valor_inicial // 60 
valor_minutos = valor_inicial % 60

# Saída
print(f'O valor de {valor_inicial} minutos, em horas e minutos, é de {valor_horas} horas e {valor_minutos} minutos.')