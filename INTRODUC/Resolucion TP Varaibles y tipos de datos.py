#Ejercicio 1

mensaje="Este es un mensaje"
print(mensaje)

mensaje="Este es un nuevo mensaje"
print(mensaje)

#Ejercicio 2

nombre="Leo"
print("Hola ",nombre,", ¿Te gusta Programar en Python?")

#Ejercicio 3

print(2+3+3)
print(108-100)
print(2*4)
print(24/3)

#Ejercicio 4
mi_entero=10
mi_decimal=5.8
mi_string="hola mundo"
mi_booleano = True
print(type(mi_entero))
print(type(mi_decimal))
print(type(mi_string))
print(type(mi_booleano))

#Ejercicio 5
entrada=float(input("Ingrese un numero decimal: "))
print(int(entrada))

#Ejercicio 6
print("1!=2 ", 1!=2)
print("True==1 ", True==1)
print("False!=False ", False!=False)
print("True>0 ", True>0)
print("1.0<1 ", 1.0<1)
print("test==test ", "test"=="test")
print("1.0>=1 ", 1.0>=1)

#Ejercicio 7
name=input("ingresa tu nombre: ")
edad=int(input("ingresa tu edad: "))
anio=2022+(100-edad) #primero resto la edad de la persona a los 100 años y luego los sumo al año actual
print(name+", vas a cumplir 100 años en: ",anio)

#Ejercicio 8

celcius=float(input("ingresar temperatura en Grados Celcius: "))
fahrenheit=(9.0/5.0)*celcius+32 #aqui se hace la conversion y se guarda el resultado en la variable fahrenheit
print("La Temperatura en grados Fahrenheit es: ",fahrenheit)


#Ejercicio 9

PrimerNumero=float(input("Ingrese el primer numero: "))
SegundoNumero=float(input("Ingrese el segundo numero: "))
print("Suma: ",PrimerNumero+SegundoNumero)
print("Resta: ",PrimerNumero-SegundoNumero)
print("Producto: ",PrimerNumero*SegundoNumero)
print("División: ",PrimerNumero/SegundoNumero)
print("Potencia: ",PrimerNumero**SegundoNumero)
print("Division entera: ",PrimerNumero//SegundoNumero)
