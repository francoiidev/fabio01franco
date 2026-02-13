# Entrada
custofab = float(input('Digite o custo de fábrica de um carro, em reais: '))

# Processamento 
distrib = 0.28 * custofab
imposto = 0.45 * custofab
custocons = custofab + distrib + imposto

# Saída
print(f'Um carro com um custo de fábrica de R$ {custofab:.2f} tem seu valor somado com a percentagem do distribuidor de R$ {distrib:.2f} e impostos de R$ {imposto:.2f}, totalizando um custo final ao consumidor de R$ {custocons:.2f}.')