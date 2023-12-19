"""1) Pida un número al usuario y determine si es par o impar."""
num = int(input ("ingrese un numero: "))
if num % 2 == 0: 
    print ("el numero ingresado es par")
else:
    print ("el numero ingresado es impar")


"""2) Escriba una cadena if-elif-else que determine el estado de vida de una persona.
• Si la persona tiene menos de 2 años, muestre un mensaje que diga que es un bebe.
• Si tiene al menos 2 años, pero menos de 4, muestre que es un infante.
• Si tiene al menos 4, pero menos de 12, muestre que es un niño.
• Si tiene al menos 13, pero menos de 20, muestre que es un adolescente.
• Si tiene al menos 20 pero menos de 65, muestre que es un adulto.
• Si tiene 65 o más, muestre que es un anciano."""

edad= int(input("ingrese su edad:" ))
if edad< 2:
    print("es un bebe")
elif 4>edad<12:
    print("es un niño")
elif 13>edad<20:
    print("es un adolescente")
elif 21>edad<65:
    print("es un adulto")
else:
    print ("es un anciano")


"""3) Cree un ciclo que nunca termine y ejecútelo. Puede probarlo haciendo que muestre algo en
pantalla por cada pasada del ciclo. Para finalizarlo, presione Ctrl-C o el comando para detener
la ejecución correspondiente a su editor"""

nombre = input("ingrese un nombre:")
while nombre != None:
    print(nombre)

"""4) Escriba un programa que contenga dos ciclos while anidados que muestre los enteros del 1
al 100, diez números por línea, como se muestra abajo:
1 2 3 4 5 6 7 8 9 10
11 12 13 14 15 16 17 18 19 20
21 22 23 24 25 26 27 28 29 30
. . 91 92 93 94 95 96 97 98 99 100"""
num=1
contador= 0
while num<100:
    contador = 0
    linea = ""
    while contador !=10:
        linea += str(num) + ","
        num +=1
        contador +=1
    print(linea)

"""5) Resuelva el ejercicio anterior usando solo un ciclo while"""    
numero = 1
while numero <= 100:
     if numero % 10 == 0:
         print(numero)
     else:
         print(numero,end = "-")
     numero += 1


    