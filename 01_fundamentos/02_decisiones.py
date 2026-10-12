# =============================================================
# LECCIÓN 2: DECISIONES (if / elif / else)
# Permiten que el programa haga cosas distintas según los datos.
# =============================================================

monto = 2_500_000   # los guiones bajos solo ayudan a leer números grandes

# Comparadores:  ==  igual   !=  distinto   >  <  >=  <=
# IMPORTANTE: lo que está "dentro" del if va con 4 espacios de sangría.
if monto > 1_000_000:
    print("Requiere aprobación del gerente")
elif monto > 100_000:
    print("Requiere aprobación del jefe de área")
else:
    print("Aprobación automática")

# --- Combinar condiciones: and, or, not ---
dias_de_retraso = 45
cliente_vip = False

if dias_de_retraso > 30 and not cliente_vip:
    print("Enviar recordatorio de cobro")

# --- Comparar textos ---
estado = "Pendiente"
# .lower() pasa a minúsculas: así "PENDIENTE", "pendiente" y "Pendiente" son iguales
if estado.lower() == "pendiente":
    print("Este documento sigue pendiente")

# --- ¿Está un texto dentro de otro? ---
asunto_correo = "Factura No. 4512 - Proveedor XYZ"
if "factura" in asunto_correo.lower():
    print("Este correo es una factura -> mover a carpeta Facturas")

# =============================================================
# EJERCICIOS
# 1. Dada una nota (0 a 5), muestra "Excelente" (>=4.5), "Aprobado" (>=3) o "Reprobado".
# 2. Dado el nombre de un archivo, por ejemplo "informe.pdf", muestra
#    "Es PDF" si termina en .pdf. Pista: nombre.endswith(".pdf")
# 3. Calcula un descuento: 10% si compra más de 500.000, 5% si más de 200.000, si no 0%.
# =============================================================
