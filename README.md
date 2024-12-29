# Tic-Tac-Toe

## Escenario

Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:

- La máquina (por ejemplo, el programa) jugará utilizando las 'X's.
- El usuario (por ejemplo, tú) jugarás utilizando las 'O's.
- El primer movimiento es de la máquina - siempre coloca una 'X' en el centro del tablero.
- Todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia).
- El usuario ingresa su movimiento introduciendo el número de cuadro elegido - el número debe de ser válido, por ejemplo, un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado.
- El programa verifica si el juego ha terminado - existen cuatro posibles veredictos: el juego continúa, el juego termina en empate, tú ganas, o la máquina gana.
- La máquina responde con su movimiento y se verifica el estado del juego.
- No se debe implementar algún tipo de inteligencia artificial - la máquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.

El ejemplo del programa es el siguiente:

```
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
```

```
Ingresa tu movimiento: 1
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
```

```
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
```

```
Ingresa tu movimiento: 8
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
```

```
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
```

```
Ingresa tu movimiento: 4
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
```

```
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
```

```
Ingresa tu movimiento: 7
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
```

¡Has Ganado!

## Requerimientos

Implementa las siguientes características:

- El tablero debe ser almacenado como una lista de tres elementos, mientras que cada elemento es otra lista de tres elementos (la lista interna representa las filas) de manera que todos los cuadros puedas ser accedidos empleando la siguiente sintaxis:

    ```python
    board[row][column]
    ```

- Cada uno de los elementos internos de la lista puede contener 'O', 'X', o un dígito representando el número del cuadro (dicho cuadro se considera como libre).
- La apariencia del tablero debe de ser igual a la presentada en el ejemplo.
- Implementa las funciones definidas para ti en el editor.

Para obtener un valor numérico aleatorio se puede emplear una función integrada de Python denominada `randrange()`. El siguiente ejemplo muestra cómo utilizarla (El programa imprime 10 números aleatorios del 1 al 8).

Nota: la instrucción `from-import` provee acceso a la función `randrange` definida en un módulo externo de Python denominado `random`.

```python
from random import randrange

for i in range(10):
        print(randrange(8))
```