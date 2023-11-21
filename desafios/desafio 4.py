"""Desafio Factorial: Pedir un numero al usuario y calcular y mostrar su factorial SIN UTILIZAR ningún ciclo (Ni while ni for). 
Si se pueden utilizar estructuras condicionales no repetitivas (if, elif, else).
Para este desafío las unicas funciones permitidas son input(), print(), 
los conversores (int(),float(),str(),bool(),list()) y funciones propias.
Esta restricción tambien aplica a librerias.
El código debe funcionar sin errores."""

#opcion 1
def factorial(x,n): #funcion para el calculo de factorial de n numero
	if(n>0):
		x=factorial(x,n-1)
		x=x*n
	else:
		x=1
	return x

numero = int(input("inserta un numero: ")) #pido el numero
calculo=factorial(1,numero) #calculo factorial de ese numero
print (f"El factorial de {numero} es {calculo}") #muestro factorial

#opcion 2

def calculo_factorial(numero):   #funcion para el calculo de factorial de n numero
    factorial = 1
    if numero < 0:
        return "No se puede calcular el factorial de un número negativo."
    elif numero == 0:
        return 1
    else:
        for i in range(1, numero + 1):
            factorial *= i
        return factorial

numero = int(input("Ingrese un número para calcular su factorial: "))  #pido el numero
resultado = calculo_factorial(numero)   #calculo factorial de ese numero
print(f"El factorial de {numero} es {resultado}")  #muestro factorial


