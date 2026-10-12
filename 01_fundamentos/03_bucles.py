# =============================================================
# LECCIÓN 3: BUCLES (repetir)
# Aquí empieza la automatización: hacer lo mismo con muchos elementos.
# =============================================================

# --- for: recorre cada elemento de una lista ---
clientes = ["Ana", "Luis", "Marta", "Pedro"]

for cliente in clientes:
    print(f"Estimado(a) {cliente}, le recordamos su pago pendiente.")

# --- range(): repetir un número de veces ---
# range(1, 6) produce 1, 2, 3, 4, 5  (el último NO se incluye)
for numero in range(1, 6):
    print(f"Generando informe_{numero}.txt")

# --- Acumular resultados ---
ventas = [120000, 85000, 230000, 40000]
total = 0
for venta in ventas:
    total = total + venta        # también se escribe: total += venta
print("Total ventas:", total)

# --- Bucle + decisión: filtrar ---
for venta in ventas:
    if venta >= 100000:
        print(f"Venta grande: {venta}")

# --- enumerate(): cuando también necesitas la posición ---
for posicion, cliente in enumerate(clientes, start=1):
    print(f"{posicion}. {cliente}")

# --- while: repetir MIENTRAS se cumpla algo ---
intentos = 0
while intentos < 3:
    intentos += 1
    print(f"Intento de conexión #{intentos}")

# --- break y continue ---
for cliente in clientes:
    if cliente == "Marta":
        print("Encontré a Marta, dejo de buscar")
        break          # sale del bucle

# =============================================================
# EJERCICIOS
# 1. Con la lista ventas, calcula el promedio (total / cantidad). Pista: len(ventas)
# 2. Muestra la tabla de multiplicar del 7 (7x1 hasta 7x10).
# 3. Dada una lista de nombres de archivos, muestra solo los que terminan en ".xlsx".
# =============================================================
