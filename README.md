# Búsqueda por Funciones Hash Benchmark

## Autor

Francisco Gonzalo García Kumul

---

## Código con comentarios claros

El repositorio contiene el archivo `main.py`, donde se implementa el algoritmo de **búsqueda por funciones hash** en Python.

El código está organizado por funciones y contiene comentarios para explicar las partes principales del programa, como la lectura del archivo, el ordenamiento de los datos, la construcción de la tabla hash, la función hash utilizada, el manejo de colisiones y la medición del tiempo de búsqueda.

Las funciones principales del código son:

| Función | Descripción |
|---|---|
| `leer_numeros()` | Lee el archivo `datos.txt` y convierte su contenido en una lista de números enteros. |
| `esta_ordenada()` | Verifica que los números hayan quedado ordenados correctamente. |
| `guardar_resultado()` | Guarda los números ordenados en el archivo `datos_ordenados.txt`. |
| `funcion_hash()` | Calcula la clave hash de cada número usando el operador módulo. |
| `construir_tabla_hash()` | Construye la tabla hash e inserta los números en sus cubetas correspondientes. |
| `buscar_en_hash()` | Busca el número ingresado por el usuario dentro de la tabla hash. |
| `pedir_numero()` | Solicita al usuario el número que desea buscar. |
| `main()` | Controla la ejecución general del programa. |

El programa realiza los siguientes pasos:

1. Lee el archivo `datos.txt`.
2. Convierte los datos en una lista de números enteros.
3. Ordena los números de menor a mayor.
4. Verifica que la lista esté correctamente ordenada.
5. Guarda la lista ordenada en `datos_ordenados.txt`.
6. Construye una tabla hash.
7. Solicita al usuario un número para buscar.
8. Busca el número usando la función hash.
9. Mide el tiempo de búsqueda en milisegundos.
10. Muestra si el número fue encontrado o no.

La función hash utilizada en el código es:

```text
clave = numero % tamanio_tabla
