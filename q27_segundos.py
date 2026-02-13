# Entrada
valor_segundos = int(input('Digite um tempo em segundos: '))

# Processamento
horas = valor_segundos // 3600
minutos = (valor_segundos % 3600) // 60
segundos = (valor_segundos % 3600) % 60

# Saída 
print(f'O tempo de {valor_segundos} s, em horas, minutos e segundos, é de {horas} h, {minutos} min e {segundos} s.')