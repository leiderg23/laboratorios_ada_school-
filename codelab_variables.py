# 3.Crear variables de diferentes tipos primitivos
cadena = "cadena"
entero = 42
flotante = 3.14
booleano = True

# 3.1 - Concatenar las variables y guardar el resultado en una nueva variable
concatenacion = cadena + str(entero) + str(flotante) + str(booleano) 

#           3.4 - Imprimir el resultado de la concatenación
print("Resultado de la concatenación:", concatenacion)

#   3.2 - investigacion
# Límite de los enteros:
    # Los enteros en Python no tienen un límite fijo, pero su tamaño está limitado por la memoria disponible en el sistema.
        # Python 3 admite enteros arbitrariamente grandes.

# Límite de los flotantes:
    # Los números de punto flotante en Python siguen el estándar IEEE 754 y tienen límites en términos de rango y precisión.
        # Para números de punto flotante de doble precisión, el rango es aproximadamente de 2.2e-308 a 1.8e308.

#       3.3:
# Calcular la suma de los primeros numeros pares

    #1ra manera de sumar los numeros pares
n = 2
suma_pares = n * (n + 1)

#           3.4 - Imprimir el resultado de la suma de los números pares
print("La suma de los primeros", n, "números pares es:", suma_pares)

#2da manera de sumar los numeros pares

numeros_pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Inicializar una variable para almacenar la suma
n = 0

# Recorrer la lista y sumar los números pares
for numero in numeros_pares:
    n += numero

#           3.4 - Imprimir el resultado
print("La suma de los números pares es:", n)

#3ra manera de sumar los numeros pares (mas dinamica)

# Inicializa una variable para almacenar la suma.
suma = 0
# Pide al usuario la cantidad de números pares que desea sumar.
n = int(input("¿Cuántos números pares desea sumar? "))

for i in range(n):
    numero_par = int(input(f"Ingrese el número par #{i + 1}: "))
    
    if numero_par % 2 == 0:
        suma += numero_par
    else:
        print("Este número no es par. Por favor, ingrese un número par.")
        
#           3.4 - imprimir resultados
print(f"La suma de los {n} números pares es: {suma}")