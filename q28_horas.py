# Entrada
valor_horas = int(input('Digite um tempo em horas: '))

# Processamento
semanas = valor_horas // 168
dias = (valor_horas % 168) // 24
horas = valor_horas % 24

# Saída 
print(f'O tempo de {valor_horas} h, em semanas, dias e horas, é de {semanas} semana(s), {dias} d e {horas} h.')