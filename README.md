# Búsqueda por Funciones Hash Benchmark

## Autor

Francisco Gonzalo García Kumul

---

## Código con comentarios claros

El proyecto incluye un archivo principal llamado `main.py`, donde se implementa la búsqueda por funciones hash en Python.

El código está dividido en funciones para que sea más fácil de entender:

| Función | Descripción |
|---|---|
| `leer_numeros()` | Lee el archivo `datos.txt` y convierte su contenido en una lista de números enteros. |
| `esta_ordenada()` | Verifica que la lista de números esté ordenada correctamente. |
| `guardar_resultado()` | Guarda los números ordenados en el archivo `datos_ordenados.txt`. |
| `funcion_hash()` | Calcula la clave hash usando el operador módulo. |
| `construir_tabla_hash()` | Crea la tabla hash e inserta los números en sus cubetas correspondientes. |
| `buscar_en_hash()` | Busca el número ingresado por el usuario dentro de la tabla hash. |
| `pedir_numero()` | Solicita al usuario el número que desea buscar. |
| `main()` | Controla la ejecución general del programa. |

El código contiene comentarios en las partes importantes para explicar la lectura del archivo, el ordenamiento, la construcción de la tabla hash, el manejo de colisiones y la medición del tiempo.

---

## Análisis de complejidad

La búsqueda por funciones hash utiliza una función para calcular la posición donde debería encontrarse un dato.

En este programa se utiliza la siguiente función hash:

```text
clave = numero % tamanio_tabla
