"""Encontrar el primer caracter no repetido en un string.
Pautas de evaluacion:
    +No utilizar ciclos for o while anidados (obligatorio)
    +Unicamente se puede utilizar la funcion input(), la funcion print() y la funcion len() (obligatorio)
    +Que el programa finalice sin errores (obligatorio)
Ejemplo:
Ingrese una cadena: abbcssadd
La primera letra que no se repite es: c"""

"""ingreso = input("ingrese texto: ")
for i in (len(ingreso)):
    if i in (ingreso):
        print (i)"""

def parametros (cadena, caracter):
    caracteres = 0
    for caracter in cadena:
        caracteres==caracteres+1
        return caracteres

print parametros("hola", "a")

#o también 

def encontrar_primer_no_repetido(texto):
    for i in texto:
        if texto.count(char) == 1:
            return char
    return None 

texto = input("Ingresa un string: ")
primer_no_repetido = encontrar_primer_no_repetido(texto)

if primer_no_repetido:
    print("El primer carácter no repetido es:", primer_no_repetido)
else:
    print("No hay caracteres no repetidos.")
