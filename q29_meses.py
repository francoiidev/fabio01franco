# Entrada
valor_meses = int(input('Digite um tempo em meses: '))

# Processamento
anos = valor_meses // 12
meses = valor_meses % 12

# Saída 
print(f'O tempo de {valor_meses}, em anos e meses, é de {anos} ano(s) e {meses} mês(s).')