import math
# def sqrt(x):
#     try:
#         y = math.sqrt(x)
#     except TypeError:
#     # do something else
#         print("Error1")
#         nuevo_numero = int(input('Introduzca un numero para solucionar el error '))
#         #se podria resolver con recursividad
#         return sqrt(nuevo_numero)
#     except ValueError:
#     #do something else
#         print("Error2")
#     return y
class Gol():
    def __init__(self):
        print("gol")
    def marcaGol(self):
        print("golazo2")
    def numeroDeGoles(self,goles):
        print("se han marcado un total de "+ str(goles) +" goles", sep=':', end = " serresiete\n")
        Gol.marcaGol(self)
        print("hola")
    def sqrt(x):
        try:
            y = math.sqrt(x)
        except TypeError:
    # do something else
            print("Error1")
            nuevo_numero = input('Introduzca un numero para solucionar el error ')
            try:
                nuevo_numero= int(nuevo_numero)
                return Gol.sqrt(nuevo_numero)
            #if not isinstance(nuevo_numero, int):
                #try:
                #nuevo_numero = int(input('introduceme un numero de verdad pillin '))
            except(ValueError):
                    fallo = True
                    contador = 1
                    while(fallo):
                        contador = contador+1
                        texto1 = 'una vez vale pero '+ str(contador) +' ya es vicio '
                        texto2 = 'ya te estas pasando '
                        try:
                            if(contador<5):
                                nuevo_numero = int(input(texto1))#str(contador)
                            else:
                                nuevo_numero = int(input(texto2))
                            fallo = False
                        except(ValueError):
                            fallo = True
                    # nuevo_numero = input('introduceme un numero de verdad pillin ')
                    # while(not isinstance(int(nuevo_numero), int)):
                    #     print("vuelve")
                    #     nuevo_numero = input('introduceme un numero de verdad pillin ')
            return Gol.sqrt(nuevo_numero)

            #else:
            #se podria resolver con recursividad
                #return Gol.sqrt(nuevo_numero)
        except ValueError:
    #do something else
            print("Error2")
        return print(y)
def main():
    gol = Gol()
    j = 0
    gol.numeroDeGoles(j)
    print("a")
    gol.marcaGol()
    print("hola")
    Gol.sqrt("s")

if __name__ == "__main__":
    main()



# from enum import Enum
# class WeekDay(Enum):
#     Sun=0
#     Mon=1
#     Tue=2
#     Wen=3
#     Thu=4
#     Fri=5
#     Sat=6
# print(WeekDay.Sun.name)
# print(WeekDay.Mon.value)
# print(WeekDay["Sat"].name)
# print(WeekDay(4).name)

# # # def __init__(self):
# # #     print(" ")
# # def main():
# # #creating 2 new objects from the Semana Enum
# # #    lunes = Semana(lunes)
# #     lunes=Semana.LUNES
# #     martes=Semana.MARTES
# # # printing an enum value
# #     print(lunes,martes)
# # # calling a mutator method
# # if __name__ == "__main__":
# #     main()

# stringLeido = input('Introduzca dos numeros, separados por espacios')
# my_floats = stringLeido.split( )
# float1 = float(my_floats[0])
# float2 = float(my_floats[1])
# print(float1)
# print(float2)


# def mcd(numero1, numero2):
#     if (numero1 == numero2):
#         return numero1
#     elif (numero1 < numero2):
#         return mcd(numero1, numero2 - numero1)
#     else:
#         return mcd(numero1 - numero2, numero2)
# def main():
#     numero1 = 4454
#     numero2 = 143052
#     print("El m.c.d. es ", mcd(numero1, numero2))



# if __name__ == "__main__":
#     main()







    # def sqrt(x):
    #     try:
    #         y = math.sqrt(x)
    #     except TypeError:
    # # do something else
    #         print("Error1")
    #         fallo = True
    #         try:
    #                 nuevo_numero = int(input('Introduzca un numero para solucionar el error '))
    #         except(ValueError):
    #                     try:
    #                         while(fallo):
    #                             contador = 1
    #                             contador = contador+1
    #                             nuevo_numero = int(input('una vez vale pero '+ str(contador) + ' ya es vicio '))
    #                             return Gol.sqrt(nuevo_numero)
    #                     except(ValueError):
    #                         fallo = True # no es necesario esta sentencia pero es para dejar claro q si ha llegado aqui es q persiste en el error
    #                 # nuevo_numero = input('introduceme un numero de verdad pillin ')
    #                 # while(not isinstance(int(nuevo_numero), int)):
    #                 #     print("vuelve")
    #                 #     nuevo_numero = input('introduceme un numero de verdad pillin ')
    #             #return Gol.sqrt(nuevo_numero)
    #         return Gol.sqrt(nuevo_numero)
    #     except ValueError:
    #         print("Error2")
    #     return print(y)


    # def sqrt(x):
    #     try:
    #         y = math.sqrt(x)
    #         contador = 0
    #     except TypeError:
    # # do something else
    #         print("Error1")
    #         nuevo_numero = input('Introduzca un numero para solucionar el error ')
    #         if not isinstance(nuevo_numero, int):
    #             try:
    #                 nuevo_numero = int(input('introduceme un numero de verdad pillin '))
    #             except(ValueError):
    #                 fallo = True
    #                 while(fallo):
    #                     try:
    #                         nuevo_numero = int(input('una vez vale pero dos ya es vicio '))
    #                         fallo = False
    #                     except(ValueError):
    #                         fallo = True
    #                 # nuevo_numero = input('introduceme un numero de verdad pillin ')
    #                 # while(not isinstance(int(nuevo_numero), int)):
    #                 #     print("vuelve")
    #                 #     nuevo_numero = input('introduceme un numero de verdad pillin ')
    #             return Gol.sqrt(nuevo_numero)

    #         else:
    #         #se podria resolver con recursividad
    #             return Gol.sqrt(nuevo_numero)
    #     except ValueError:
    # #do something else
    #         print("Error2")
    #     return print(y)