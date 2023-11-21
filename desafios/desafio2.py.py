"""Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. 
Pautas de evalucion: Solo esta permitido utilizar la funcion, input(), print() y las creadas por uno mismo
Aclaracion: Si recibe "Qué lindo día que hace hoy" debe devolver: {'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}"""

cadena_ingresada = input("Ingrese texto: ")

def contar_palabras(cadena_ingresada):
    palabras = [cadena_ingresada (1,1,1)]
    aparece= {}
    for i in palabras:
        if i in aparece:
            aparece [i] += 1
        else:
            aparece [i] = 1  
    return aparece

ingreso_cadena = input("ingrese una cadena:")
cadena= contar_palabras(cadena_ingresada)
print(cadena)

