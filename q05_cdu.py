# Entrada
numero_inicial = int(input('Digite um número de 3 dígitos: '))

# Processamento
valor_centenas = numero_inicial // 100
valor_dezenas = numero_inicial // 10 - valor_centenas * 10
valor_unidades = numero_inicial - valor_centenas * 100 - valor_dezenas * 10

valor_final = valor_centenas + valor_dezenas + valor_unidades

# Saída 
print(f'A soma dos algarismos das centenas, das dezenas e das unidades do número {numero_inicial} é {valor_final} ({valor_centenas} centenas, {valor_dezenas} dezenas e {valor_unidades} unidades).')