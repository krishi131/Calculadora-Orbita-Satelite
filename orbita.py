# Calculadora de Orbita - Proyecto Krishi para NASA Space Apps
# Usa las Leyes de Kepler y datos de la Tierra

import math

# Constantes
G = 6.67430e-11
M_TIERRA = 5.972e24
R_TIERRA = 6371000

print("CALCULADORA DE ORBITA SATELITAL - NASA")
print("Ubicacion de referencia: Morelia, Michoacan")
print("-" * 50)

altura_km = float(input("Ingresa la altura del satelite en km (ej. 400 para la ISS): "))
altura_m = altura_km * 1000

r = R_TIERRA + altura_m
mu = G * M_TIERRA

velocidad = math.sqrt(mu / r)
periodo_seg = 2 * math.pi * math.sqrt(r**3 / mu)
periodo_min = periodo_seg / 60

print("\nRESULTADOS:")
print(f"Altura sobre Morelia: {altura_km} km")
print(f"Velocidad orbital necesaria: {velocidad/1000:.2f} km/s")
print(f"Tiempo en dar 1 vuelta a la Tierra: {periodo_min:.2f} minutos")
print(f"Vueltas por dia: {1440/periodo_min:.1f} orbitas")
