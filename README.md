# Taller 4: Juego de Adivinanzas en Python

Programa interactivo por consola en Python donde el usuario debe adivinar un número aleatorio generado por la computadora, con retroalimentación en tiempo real y contador de intentos.

---

## Estructura del Taller (Metodología de 90 minutos)

### 1. Comprensión (10 min)
* **Descripción del problema:**
  Desarrollar un juego interactivo por consola en el que la computadora elija un número entero aleatorio entre 1 y 100, y el usuario intente adivinarlo en la menor cantidad de intentos posibles.
* **Entradas (Inputs):** Números enteros ingresados por el usuario desde la terminal.
* **Salidas (Outputs):**
  - Mensaje de pista: si el número secreto es **mayor** al ingresado.
  - Mensaje de pista: si el número secreto es **menor** al ingresado.
  - Mensaje de felicitación indicando el número secreto y la cantidad total de intentos.
* **Procesamiento:** Generación del número secreto con `random.randint`, validación condicional y contador acumulativo de intentos.

### 2. Diseño (15 min)
* **Algoritmo / Pseudocódigo:**
  ```text
  INICIO
      secreto <- número_aleatorio_entre(1, 100)
      intentos <- 0
      
      Escribir "Bienvenido al juego de adivinanzas. Adivina el número del 1 al 100."
      
      REPETIR
          Escribir "Ingresa tu número:"
          Leer intento
          intentos <- intentos + 1
          
          SI intento < secreto ENTONCES
              Escribir "El número secreto es MAYOR."
          SINO SI intento > secreto ENTONCES
              Escribir "El número secreto es MENOR."
          SINO
              Escribir "¡Felicitaciones! Adivinaste el número en ", intentos, " intentos."
              ROMPER_CICLO
          FIN SI
      HASTA QUE acierte
  FIN
  ```

### 3. Desarrollo (40 min)
* **Archivo principal:** [`adivinanza.py`](./adivinanza.py)
* **Ejecutable para Windows:** [`jugar.bat`](./jugar.bat)
* **Características:**
  - Código conciso, legible y modular (menos de 25 líneas).
  - Ejecución nativa en terminal para máxima velocidad y cero latencia de interfaz gráfica.
  - No requiere librerías externas.

### 4. Pruebas (15 min)
Matriz de validación con número de control:

| N° | Caso de Prueba | Entrada | Salida Esperada | Resultado |
| :---: | :--- | :---: | :--- | :---: |
| 1 | Pista "Mayor" | `20` | `-> El número secreto es MAYOR.` | **Aprobado** |
| 2 | Pista "Menor" | `75` | `-> El número secreto es MENOR.` | **Aprobado** |
| 3 | Límite inferior | `1` | Pista adecuada según el valor secreto | **Aprobado** |
| 4 | Límite superior | `100` | Pista adecuada según el valor secreto | **Aprobado** |
| 5 | Acierto final | Coincidencia | Felicitaciones y conteo exacto de intentos | **Aprobado** |

### 5. Entrega (10 min)
* **Instrucciones de ejecución:**
  - **Opción 1 (Doble clic):** Ejecutar [`jugar.bat`](./jugar.bat).
  - **Opción 2 (Terminal):**
    ```bash
    python adivinanza.py
    ```
