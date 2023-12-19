"""ejercicio de la dispositiva de modulo. 3
def factorial(numero):
    resultado= 1 #se crea una variable para que por cada uno de los ciclos se vaya multiplicando por i 
    for i in range(1, numero+1):
        resultado = resultado*i
        print (resultado)
factorial (5) #colocar el numero cuyo factorial quiero """

"""ejemplo - clase 4
def esPrimo(numero)
    for i in range(2, numero): #empieza en 2 porque todo num div en 1 si da 0
        if numero%==0:
            return False
    return True
print (esPrimo(7))
"""
"""1)Diseña una función que tome como parámetro 2 números, 
y que devuelva una lista que contenga todos los números enteros entre estos 2 incluyendo ambos parámetros."""

def funcion1(parametro1,parametro2):
    lista=[]
    for i in range (parametro1,parametro2+1):
        lista.append(i)
    return lista

print(funcion1(10, 80))

"""2) Escribir una función que tome como parámetro 2 números, y retorne una lista con
todos los números pares entre estos, excluyendo a los parámetros."""
def espar(numero):
    if numero%2==0:
        return True
    return False

def funcion1(parametro1,parametro2):
    lista=[]
    for i in range (parametro1+1,parametro2):
        if espar(i):
            lista.append(i)
    return lista

print(funcion1(10, 80))

"""3)Escribir una función que tome 2 parámetros, el primero que reciba una cadena, y el segundo que reciba un carácter.
La función tendrá que retornar la cantidad de veces que aparece ese carácter en esa cadena."""

def parametros (cadena, caracter):
    cantidad = 0
    for i in range(len(cadena)): # entre parentesis decimos cuantas veces queremos que se analice la cadena
        if cadena[i]== caracter: 
            cantidad +=1
    return (cantidad)

print(parametros("Holaaa", "a"))

"""4)Elaborar una función que tome como parámetro 2 números, y retorne una lista con
todos los números primos entre ese rango de números.""" 

def numeros_primos(numero1, numero2):
        lista= []
        for i in range (numero1, numero2+1):
            if i%/=0:
                lista.append(i)
        return lista

print (numeros_primos(1,10))

"""5)Elaborar una función que tome como parámetro una lista, y devuelva un bool que diga
si en esa lista todos sus números son pares."""

def lista_pares():
    lista =[]
    for i in range:
        lista.append(i)
        if lista/2==0:
        return True

"""6)Elaborar una función que tome como parámetro una lista y devuelva un bool que diga
si en esa lista todos sus números son primos."""
def lista_primos():
    lista =[]
    for i in range:
        lista.append(i)
        if lista/2==0:
        return True
print lista_primos