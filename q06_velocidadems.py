# Entrada
velocidade_km = float(input('Digite, em quilômetros por hora, uma velocidade qualquer: '))

# Processamento
velocidade_ms = velocidade_km / 3.6

# Saída
print(f'A velocidade {velocidade_km:.1f} km/h, em metros por segundo, é de {velocidade_ms:.1f} m/s.')