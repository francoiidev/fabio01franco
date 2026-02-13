# Entrada
valor = float(input('Digite o valor, em reais, do produto a ser parcelado: '))

# Processamento
prestacoes = valor // 3 
resto = valor % 3
entrada = prestacoes + resto

# Saída
print(f'Para o valor de R$ {valor:.2f}, a entrada custará R$ {entrada:.2f} e as duas prestações custarão R$ {prestacoes:.2f}.')