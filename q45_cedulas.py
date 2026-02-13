# Entrada 
print('O caixa possui notas de R$ 50.00, R$ 10.00, R$ 5.00, e R$ 1.00.')
valor = float(input('Digite uma quantia em reais: '))

# Processamento
# Hoje, caixas eletrônicos utilizam notas de 100, 50, 20, 10, 5 e 2 reais. Fiquei com medo de não ser a proposta da questão e optei por usar as do exemplo.
notas50 = valor // 50
notas10 = (valor % 50) // 10
notas5 = ((valor % 50) % 10) // 5
notas1 = (((valor % 50) % 10) % 5) // 1

# Saída
print(f'Para a quantia de R$ {valor:.2f}, sob o critério da distribuição ótima, seriam entregues {notas50:.0f} nota(s) de R$ 50, {notas10:.0f} nota(s) de R$ 10, {notas5:.0f} nota(s) de R$ 5 e {notas1:.0f} nota(s) de R$ 1.')