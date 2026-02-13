# Entrada
temp_fahrenheit = float(input('Digite uma temperatura em °F: '))

# Processamento 
temp_celsius = ((temp_fahrenheit * 5) - 160) / 9

# Saída
print(f'A temperatura {temp_fahrenheit:.1f} °F, em celsius, é igual a {temp_celsius:.1f} °C.')