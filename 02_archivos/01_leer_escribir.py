# =============================================================
# LECCIÓN 6: LEER Y ESCRIBIR ARCHIVOS DE TEXTO
# =============================================================
from pathlib import Path   # Path es la forma moderna de manejar rutas de archivos

# Carpeta donde está este script (así funciona desde cualquier lugar)
carpeta = Path(__file__).parent
archivo = carpeta / "notas_ejemplo.txt"    # el operador / une rutas

# --- Escribir ---
# "w" = write (sobrescribe).  "a" = append (agrega al final).
# encoding="utf-8" evita problemas con tildes y ñ.
with open(archivo, "w", encoding="utf-8") as f:
    f.write("Reunión con contabilidad\n")     # \n = salto de línea
    f.write("Enviar reporte de ventas\n")
    f.write("Llamar a proveedor\n")
print(f"Archivo creado: {archivo.name}")

# --- Agregar líneas ---
with open(archivo, "a", encoding="utf-8") as f:
    f.write("Revisar facturas pendientes\n")

# --- Leer todo ---
with open(archivo, "r", encoding="utf-8") as f:
    contenido = f.read()
print("--- Contenido completo ---")
print(contenido)

# --- Leer línea por línea (lo más común) ---
with open(archivo, "r", encoding="utf-8") as f:
    for numero, linea in enumerate(f, start=1):
        linea = linea.strip()            # quita espacios y el salto de línea
        print(f"Tarea {numero}: {linea}")

# --- Atajos de pathlib ---
print(archivo.exists())                  # ¿existe?
print(archivo.suffix)                    # extensión: .txt
print(archivo.stem)                      # nombre sin extensión
texto = archivo.read_text(encoding="utf-8")

# --- Listar archivos de una carpeta ---
print("--- Archivos .py en esta carpeta ---")
for ruta in carpeta.glob("*.py"):
    print(ruta.name)

# Limpieza: borrar el archivo de ejemplo
archivo.unlink()

# =============================================================
# EJERCICIOS
# 1. Crea un archivo "pendientes.txt" con 5 tareas y luego muéstralas numeradas.
# 2. Cuenta cuántas líneas de un archivo contienen la palabra "urgente".
# 3. Lista todos los archivos de tu carpeta Descargas y su tamaño (ruta.stat().st_size).
#    Pista: Path.home() / "Downloads"
# =============================================================
