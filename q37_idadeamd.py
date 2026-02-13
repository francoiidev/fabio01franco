# Entrada
idade_dias = int(input('Digite uma idade em dias: '))

# Processamento 
anos = idade_dias // 365
meses = (idade_dias % 365) // 30
dias = (idade_dias % 365) % 30

# Saída
print(f'A idade {idade_dias} dias, em anos, meses e dias, é de {anos} ano(s), {meses} mês(s) e {dias} dia(s).')