"""
RENOMBRAR ARCHIVOS EN LOTE

Renombra todos los archivos de una carpeta (opcionalmente solo una extensión) con
el patrón:  <prefijo>_<fecha>_<número>.<extensión>
    IMG_4512.jpg  ->  visita_cliente_2026-10-12_001.jpg

Uso:
    python renombrar_archivos.py CARPETA PREFIJO [.extension] [--ejecutar]

Ejemplos:
    python renombrar_archivos.py ./fotos visita_cliente .jpg
    python renombrar_archivos.py ./fotos visita_cliente .jpg --ejecutar
"""
import sys
from datetime import datetime
from pathlib import Path


def fecha_modificacion(archivo):
    """Fecha en que se modificó el archivo por última vez, como 2026-10-12."""
    return datetime.fromtimestamp(archivo.stat().st_mtime).strftime("%Y-%m-%d")


def renombrar(carpeta, prefijo, extension=None, ejecutar=False):
    archivos = sorted(p for p in carpeta.iterdir() if p.is_file())
    if extension:
        archivos = [p for p in archivos if p.suffix.lower() == extension.lower()]

    for numero, archivo in enumerate(archivos, start=1):
        nuevo_nombre = f"{prefijo}_{fecha_modificacion(archivo)}_{numero:03d}{archivo.suffix.lower()}"
        nuevo = archivo.with_name(nuevo_nombre)
        if nuevo.exists() and nuevo != archivo:
            print(f"OMITIDO (ya existe {nuevo_nombre}): {archivo.name}")
            continue
        print(f"{archivo.name}  ->  {nuevo_nombre}")
        if ejecutar:
            archivo.rename(nuevo)

    if not ejecutar:
        print(f"\nMODO PRUEBA ({len(archivos)} archivos). Agrega --ejecutar para renombrar.")


if __name__ == "__main__":
    argumentos = [a for a in sys.argv[1:] if a != "--ejecutar"]
    if len(argumentos) < 2:
        print(__doc__)
        sys.exit(1)
    carpeta = Path(argumentos[0]).expanduser()
    if not carpeta.is_dir():
        sys.exit(f"No encuentro la carpeta: {carpeta}")
    extension = argumentos[2] if len(argumentos) > 2 else None
    renombrar(carpeta, argumentos[1], extension, ejecutar="--ejecutar" in sys.argv)
