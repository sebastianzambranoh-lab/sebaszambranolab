# Aprender a programar para automatizar tu trabajo

Este repositorio es una ruta de aprendizaje **práctica y en español** para pasar de
"nunca he programado" a "tengo scripts que hacen mis tareas repetitivas por mí".

Usamos **Python** porque:
- Se lee casi como inglés sencillo.
- Es el lenguaje más usado para automatizar oficina: archivos, Excel, correos, PDFs, web.
- Es gratis y funciona en Windows, Mac y Linux.

---

## 0. Preparar tu computador (una sola vez)

1. Instala Python desde https://www.python.org/downloads/
   - **En Windows marca la casilla "Add Python to PATH"** al instalar.
2. Instala un editor: **Visual Studio Code** (https://code.visualstudio.com/) y su extensión "Python".
3. Comprueba que funciona. Abre una terminal (en Windows: "Símbolo del sistema" o "PowerShell") y escribe:
   ```
   python --version
   ```
   Debe responder algo como `Python 3.12.x`.
4. Descarga este repositorio (botón verde **Code → Download ZIP**) y descomprímelo.

## Cómo ejecutar una lección

Desde una terminal ubicada en la carpeta del repositorio:

```
python 01_fundamentos/01_variables.py
```

**Método de estudio recomendado** para cada archivo:
1. **Lee** el archivo completo. Los comentarios (líneas con `#`) explican cada paso.
2. **Predice** qué va a mostrar antes de ejecutarlo.
3. **Ejecútalo** y compara con tu predicción.
4. **Modifícalo**: cambia valores, rómpelo a propósito y lee el error.
5. Haz los **ejercicios** del final del archivo.

> Equivocarse y leer el mensaje de error es la forma normal de programar. No es fallar.

---

## Ruta de aprendizaje

| Semana | Carpeta | Qué aprendes |
|---|---|---|
| 1 | `01_fundamentos/01_variables.py` | Guardar datos: textos, números, cálculos |
| 1 | `01_fundamentos/02_decisiones.py` | `if / elif / else`: que el programa decida |
| 2 | `01_fundamentos/03_bucles.py` | `for` y `while`: repetir tareas sin copiar y pegar |
| 2 | `01_fundamentos/04_listas_diccionarios.py` | Manejar muchos datos a la vez |
| 3 | `01_fundamentos/05_funciones.py` | Empaquetar pasos en bloques reutilizables |
| 3 | `02_archivos/01_leer_escribir.py` | Leer y crear archivos de texto |
| 4 | `02_archivos/02_csv.py` | Leer y escribir tablas (CSV, lo que exporta Excel) |
| 4+ | `03_automatizaciones/` | Scripts reales listos para adaptar |

### Automatizaciones incluidas (`03_automatizaciones/`)

| Script | Qué hace |
|---|---|
| `organizar_carpeta.py` | Ordena una carpeta desordenada (p. ej. Descargas) en subcarpetas por tipo: PDFs, imágenes, Excel… |
| `renombrar_archivos.py` | Renombra muchos archivos en lote con un patrón (fecha, numeración) |
| `reporte_ventas.py` | Lee un CSV de ventas y genera un resumen por vendedor y por mes |

Todos usan solo lo que trae Python de fábrica y tienen un **modo de prueba**
que muestra qué harían sin tocar nada.

---

## Cómo leer código que no escribiste

Cuando abras cualquier script (de aquí o de internet):
1. **Busca el final primero**: casi siempre hay un `if __name__ == "__main__":` que dice qué se ejecuta.
2. **Identifica las entradas** (qué archivo o datos lee) y **las salidas** (qué crea o muestra).
3. **Lee los nombres de las funciones** (`def ...`): suelen contar la historia del programa.
4. **Ejecútalo con datos de prueba**, nunca con tus archivos importantes la primera vez.
5. **Pon `print(...)`** en medio para ver qué valor tiene cada variable.

## Siguientes pasos (después de terminar esta ruta)

- **Excel de verdad (.xlsx)**: librería `openpyxl` o `pandas` (`pip install openpyxl pandas`).
- **PDFs**: `pypdf`.
- **Correos**: `smtplib` (incluido en Python) o la API de Gmail/Outlook.
- **Páginas web / formularios**: `requests` y `playwright`.
- **Programar tareas**: el Programador de tareas de Windows o `cron` en Mac/Linux.
- Libro gratuito recomendado: *Automate the Boring Stuff with Python* (https://automatetheboringstuff.com).

¿Tienes una tarea rutinaria concreta? Descríbela (qué archivos usas, qué pasos haces a mano)
y se puede convertir en un nuevo script en `03_automatizaciones/`.
