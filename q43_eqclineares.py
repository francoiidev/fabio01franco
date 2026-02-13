# Entrada
print('Na equação linear do tipo:')
print('ax + by = c')
print('dx + ey = f')
a = int(input('Insira o coeficiente a: '))
b = int(input('Insira o coeficiente b: '))
c = int(input('Insira o coeficiente c: '))
d = int(input('Insira o coeficiente d: '))
e = int(input('Insira o coeficiente e: '))
f = int(input('Insira o coeficiente f: '))

# Processamento
x = ((c * e) - (b * f)) / ((a * e) - (b * d))
y = ((a * f) - (c * d)) / ((a * e) - (b * d))

# Saída
print(f'Com os coeficientes {a}, {b}, {c}, {d}, {e} e {f}, x é igual a {x:.1f} e y é igual a {y:.1f}.')