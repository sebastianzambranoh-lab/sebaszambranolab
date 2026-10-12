# =============================================================
# LECCIÓN 1: VARIABLES
# Una variable es una "caja con nombre" donde guardas un dato.
# Todo lo que empieza con # es un comentario: Python lo ignora.
# =============================================================

# --- Textos (se llaman "strings" y van entre comillas) ---
nombre = "Karen"
cargo = "Analista"

# print() muestra algo en pantalla
print(nombre)
print("Cargo:", cargo)

# --- Números ---
facturas_pendientes = 12      # número entero (int)
valor_factura = 150000.50     # número decimal (float) -> se usa punto, no coma

total = facturas_pendientes * valor_factura
print("Total pendiente:", total)

# --- Operaciones básicas ---
# +  suma        -  resta       *  multiplicación
# /  división    // división entera    %  residuo
print(10 / 3)    # 3.333...
print(10 // 3)   # 3
print(10 % 3)    # 1

# --- f-strings: la forma más cómoda de armar textos con datos ---
# Pon una f antes de las comillas y las variables entre { }
mensaje = f"Hola {nombre}, tienes {facturas_pendientes} facturas por {total:,.0f} pesos."
print(mensaje)

# --- Booleanos: Verdadero o Falso ---
esta_aprobado = True
print("¿Aprobado?", esta_aprobado)

# --- Pedir datos al usuario ---
# input() siempre devuelve TEXTO. Si necesitas un número, conviértelo con int() o float().
# (Quita el # de las dos líneas siguientes para probarlo)
# horas = int(input("¿Cuántas horas trabajaste hoy? "))
# print(f"Esta semana serían {horas * 5} horas")

# =============================================================
# EJERCICIOS
# 1. Crea variables con tu salario por hora y horas trabajadas al mes,
#    y muestra el salario mensual con un f-string.
# 2. Calcula el IVA (19%) de un valor y muestra valor, IVA y total.
# 3. ¿Qué pasa si haces "5" + 5 ? Lee el error. ¿Cómo lo arreglas?
# =============================================================
