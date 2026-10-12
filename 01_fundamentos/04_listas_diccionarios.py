# =============================================================
# LECCIÓN 4: LISTAS Y DICCIONARIOS
# Las dos estructuras que más vas a usar para manejar datos.
# =============================================================

# ---------- LISTAS: colección ordenada ----------
tareas = ["Revisar correo", "Conciliar cuentas", "Enviar reporte"]

print(tareas[0])      # primer elemento (se cuenta desde 0)
print(tareas[-1])     # último elemento
print(len(tareas))    # cuántos hay

tareas.append("Actualizar inventario")   # agregar al final
tareas.remove("Revisar correo")          # quitar un elemento
print(tareas)

numeros = [5, 2, 9, 1]
print(sorted(numeros))                  # ordenada: [1, 2, 5, 9]
print(sum(numeros), max(numeros), min(numeros))

# ---------- DICCIONARIOS: datos con etiqueta (clave -> valor) ----------
# Piensa en una fila de Excel donde cada columna tiene nombre.
empleado = {
    "nombre": "Luis Pérez",
    "area": "Contabilidad",
    "salario": 3_200_000,
}

print(empleado["nombre"])
empleado["salario"] = 3_500_000          # modificar
empleado["correo"] = "luis@empresa.com"  # agregar
print(empleado)

# Recorrer un diccionario
for clave, valor in empleado.items():
    print(f"{clave}: {valor}")

# .get() evita errores si la clave no existe
print(empleado.get("telefono", "Sin teléfono"))

# ---------- LISTA DE DICCIONARIOS = UNA TABLA ----------
# Esto es exactamente cómo se ve un Excel/CSV cuando lo lees con Python.
facturas = [
    {"numero": 101, "cliente": "Ana", "valor": 500000, "pagada": True},
    {"numero": 102, "cliente": "Luis", "valor": 320000, "pagada": False},
    {"numero": 103, "cliente": "Ana", "valor": 150000, "pagada": False},
]

pendiente = 0
for f in facturas:
    if not f["pagada"]:
        pendiente += f["valor"]
        print(f"Factura {f['numero']} de {f['cliente']} sin pagar")
print("Total pendiente:", pendiente)

# Agrupar: total facturado por cliente
por_cliente = {}
for f in facturas:
    cliente = f["cliente"]
    por_cliente[cliente] = por_cliente.get(cliente, 0) + f["valor"]
print(por_cliente)   # {'Ana': 650000, 'Luis': 320000}

# =============================================================
# EJERCICIOS
# 1. Agrega 2 facturas más a la lista y vuelve a ejecutar.
# 2. Cuenta cuántas facturas están pagadas y cuántas no.
# 3. Crea un diccionario {"enero": 0, "febrero": 0} y súmale ventas de una lista
#    como [("enero", 100), ("febrero", 50), ("enero", 30)].
# =============================================================
