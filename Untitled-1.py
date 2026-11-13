
contador = 0
while contador <= 17:
    print(contador)
    contador += 1

for numero in range(1, 10):
    if numero == 5:
        continue
    if numero == 8:
        break
    print(numero)
    