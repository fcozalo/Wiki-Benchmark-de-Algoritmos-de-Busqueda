# Búsqueda por Funciones Hash

## Autor

Francisco Gonzalo García Kumul

---

## Análisis de complejidad

La **búsqueda por funciones hash** es un método que permite encontrar datos de forma rápida usando una función que transforma un valor en una posición dentro de una tabla.

En este proyecto, el programa trabaja con un archivo llamado `datos.txt`, el cual contiene aproximadamente **50,000 números enteros**. El programa realiza los siguientes pasos:

1. Lee los números desde el archivo `datos.txt`.
2. Convierte los datos en una lista de números enteros.
3. Ordena los números de menor a mayor.
4. Guarda la lista ordenada en `datos_ordenados.txt`.
5. Construye una tabla hash.
6. Pide al usuario un número para buscar.
7. Aplica una función hash al número buscado.
8. Busca el número dentro de la cubeta correspondiente.
9. Mide el tiempo de búsqueda en milisegundos.

Aunque la búsqueda por hash no necesita que los datos estén ordenados, en este proyecto se realiza el ordenamiento porque la actividad solicita que el archivo sea leído y ordenado antes de realizar la búsqueda.

---

### Método usado en el programa

El método implementado utiliza una **tabla hash con encadenamiento**.

Una tabla hash está formada por varias posiciones llamadas **cubetas**. Cada número se guarda en una cubeta dependiendo del resultado de la función hash.

La función hash utilizada en el programa es:

```text
clave = numero % tamanio_tabla
