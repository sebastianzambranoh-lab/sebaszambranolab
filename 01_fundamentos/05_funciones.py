# =============================================================
# LECCIÓN 5: FUNCIONES
# Una función es una "receta" con nombre: la escribes una vez y la usas muchas.
# =============================================================

# def nombre(parametros):   <- define la función
#     ...pasos...
#     return resultado       <- devuelve un valor

def calcular_iva(valor, tasa=0.19):
    """Devuelve el IVA de un valor. La tasa por defecto es 19%."""
    return valor * tasa


def formatear_pesos(valor):
    """Convierte 1234567.8 en '$1.234.568'."""
    return "$" + f"{valor:,.0f}".replace(",", ".")


def clasificar_cliente(total_compras):
    if total_compras >= 10_000_000:
        return "Oro"
    elif total_compras >= 3_000_000:
        return "Plata"
    return "Bronce"


# Usar las funciones
base = 850000
iva = calcular_iva(base)
print("IVA:", formatear_pesos(iva))
print("Total:", formatear_pesos(base + iva))
print("IVA al 5%:", formatear_pesos(calcular_iva(base, tasa=0.05)))

for compras in [500_000, 4_000_000, 15_000_000]:
    print(formatear_pesos(compras), "->", clasificar_cliente(compras))

# --- Manejar errores con try / except ---
# Muy útil al automatizar: si un dato viene mal, no se cae todo el programa.
def convertir_a_numero(texto):
    try:
        return float(texto.replace(",", "."))
    except ValueError:
        print(f"  Aviso: '{texto}' no es un número, uso 0")
        return 0

for dato in ["1500", "23,5", "N/A"]:
    print(dato, "->", convertir_a_numero(dato))

# --- Importar funciones que ya existen ---
# Python trae muchísimas herramientas listas ("la biblioteca estándar").
from datetime import date
hoy = date.today()
print("Hoy es", hoy.strftime("%d/%m/%Y"))

# =============================================================
# EJERCICIOS
# 1. Escribe una función dias_entre(fecha1, fecha2) usando date y resta (fecha2 - fecha1).days
# 2. Escribe una función que reciba un nombre de archivo y devuelva su extensión.
#    Ej: "reporte.final.xlsx" -> "xlsx". Pista: .split(".")
# 3. Escribe una función que reciba una lista de valores y devuelva (total, promedio).
# =============================================================
