"""Clase 17/11/23
Practica lista : va recorriendo uno por uno los elementos en este caso hasta el 6, teniendo en cuenta las posiciones.

lista = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < 6:
    elemento = lista [i]
    i +=1

lista = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < 6:
    elemento = lista [i]
    print (elemento)
    i +=1

lista = []
for i in range (int(input()))
    lista.append(i)
print (lista)

while i < len:
    elemento = lista [i]
    print (elemento)
    i +=1

ejemplo desde que valor empieza y hasta donde llegue y de cuanto en cuanto 
for i in range (0, 10, 2):
    print (i)

dada una lista hacer un programa que muestre unicamente los numeros pares

lista = [22, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0 
while i  % 2 == 0:
    elemento = lista [i]
    print (elemento)
    i +=1

Me muestra los elementos de la lista, i me muestra los elementos 
for i in range (len(lista)):  ---Le indico que sea segun el tamaño de la lista 
    if lista [i] % 2 == 0:
        print (lista [1]) """


#ejercicio de la teoria
#lista = []
#for i in range (36):
#    lista.append(i)
#print(lista)

#lista = []
#x = int(input("ingresar inicio: "))
#y = int(input("ingresar final: "))
#for i in range (x , y):
#    lista.append(i)
#print(lista)


#Pedir una palabra al usuario, meter los todos sus caracteres en una lista y mostrarla en pantalla.

palabra = input ("ingrese palabra: ")
lista = []
for i in range (len (palabra)):
    lista.append(palabra[i])
print (palabra[i]) 

#3. Pide una cadena string por teclado, mete los caracteres en una lista sin espacios.
palabra = input ("ingrese palabra: ")
lista = []
for i in range (len (palabra)):
    if palabra[i] != " ":
    lista.append(palabra[i])
print (palabra[i]) 

