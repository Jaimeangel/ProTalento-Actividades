# Definición de variables de diferentes tipos primitivos
entero = 42
flotante = 3.14
cadena = "Hola, mundo"
booleano = True

# Concatenar las variables en una cadena haciendo las respectivas conversiones
resultado = str(entero) + " " + str(flotante) + " " + cadena + " " + str(booleano)

# Imprimir el resultado
print(resultado)

# Límites de los enteros en Python

# El tipo de dato 'int' en Python no tiene un límite estricto.
# Puedes representar enteros muy grandes sin preocuparte por un desbordamiento.
# Python maneja automáticamente la asignación de memoria según sea necesario.

# Ejemplo de un entero grande
big_integer = 10**1000
print(big_integer)

# Límites de los flotantes en Python

# Los flotantes en Python siguen el estándar IEEE 754 y tienen un límite en la representación de números reales.
# Esto significa que tienen una precisión limitada y pueden no representar números muy grandes o muy pequeños con precisión.
# La precisión de los flotantes se vuelve menos precisa a medida que los números se alejan de cero.

# Ejemplo de un flotante muy grande
big_float = 1.0e308
print(big_float)

# Ejemplo de un flotante muy pequeño
small_float = 1.0e-308
print(small_float)

# Solicitar al usuario que ingrese un valor entero para 'n'
n = int(input("Ingresa un valor entero para n: "))

# Calcular la suma de los primeros n números pares
suma = n * (n + 1)

# Imprimir el resultado
print(f"La suma de los primeros {n} números pares es: {suma}")