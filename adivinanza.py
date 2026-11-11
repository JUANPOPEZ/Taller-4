import random

# 1. Generamos el número aleatorio secreto entre 1 y 100
secreto = random.randint(1, 100)
intentos = 0

print("=== JUEGO DE ADIVINANZAS ===")
print("He seleccionado un número entre 1 y 100. ¡Intenta adivinarlo!")

# 2. Ciclo de interacción con el usuario
while True:
    intento = int(input("\nIngresa tu número: "))
    intentos += 1
    
    if intento < secreto:
        print("-> El número secreto es MAYOR.")
    elif intento > secreto:
        print("-> El número secreto es MENOR.")
    else:
        print(f"\n¡Felicitaciones! Adivinaste el número secreto ({secreto}) en {intentos} intentos.")
        input("\nPresiona Enter para salir...")
        break
