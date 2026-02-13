# Entrada
valor_minutos = int(input('Digite um tempo em minutos: '))

# Processamento
dias = valor_minutos // 1440
horas = (valor_minutos % 1440) // 60
minutos = valor_minutos % 60

# Saída 
print(f'O tempo de {valor_minutos} minutos, em dias, horas e minutos, é de {dias} d, {horas} h e {minutos} min.')