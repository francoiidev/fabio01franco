# Entrada
cotacao_dolar = float(input('Digite a atual cotação do dólar, em reais: '))
valor_dolar = float(input('Digite o valor a ser convertido, em dólares: '))

# Processamento
valor_reais = valor_dolar * cotacao_dolar

# Saída 
print(f'O valor de U$ {valor_dolar:.2f}, em reais, é de R$ {valor_reais:.2f}')