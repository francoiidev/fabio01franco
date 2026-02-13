# Entrada
nota_um = float(input('Digite a nota de maior peso: '))
peso_um = int(input('Digite o seu peso: '))
nota_dois = float(input('Digite a segunda nota: '))
peso_dois = int(input('Digite o seu peso: '))
nota_tres = float(input('Digite a nota de menor peso: '))
peso_tres = int(input('Digite o seu peso: '))

# Processamento
media_ponderada = ((nota_um * peso_um) + (nota_dois * peso_dois) + (nota_tres * peso_tres)) / (peso_um + peso_dois + peso_tres)

# Saída
print(f'A média ponderada das notas {nota_um:.1f}, {nota_dois:.1f} e {nota_tres:.1f}, com os pesos {peso_um}, {peso_dois} e {peso_tres}, respectivamente, é de {media_ponderada:.1f}.')