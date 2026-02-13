# Entrada
numero_um = int(input('Digite o dividendo da operação: '))
numero_dois = int(input('Digite o divisor da operação: '))

# Processamento
quociente = numero_um // numero_dois
resto = numero_um % numero_dois

# Saída
print(f'Na operação de divisão {numero_um} dividido por {numero_dois}, o quociente da mesma é {quociente} e o resto é {resto}.')