import pandas as pd

archivo_excel = "C:/Users/varga/PycharmProjects/automatizacionPython/resources/Data/dataEjecucion.xlsx"

def obtener_valor_en_celda(nombre_columna, numero_fila):
    try:
        # Carga el archivo Excel
        df = pd.read_excel(archivo_excel)
        # Obtener el valor en la celda especificada
        valor = df.loc[numero_fila - 2, nombre_columna]
        return valor
    except FileNotFoundError:
        print(f"No se encontró el archivo '{archivo_excel}'.")
        return None
    except KeyError:
        print(f"No se encontró la columna '{nombre_columna}' en el archivo Excel.")
        return None
    except IndexError:
        print(f"No hay suficientes filas en la columna '{nombre_columna}'.")
        return None

