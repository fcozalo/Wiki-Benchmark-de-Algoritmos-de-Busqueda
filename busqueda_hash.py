import os
import time


def leer_numeros(ruta_archivo):
    numeros = []

    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

            contenido = contenido.replace(",", " ")
            contenido = contenido.replace(";", " ")

            partes = contenido.split()

            for dato in partes:
                numeros.append(int(dato))

    except FileNotFoundError:
        print("Error: No se encontró el archivo.")
        print("Ruta buscada:", ruta_archivo)
        return []

    except ValueError:
        print("Error: El archivo contiene datos que no son números enteros.")
        return []

    return numeros


def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False

    return True


def guardar_resultado(ruta_archivo, lista):
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        for numero in lista:
            archivo.write(str(numero) + "\n")


def funcion_hash(numero, tamanio_tabla):
    return numero % tamanio_tabla


def construir_tabla_hash(lista, tamanio_tabla):
    tabla = []

    for i in range(tamanio_tabla):
        tabla.append([])

    for indice in range(len(lista)):
        numero = lista[indice]
        clave = funcion_hash(numero, tamanio_tabla)

        tabla[clave].append([numero, indice])

    return tabla


def buscar_en_hash(tabla, numero_buscado, tamanio_tabla):
    clave = funcion_hash(numero_buscado, tamanio_tabla)

    posiciones = []

    for elemento in tabla[clave]:
        numero = elemento[0]
        indice = elemento[1]

        if numero == numero_buscado:
            posiciones.append(indice)

    return posiciones, clave, len(tabla[clave])


def pedir_numero():
    correcto = False
    numero = 0

    while correcto == False:
        try:
            numero = int(input("\nIngresa el número que quieres buscar: "))
            correcto = True
        except ValueError:
            print("Error: Debes ingresar un número entero.")

    return numero


def main():
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))

    ruta_datos = os.path.join(carpeta_actual, "datos.txt")
    ruta_salida = os.path.join(carpeta_actual, "datos_ordenados.txt")

    print("Carpeta del programa:", carpeta_actual)
    print("Buscando archivo en:", ruta_datos)

    numeros = leer_numeros(ruta_datos)

    if len(numeros) == 0:
        print("No hay datos para procesar.")
        return

    print("Cantidad de números leídos:", len(numeros))

    inicio_ordenamiento = time.perf_counter()

    numeros.sort()

    fin_ordenamiento = time.perf_counter()

    tiempo_ordenamiento_ms = (fin_ordenamiento - inicio_ordenamiento) * 1000

    print("\nOrdenamiento terminado.")
    print("Tiempo de ordenamiento:", round(tiempo_ordenamiento_ms, 4), "ms")

    if esta_ordenada(numeros):
        print("Verificación: La lista está ordenada correctamente.")
    else:
        print("Verificación: La lista NO está ordenada correctamente.")

    guardar_resultado(ruta_salida, numeros)
    print("Lista ordenada guardada en:", ruta_salida)

    tamanio_tabla = 100003

    print("\nConstruyendo tabla hash...")

    inicio_hash = time.perf_counter()

    tabla_hash = construir_tabla_hash(numeros, tamanio_tabla)

    fin_hash = time.perf_counter()

    tiempo_hash_ms = (fin_hash - inicio_hash) * 1000

    print("Tabla hash construida.")
    print("Tiempo de construcción de tabla hash:", round(tiempo_hash_ms, 4), "ms")

    numero_buscado = pedir_numero()

    inicio_busqueda = time.perf_counter()

    posiciones, clave, elementos_en_cubeta = buscar_en_hash(tabla_hash, numero_buscado, tamanio_tabla)

    fin_busqueda = time.perf_counter()

    tiempo_busqueda_ms = (fin_busqueda - inicio_busqueda) * 1000

    print("\nResultado de la búsqueda")
    print("Número buscado:", numero_buscado)
    print("Clave hash generada:", clave)
    print("Elementos revisados en esa cubeta:", elementos_en_cubeta)
    print("Tiempo de búsqueda:", round(tiempo_busqueda_ms, 6), "ms")

    if len(posiciones) > 0:
        print("Estado: Número encontrado.")
        print("Cantidad de veces que aparece:", len(posiciones))
        print("Primera posición en la lista ordenada:", posiciones[0])
    else:
        print("Estado: Número no encontrado.")


main()