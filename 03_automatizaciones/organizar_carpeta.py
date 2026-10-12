"""
ORGANIZAR UNA CARPETA POR TIPO DE ARCHIVO

Mueve cada archivo a una subcarpeta según su extensión:
    informe.pdf   -> PDFs/informe.pdf
    foto.jpg      -> Imagenes/foto.jpg
    ventas.xlsx   -> Excel/ventas.xlsx

Uso:
    python organizar_carpeta.py "C:/Users/TuUsuario/Downloads"           (modo prueba: solo muestra)
    python organizar_carpeta.py "C:/Users/TuUsuario/Downloads" --ejecutar (mueve de verdad)
"""
import shutil
import sys
from pathlib import Path

# Personaliza aquí: nombre de carpeta -> extensiones que van en ella
CATEGORIAS = {
    "PDFs": [".pdf"],
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Excel": [".xlsx", ".xls", ".csv"],
    "Word": [".docx", ".doc"],
    "Presentaciones": [".pptx", ".ppt"],
    "Comprimidos": [".zip", ".rar", ".7z"],
}


def carpeta_destino(archivo):
    """Devuelve el nombre de la categoría para un archivo, u 'Otros'."""
    extension = archivo.suffix.lower()
    for categoria, extensiones in CATEGORIAS.items():
        if extension in extensiones:
            return categoria
    return "Otros"


def ruta_libre(destino):
    """Si ya existe un archivo con ese nombre, agrega (1), (2)... para no sobrescribir."""
    contador = 1
    nueva = destino
    while nueva.exists():
        nueva = destino.with_name(f"{destino.stem} ({contador}){destino.suffix}")
        contador += 1
    return nueva


def organizar(carpeta, ejecutar=False):
    movidos = 0
    for archivo in carpeta.iterdir():
        if not archivo.is_file():
            continue                      # saltar subcarpetas
        categoria = carpeta_destino(archivo)
        destino = ruta_libre(carpeta / categoria / archivo.name)
        print(f"{archivo.name}  ->  {categoria}/{destino.name}")
        if ejecutar:
            destino.parent.mkdir(exist_ok=True)
            shutil.move(str(archivo), str(destino))
        movidos += 1

    if ejecutar:
        print(f"\nListo: {movidos} archivos organizados.")
    else:
        print(f"\nMODO PRUEBA: se moverían {movidos} archivos. Agrega --ejecutar para hacerlo.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    carpeta = Path(sys.argv[1]).expanduser()
    if not carpeta.is_dir():
        sys.exit(f"No encuentro la carpeta: {carpeta}")
    organizar(carpeta, ejecutar="--ejecutar" in sys.argv)
