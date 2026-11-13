
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Fallo matematico")
else:
    print("No se ha producido ningun error. El calculo es correcto.")
finally:
    print("El programa finaliza sin detener. Entorno limpio.")
    