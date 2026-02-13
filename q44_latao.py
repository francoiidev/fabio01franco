# Entrada
latao = float(input('Digite a quantidade de latão desejada, em quilogramas: '))

# Processamento
cobre = latao * 0.7
zinco = latao * 0.3

# Saída
print(f'Para se obter {latao:.1f} kg de latão, devem ser utilizados {cobre:.1f} kg de cobre e {zinco:.1f} kg de zinco.')