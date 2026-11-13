
while True:
    try:
        edad = int(input("Introduce tu edad: "))
        break
    except ValueError:
        print("Error: Debes introducir un numero entero.")
print(f"Validacion exitosa, Tienes {edad} años.")
