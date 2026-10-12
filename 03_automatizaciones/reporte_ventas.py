"""
REPORTE DE VENTAS A PARTIR DE UN CSV

Lee un archivo de ventas (exportado de Excel o de un sistema) y genera:
  - Total vendido por vendedor
  - Total vendido por mes
  - Un CSV con el resumen, listo para abrir en Excel

Uso:
    python reporte_ventas.py                       (usa datos/ventas_ejemplo.csv)
    python reporte_ventas.py mi_archivo.csv

El CSV debe tener las columnas: fecha (AAAA-MM-DD), vendedor, producto, cantidad, precio_unitario
"""
import csv
import sys
from pathlib import Path

CARPETA = Path(__file__).parent


def leer_ventas(ruta):
    with open(ruta, newline="", encoding="utf-8-sig") as f:
        # Detecta automáticamente si el separador es coma o punto y coma
        muestra = f.read(2048)
        f.seek(0)
        separador = ";" if muestra.count(";") > muestra.count(",") else ","
        return list(csv.DictReader(f, delimiter=separador))


def sumar_por(ventas, columna_grupo):
    """Agrupa las ventas por una columna y suma cantidad * precio."""
    totales = {}
    for v in ventas:
        grupo = v[columna_grupo]
        valor = int(v["cantidad"]) * float(v["precio_unitario"])
        totales[grupo] = totales.get(grupo, 0) + valor
    return totales


def imprimir_tabla(titulo, totales):
    print(f"\n=== {titulo} ===")
    for clave, valor in sorted(totales.items(), key=lambda x: x[1], reverse=True):
        print(f"  {clave:<15} ${valor:>14,.0f}")
    print(f"  {'TOTAL':<15} ${sum(totales.values()):>14,.0f}")


def main():
    ruta = Path(sys.argv[1]) if len(sys.argv) > 1 else CARPETA / "datos" / "ventas_ejemplo.csv"
    ventas = leer_ventas(ruta)

    # Crear la columna "mes" a partir de la fecha (2026-03-15 -> 2026-03)
    for v in ventas:
        v["mes"] = v["fecha"][:7]

    por_vendedor = sumar_por(ventas, "vendedor")
    por_mes = sumar_por(ventas, "mes")

    print(f"Se leyeron {len(ventas)} ventas de {ruta.name}")
    imprimir_tabla("Ventas por vendedor", por_vendedor)
    imprimir_tabla("Ventas por mes", por_mes)

    salida = ruta.with_name(ruta.stem + "_resumen.csv")
    with open(salida, "w", newline="", encoding="utf-8-sig") as f:
        escritor = csv.writer(f, delimiter=";")    # ; para que Excel en español lo abra en columnas
        escritor.writerow(["Tipo", "Grupo", "Total"])
        for vendedor, total in por_vendedor.items():
            escritor.writerow(["Vendedor", vendedor, round(total)])
        for mes, total in sorted(por_mes.items()):
            escritor.writerow(["Mes", mes, round(total)])
    print(f"\nResumen guardado en: {salida}")


if __name__ == "__main__":
    main()
