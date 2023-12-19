#Ejercicio 1

#numero_limite = int(input("Ingrese el valor limite: "))
#lista = []
#for i in range(1,numero_limite +1 ):
#     lista.append(i)
#print(lista)


#Ejercicio 2

# numero = int(input("Ingrese un numero: "))
# lista = []
# for i in range(11):
#     lista.append(numero*i)
# print(lista)


#Ejercicio 3

# cadena = input("Ingrese una cadena: ")
# lista = []
# for caracter in cadena:
#     if caracter not in lista:
#         lista.append(caracter)

# print(lista)

#Ejercio 4

# cadena = input("Ingrese una cadena: ")
# lista = []
# for caracter in cadena:
#     if caracter != " ":
#         lista.append(caracter)

# print(lista)

#Ejercio 5

# tupla = (1,2,3,4,5,5,5,5,3,1)

# numero = int(input("Ingresa un numero: "))

# contador = 0
# for i in range(tupla.__len__()):
#     if tupla[i] == numero:
#         contador += 1
# print(f"El numero se repite {contador} veces")

#Ejercio 6

# TUPLA_DE_MESES = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio"
#                   ,"Agosto","Septiembre","Octubre","Novienbre","Diciembre")


# Numero_Ingreso = ""
# while Numero_Ingreso != "SALIR":
#     print("Si queres salir escribi SALIR")
#     Numero_Ingreso = int(input("Ingrese un numero para mostrar al mes que corresponde: "))
#     if Numero_Ingreso > 12:
#         print("Ese mes no existe, proba nuevamente")
#     else:
#         print(f"\nEl numero {Numero_Ingreso} corresponde al mes {TUPLA_DE_MESES[Numero_Ingreso-1]}\n")
        

#Ejercicio 7

# TUPLA_DE_NUMEROS = (5,2,3,4,5,6,-3,2,-2,6)

# Mayor_Numero = TUPLA_DE_NUMEROS[0]

# Menor_Numero = TUPLA_DE_NUMEROS[0]

# for  numero in TUPLA_DE_NUMEROS:
#     if numero < Menor_Numero:
#         Menor_Numero = numero
#     elif numero > Mayor_Numero:
#         Mayor_Numero = numero

# print(f"El mayor numero es: {Mayor_Numero}, y el menor numero es: {Menor_Numero}")


#Ejercicio 8

# Agenda = {}

# ingreso = ""
# while True:
#     ingreso = input("Ingresa un nombre para buscar su numero: ")
#     if(ingreso == "*"):
#         break
#     if ingreso.lower() in Agenda:
#         print(f"El numero de {ingreso} es: {Agenda[ingreso]}")
#     else:
#         print("Ese nombre no exite en la agenda...")
#         Agenda[ingreso] = int(input("Escribe el numero:"))
# print(Agenda)

#Ejercicio 9 y 10

# ingreso = 1                                             #Esta parte carga los numeros en una lista
# lista = []
# while ingreso != 0:
#     ingreso = int(input("Ingrese un numero: "))
#     lista.append(ingreso)

# lista_ordenada = False                                 #Esta parte ordena los numeros de una lista de menor a mayor,
# while lista_ordenada == False:                         #En este caso se usa un metodo llamado, ordenamiento de burbuja. para entenderlo mejor mira:
#     lista_ordenada = True                               #https://www.youtube.com/watch?v=Hd5jp935ays&ab_channel=ChristianA.Morales
#     for i in range(len(lista)-1):
#         numero_1 = lista[i]
#         numero_2 = lista[i+1]
#         if(numero_1>numero_2):                            #Cambiar el signo en esta parte me ordena de mayor a menor o de menor a mayor
#             lista[i],lista[i+1] = numero_2 , numero_1
#             lista_ordenada = False

# lista.sort()                #Esto tambien ordena una lista, es otra forma mas facil de hacer en PYTHON, 
                                #Internamente realiza una tarea parecida a la de arriba, seguramente no la misma
# lista.sort(reverse=True)    #Con este truco podemos ordenarla al reves

# print(lista) #Muestro la lista


#Ejercicio 11

# Tracutor_Morse = {"a":".-","b": "-...","c":"-.-.","d":"-..","e":".","f":"..-.",
#                   "g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..",
#                   "m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.",
#                   "s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--",
#                   "z":"--.."," ":"     "}


# while True:
#     ingreso = input("Ingrese su palabra a traducir: ")
#     if(ingreso == "SALIR"):
#         print("Saliendo")
#         break
#     codigo_morse = ""
#     for caracter in ingreso:
#         codigo_morse+= Tracutor_Morse[caracter]
#     print(codigo_morse)
       
