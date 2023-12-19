class gato:

    def __init__(self, nombre, pelo,ojos,cansancio,hambre):
        self.nombre = nombre
        self.colordepelo = pelo
        self.colordeojo = ojos
        self.cansancio = cansancio
        self.hambre = hambre


    def comer(self):
        if self.hambre == 0: 
            print (f"dar comida")
        else:
            print (f"{self.nombre} esta satisfecho")

    def dormir(self):
        if self.cansancio == 100:
            print (f"{self.nombre} debe dormir")
        else:
            print (f"{self.nombre} puede jugar")

    def jugar(self):
        if self.cansancio < 100:
            print (f"{self.nombre} tiene energía para jugar")
            self.cansancio = (self.cansancio - 10)

    def acariciar(self):
        if self.cansancio == 0:
            print(f"acariciar")

gato1= gato ("pp", "blanco", "negro", 2, 7)
gato2= gato ("qq", "marron", "gris", 0, 9)
gato3= gato ("mm", "negro","celeste", 8, 0)

gato3.comer()
gato2.dormir() 
gato3.acariciar()
