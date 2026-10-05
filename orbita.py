# Calculadora de Órbita - Proyecto Krishi para NASA Space Apps
# Usa las Leyes de Kepler y datos de la Tierra

import math

# Constantes
G = 6.67430e-11  # Constante gravitacional
M_TIERRA = 5.972e24  # Masa de la Tierra en kg
R_TIERRA = 6371000  # Radio de la Tierra en metros

print("🛰️ CALCULADORA DE ÓRBITA SATELITAL - NASA")
print("Ubicación de referencia: Morelia, Michoacán")
print("-" * 50)

# Pedir altura al usuario
altura_km = float(input("Ingresa la altura del satélite en km (ej. 400 para la ISS): "))
altura_m = altura_km * 1000

# Cálculos de Mecánica Orbital
r = R_TIERRA + altura_m  # Radio orbital total
mu = G * M_TIERRA  # Parámetro gravitacional estándar

# 1. Velocidad orbital
velocidad = math.sqrt(mu / r)

# 2. Periodo orbital
periodo_seg = 2 * math.pi * math.sqrt(r**3 / mu)
periodo_min = periodo_seg / 60

# Resultados
print("\n🚀 RESULTADOS:")
print(f"Altura sobre Morelia: {altura_km} km")
print(f"Velocidad orbital necesaria: {velocidad/1000:.2f} km/s")
print(f"Tiempo en dar 1 vuelta a la Tierra: {periodo_min:.2f} minutos")
print(f"Vueltas por día: {1440/periodo_min:.1f}")

if 350 <= altura_km <= 450:
    print("\n¡Esa es la altura de la ISS! La ves pasar sobre Morelia cada 90 min aprox.")
