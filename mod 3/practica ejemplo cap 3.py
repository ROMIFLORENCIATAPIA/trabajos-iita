"""crear prog donde vamos a declarar un dicc para guardar los precios de la fruta.
 el prog pedira el nombre de la fruta y la cantidad que se vendio y nos mostrara el precio final de la fruta
 a partir de los datos guardados en el dicc. si la fruta no existe da error.
 tras cada consulta el prog pregunta si queremos hacer otra consulta"""



Frutas = {"manzana": 10, "naranja": 60, "durazno": 5, "Banana" : 20}
while True:
    ingreso_fruta = input("ingrese nombre de la fruta elegida: ")
    
    if ingreso_fruta == "No":
        break
    else:
        ingrese_cantidad = int( input("Ingrese cantidad de la fruta: "))
        precio_final = Frutas[ingreso_fruta] * ingrese_cantidad
        print(f"El precio de {ingreso_fruta} es {precio_final}.")




