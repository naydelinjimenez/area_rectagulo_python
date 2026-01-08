"""
Programa: Cálculo del área de un rectángulo
Descripción: Este programa solicita al usuario la base y la altura
de un rectángulo, calcula su área y determina si es grande o pequeña.
"""

# Solicitar datos al usuario (float)
base_rectangulo = float(input("Ingrese la base del rectángulo: "))
altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))

# Cálculo del área (float)
area_rectangulo = base_rectangulo * altura_rectangulo

# Condición booleana
area_grande = area_rectangulo > 50

# Mostrar resultados (string)
print("El área del rectángulo es:", area_rectangulo)

if area_grande:
    print("El área es grande.")
else:
    print("El área es pequeña.")
    