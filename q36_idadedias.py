# Entrada
anos = int(input('Digite os anos de idade: '))
meses = int(input('E quantos meses? '))
dias = int(input('E dias? '))

# Processamento 
idade_dias = (anos * 365) + (meses * 30) + dias

# Saída
print(f'A idade {anos} ano(s), {meses} mês(s) e {dias} dia(s), em dias, é igual a {idade_dias} dias.')