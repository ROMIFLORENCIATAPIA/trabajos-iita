"""Determinar el  mayor , el menor y el promedio TODOS los números ingresados por el usuario.
La cantidad de números a ingresar también tendrá que ser ingresada por el usuario.
Pautas de evaluacion:
-Unicamente utilizar la funcion print(), input(), y conversores
+Cumplimiento de la consigna al 100%. (obligatorio)
+Que el programa finalice sin errores (obligatorio)

Por ejemplo: Ingrese cuantos numeros va a ingresar: 5

Ingrese numero: 5
ingrese numero: 2
ingrese numero: -2
ingrese numero: 6
ingrese numero: 8

El mayor numero que ingresó fue 8
El menor numero que ingreseo fue -2
El promedio de los numeros es 3.8"""

ingresos= int(input("Cuantos numeros va a ingresar: "))
mayor = None
menor = None
suma = 0
for i in range(ingresos):
    numero = float(input("Ingrese el número: "))
    suma += numero
    if mayor is None or numero > mayor:
        mayor = numero
    if menor is None or numero < menor:
        menor = numero
promedio = suma/ingresos

print("El mayor número es:", mayor)
print("El menor número es:", menor)
print("El promedio de los números ingresados es:", promedio)







