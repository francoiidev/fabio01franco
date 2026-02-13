# Entrada
numero_um = int(input('Digite o primeiro número: '))
numero_dois = int(input('Digite o segundo número: '))
numero_tres = int(input('Digite o terceiro número: '))

# NOTA: professor, ainda não sei como escrever uma linha de código que identificaria os 3 números caso fossem escritos seguidamente, 
# e nem se isso é possível. Portanto, optei por três inputs mesmo. 

# Processamento 
soma = numero_um + numero_dois
subtracao = numero_dois - numero_tres 

# Saída 
print(f'Usando os números {numero_um}, {numero_dois} e {numero_tres}, a soma de {numero_um} mais {numero_dois} é igual a {soma} e a subtração de {numero_dois} menos {numero_tres} é igual a {subtracao}.')