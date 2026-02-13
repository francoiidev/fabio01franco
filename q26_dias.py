# Entrada
valor_dias = int(input('Digite um número de dias: '))

# Processamento
semanas = valor_dias // 7
dias = valor_dias % 7

# Saída 
print(f'O tempo de {valor_dias} dia(s), em semanas e dias, é de {semanas} semana(s) e {dias} d.')