# =============================================================
# LECCIÓN 7: TABLAS CSV
# CSV = archivo de texto con columnas separadas por comas (o punto y coma).
# Excel puede abrirlo y guardarlo: Archivo -> Guardar como -> CSV UTF-8.
# =============================================================
import csv
from pathlib import Path

carpeta = Path(__file__).parent
entrada = carpeta / "empleados_ejemplo.csv"
salida = carpeta / "nomina_calculada.csv"

# --- 1. Crear un CSV de ejemplo ---
empleados = [
    {"nombre": "Ana Gómez", "area": "Ventas", "salario": "2800000", "horas_extra": "10"},
    {"nombre": "Luis Pérez", "area": "Contabilidad", "salario": "3500000", "horas_extra": "0"},
    {"nombre": "Marta Ruiz", "area": "Ventas", "salario": "3100000", "horas_extra": "6"},
]
with open(entrada, "w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=["nombre", "area", "salario", "horas_extra"])
    escritor.writeheader()
    escritor.writerows(empleados)
print("Creado:", entrada.name)

# --- 2. Leer el CSV ---
# DictReader convierte cada fila en un diccionario usando los encabezados.
# OJO: todo llega como TEXTO, hay que convertir los números.
# Si tu Excel en español guarda con punto y coma, usa: csv.DictReader(f, delimiter=";")
filas_resultado = []
with open(entrada, newline="", encoding="utf-8") as f:
    for fila in csv.DictReader(f):
        salario = float(fila["salario"])
        horas = int(fila["horas_extra"])
        valor_hora = salario / 240
        pago_extra = horas * valor_hora * 1.25
        filas_resultado.append({
            "nombre": fila["nombre"],
            "area": fila["area"],
            "total_a_pagar": round(salario + pago_extra),
        })
        print(f"{fila['nombre']:<12} extra: {pago_extra:>12,.0f}")

# --- 3. Escribir el resultado en otro CSV ---
with open(salida, "w", newline="", encoding="utf-8-sig") as f:   # utf-8-sig: Excel muestra bien las tildes
    escritor = csv.DictWriter(f, fieldnames=["nombre", "area", "total_a_pagar"])
    escritor.writeheader()
    escritor.writerows(filas_resultado)
print("Resultado guardado en:", salida.name, "-> ábrelo con Excel")

# =============================================================
# EJERCICIOS
# 1. Agrega una columna "bono" de 5% solo para el área Ventas.
# 2. Calcula el total de nómina por área (pista: diccionario como en la lección 4).
# 3. Exporta desde tu Excel real una tabla a CSV y léela con este mismo código.
# =============================================================
