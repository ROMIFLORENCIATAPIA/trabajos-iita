#1)Escriba una función que muestre todos los números primos entre 1 y un número n que es ingresado por parámetro.
def primos (num):
    if num < 2:
        return False
    for i in range (2, num):
        if num % i == 0:
            return False 
    return True

n= int(input("ingrese un numero:"))
for num in range (1, n):
    if primos (num):
        print (f"Los numeros primos ingresados son: {num}")

"""2) Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta que el usuario ingrese ‘salir’. 
Cada vez que se ingrese un condimento, muestre un mensaje avisando que ya se agregó el condimento al sándwich.
 Escriba versiones diferentes del programa de acuerdo a estos criterios:
• Use un test condicional en el ciclo while para detener la ejecución.
• Use un test condicional dentro del ciclo para decidir si continuar la ejecución."""

def sandwich ():
    while True:
        condimento= input("cual condimento queres agregar:")
        if condimento =="salir":
            break
         else:
            print(f"Se agrego el condimento {condimento} a tu sandwich")

"""3) A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un tamaño y el mensaje que debería ir impreso en la remera. 
La función debe mostrar un mensaje describiendo el tamaño de la remera y el mensaje impreso en ella.
Llame la función una vez usando argumentos por posición. Llámela una segunda vez usando argumentos por clave."""

def hacer_remera(tamaño, mensaje):
remera: input(f"ingrese un talle {tamaño} e ingrese el mensaje a imprimir{mensaje}")
print hacer_remera(m, "hola mundo")


"""B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. 
Haga un par de remeras, la primera con los valores por defecto, y la segunda con valores diferentes."""

def hacer_remera(tamaño, mensaje):
    if hacer remera = (L, "me gusta Python"):
        print hacer_remera()
    else:
        remera: input(f"ingrese un talle {tamaño} e ingrese el mensaje a imprimir{mensaje}")

print hacer_remera(m, "hola mundo")

"""4) Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros de la serie de Fibonacci.
En esta serie, los primeros dos números son 0 y 1, y cada sucesivo número es la suma de los dos números inmediatamente anteriores
(ejemplo: 0,1,1,2,3,5,8,13,21,34,55,…)."""

num_fibonacci[0, 1]
def fibonacci():
    for i in num_fibonacci:
        suma == suma.num_fibonacci
        num_fibonacci.append(suma)
n = int(input("ingrese la cantidad de números de la serie de Fibonacci que desee generar: "))
result = num_fibonacci(n)
print(f"Los primeros {n} numeros de la serie de Fibonacci son: {result}") 


print ("Los numeros Fibonacci son los siguientes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55")
print()
def fibonacci(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series[:n]

n = int(input("ingrese la cantidad de números de la serie de Fibonacci que desee generar: "))
result = fibonacci(n)
print(f"Los primeros {n} numeros de la serie de Fibonacci son: {result}") 

 
"""5) (Opcional) Calculadora más inteligente: Modifique el ejercicio 9 del primer practico 
para que la calculadora sea capaz de devolver el resultado solamente de una operación especificada por el usuario. 
Por ejemplo, si el usuario ingresa dos numeros x, y, y luego ingresa ‘1’, la calculadora devuelve la suma entre los numeros x,y; 
si ingresa ‘2’, devuelve la resta, etc."""

inport match
numero1 = float (input( "introduce el primer número: "))
numero2 = float (input( "introduce el segundo número: "))

print("MENU DE OPCIONES")
print("1 multiplicación:")
print("2 división:")
print("3 suma:")
print("4 resta:")
print("5 raiz cuadrada:")
opcion = int (input("Ingrese una opcion:"))

if opcion == 1:
    print("La multiplicacion es:", (numero1*numero2))
elif opcion ==2:
    print("La división es:", (numero1/numero2))
elif opcion ==3:
    print("La suma es:", (numero1+numero2))
elif opcion==4:
    print("La resta es:", (numero1-numero2))
elif opcion==5:
    print("La raiz cuadrada es:", math.sqrt(numero1))
else:
    print("opcion no valida")

"""6) (Opcional) Conversión imperial: Desarrollar un programa en Python que pueda convertir gramos a libras,
centímetros a pulgadas y kilómetros a millas.
El programa debe permitir la conversión en ambos sentidos. 1.60934 Km = 1 milla 0.393701 pulgadas = 1 cm 0.00220462 libras = 1 gramo"""



"""7) (Opcional) Cuando un año es bisiesto, el mes más corto del año, febrero, tiene 29 días en vez de 28. Esto sucede casi cada 4 años. 
Los tres criterios que permiten saber si un año es bisiesto en el calendario gregoriano (el nuestro) son los siguientes:
• Si el año es divisible enteramente por 4, es bisiesto a menos que: o El año sea divisible por 100, entonces NO es bisiesto, a menos que:
▪ El año sea también divisible por 400. Entonces sí es un año bisiesto.
Esto significa que en el calendario gregoriano los años 2000 y 2400 son bisiestos,
 mientras que los años 1900, 2100, 2200 y 2300 no son bisiestos."""
#a) Escriba una función que tome un año y diga si es bisiesto o no.

def a_bisiesto():
    if (a_bisiesto==(%4==0) or (% 400 and %100 == 0))
    return True

solicito= int(input("ingrese un año"))
ingreso= a_bisiesto(solicito)
print:(f"El año {solicito} es bisiesto.")


#b) Modifique su programa para que devuelva todos los años bisiestos entre el año actual y el año pasado a la función como parámetro 
#(este debe ser posterior al año actual).
def a_bisiesto(2023, n):
    if (a_bisiesto==(%4==0) or (% 400 and %100 == 0))
    return True

solicito= int(input("ingrese un año"))
ingreso= a_bisiesto(2023, solicito)
print:(f"Los años bisiestos son:"{ingreso})

"""8) (Opcional) Si listamos todos los números naturales menores a 10 que son múltiplos de 3 o 5, obtenemos 3,5,6 y 9. 
La suma de estos múltiplos es 23. Encuentre la suma de todos los múltiplos de 3 o 5 menores a 1000."""

sum_multiples = sum(i for i in range(1,100) if i % 3 == 0 or i % 5 == 0)
print(sum_multiples)

total_sum = 0
for i in range (1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        total_sum += 1
print (total_sum)



