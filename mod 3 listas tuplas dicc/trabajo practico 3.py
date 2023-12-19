"""1) Meter los números del 1 al 20 en una lista y mostrarla en pantalla. Hacer lo mismo
para un rango de números indicado por un usuario."""
 
lista = []
for i in range (21):
    lista.append(i)
print(lista)

lista = []
x = int(input("ingresar inicio: "))
y = int(input("ingresar final: "))
for i in range (x , y):
    lista.append(i)
print(lista)

"""2) Pide un número y guarda en una lista su tabla de multiplicar hasta el 10. Por
ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50"""

n = int(input("ingrese un numero: "))
lista = []
for i in range (1, 11, 1):
    lista.append((i)* n)
print(lista)


"""3) Pide una cadena (string) por teclado, mete los caracteres en una lista sin repetir
caracteres."""

cadena = input("ingrese cadena: ")
caracteres = []
for i in cadena:
    if i not in caracteres:
        caracteres.append(i)
print(caracteres)

"""4) Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios."""

cadena = input("ingrese cadena: ")
caracteres = []
for i in cadena:
    if i != " ":
        caracteres.append(i)
print(caracteres)

#5) Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.
tupla = (1, 2, 3, 4)

repetido = 0
nuevo = int(input("ingrese numero: "))
for i in range (len(tupla)):
    if tupla[i] == nuevo:
        repetido = repetido + 1
        print (f"El numero se repite {repetido} veces") 

#crea lista donde se agreguen num y diga cuantos se repiten

listaNum=[]
while True:
    num=input("ingrese un numero:")
    if num=="":
        break
    else:
        listaNum.append(int(num))

def caracterRepetido(numero):
    repetido=0
    for i in range(len(listaNum)):
        if listaNum[i]==numero:
            repetido=repetido + 1
    print(f"el numero{numero} se ha repetido{repetido}veces")


"""6) Crea una tupla con los meses del año, pedir números al usuario. Si el numero esta
entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino
muestra un mensaje de error. El programa termina cuando el usuario introduce un
cero"""

meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

while True:
    num = int(input("ingrese un numero: "))
    if num == 0:
        break
    elif 0<=num<=12:
        print ({meses[num - 1]})
    else:
        print("error")

"""7) Crea una tupla con números e indica el número con mayor valor y el que menor
tenga."""

tupla = (1, 2, 3, 4, 5)
mayor_valor = tupla[0]
menor_valor = tupla[0]
for i in tupla:
    if i > mayor_valor:
        mayor_valor = i
    elif i < menor_valor:
        menor_valor = i
print(f"El numero de mayor valor es {mayor} y el de menor valor es {menor}")

"""8) (Opcional)Escribir un programa que vaya solicitando al usuario que ingrese
nombres. - Si el nombre se encuentra en la agenda (implementada con un
diccionario), debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no
es correcto. - Si el nombre no se encuentra, debe permitir ingresar el teléfono
correspondiente. El usuario puede utilizar la cadena "*", para salir del programa"""

dicc_agenda= {"maria": "87654367", "pedro": "10239876", "juan": "67543290", "ana": "98123456"}
nuevo_contacto = ""
while True:
    nombre = input("Ingrese nombre: ")
    if nombre == "*":
        break
    if nombre in dicc_agenda:
        print (nombre) + (dicc_agenda [nombre])
        preguntar = input("desea modificar telefono?: ")
        if preguntar == "si":
            print (int("ingrese nuevo numero: "))
    else:
    print("Ese nombre no exite en la agenda...")
    dicc_agenda[nuevo_cotacto] = {(input("ingrese nombre:")): int(input("ingrese telefono: "))}

"""9) Opcional: Pide números y mételos en una lista, cuando el usuario meta un 0 ya
dejaremos de insertar. Por último, muestra los números ordenados de menor a
mayor."""

num_ingresado = 1
lista_de_num = []
while num_ingresado != 0:
    num_ingresado = int(input("ingrese un numero: "))
    if num_ingresado == 0:
        break
    else:
        lista_de_num.append(num_ingresado)
        
for i in range (len(lista_de_num)-1):
    print (lista_de_num)


"""10) Opcional: Lo mismo que el anterior, pero ordenando de mayor a menor."""
num = int(input("ingree un numero: "))
lista_de_num = []
while num != 0:
    if num == 0:
        break
    else:
        lista_de_num.append(num)
for i in range (len(lista_de_num)+1):
    print (lista_de_num)


"""11) Opcional: Codificador Morse: Desarrolle un programa en Python que permita al
usuario escribir un mensaje y convertirlo a código Morse. La codificación Morse se
presenta en la siguiente tabla:"""

Codificador_Morse = {"a":".-","b": "-...","c":"-.-.","d":"-..","e":".","f":"..-.",
                   "g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..",
                   "m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.",
                   "s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--",
                   "z":"--.."," ":"  "}

while True:
    ingreso = input("¿Tiene un mensaje?: ")
    if ingreso == "no":
         print("no hay mensaje")
         break
    else:
        ingreso=("ingrese mensaje")
        codigo_morse = ""
        for caracter in ingreso:
            codigo_morse+= Codificador_Morse[caracter]
    print(codigo_morse)
