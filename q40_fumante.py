# Entrada
numero_anos = int(input('Digite o tempo, em anos, que fuma: '))
numero_cigarros = int(input('Digite o número de cigarros fumados por dia: '))
preco_carteira = float(input('Digite o preço da carteira de cigarros: ')) 

# Processamento
numero_dias = numero_anos * 365
total_cigarros = numero_cigarros * numero_dias
numero_carteiras = round((total_cigarros / 20), 0)
dinheiro = numero_carteiras * preco_carteira

# Saída
print(f'O preço gasto por um fumante que fuma {numero_cigarros} cigarro(s) por dia há {numero_anos} ano(s), com a carteira custando R$ {preco_carteira:.2f}, é de, aproximadamente, R$ {dinheiro:.2f}.')