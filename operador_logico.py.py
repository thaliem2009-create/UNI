from builtins import print
import os

# =============================================================================
# SECCIÓN 1: OPERADORES RELACIONALES Y LÓGICOS
# 1) Darle mayor descripción en consola a este problema
# 2) Generar un condicional concatenado que me permita saber la razón por 
# la que un usuario fue rechazado
# =============================================================================
print("=== SECCIÓN 1: Evaluando Expresiones Lógicas ===")

edad_estudiante = 18
tiene_carnet = False
promedio_notas = 10

# Evaluación relacional
es_mayor_de_edad = edad_estudiante >= 18

if(es_mayor_de_edad):{
    print(f"Si es mayor de edad y tiene({edad_estudiante} años)")
}
else:{
    print(f"No es mayor de edad y tiene({edad_estudiante} años)")
}

# Evaluación lógica combinada (AND / OR / NOT)
elegible_beca = (es_mayor_de_edad) and (promedio_notas >= 8.0) and tiene_carnet
print(f"¿Es elegible para la beca de liderazgo?: {elegible_beca}")

necesita_refuerzo = not (promedio_notas >= 7.0)
print(f"¿Necesita refuerzo académico?: {necesita_refuerzo}\n")