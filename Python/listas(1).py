# """diseña una lista de 10 num

# lista=[]
# for i in range (10):
#     # num=int(input('digita una numero'))
#     # lista.append(num)
#     lista.append(int(input('digita una numero')))
# print(lista) """

# def saludar(nombre):
#     print('hola',nombre)

# saludar('pedro')

# lista=[1,3,5,7,9,2,4,6,8,10,1]

# print(lista.count(1))

# import random
# lista=[]
# suma=0
# for i in range (10):
#     lista.append(random.randint(1,10))
#     for j in range (10):
#         suma+=lista[j]
# print(f"Suma de lista {suma}")

# lista=[10,20,30,40,50,60,70,80,90,100]
# mayor= lista [9]
# for i in range (10):
#     if lista[i]>mayor:
#         mayor==lista[i]
# # print(f'mayor{mayor}')



# lista=[10,20,30,40,50,60,70,80,90,100]
# menor= lista [0]
# for i in range (10):
#     if lista[i]<menor:
#         menor==lista[i]
# print(f'menor{menor}')

# # ejercicios
# menu=0
# estudiante=[]
# notas=[]
# while menu!=5:
#     menu=int(input('''
# 1. nombres de los estudiante
# 2. ingresa las notas del estudiante 
# 3. mostrar la mayor nota del estudiante
# 4. salir
# digita una opcion '''))
#     match menu:
#         case 1:
#             for i in range(5):
#                 estudiante.append(input('digita un nombre'))
#         case 2:
#             for i in range(5):
#                 notas.append(float('digita un nota'))
#         case 3:
#             mayor=max(notas)
#             for i in range(5):
#                 if notas[i]==mayor:
#                     print(f'estudiante{estudiante[i]}:{notas[i]}')
#         case 4:
#             for i in range(5):
#                     print(f'estudiante{estudiante[i]}:{notas[i]}')
#         case 5:
#             salir=True
#             print('culminado')
#         case otro:
#             print('error')            
# menu=0
# animal=[]
# animalnum=0
# while menu!=5:
#     menu=int(input('''
#  1. nombres de los 10 animales
#  2. ordenar 
#  3. esta en la lista o no
#  4. mostar listado
#  5. salir
#  digita una opcion:  '''))
#     match menu:
#         case 1:
#             for i in range(10):
#                 animal.append(input('digita nombre del animal: ').lower)
#         case 2:
#             animal.sort()
#             for j in range(10):
#                 print(f'{animal[j]}')
#         case 3:
#             posicion=int(input('Digita desde la posicion que quieres ver '))
#             print(f'{animal[posicion:]}')
#         case 4:
#             buscar=input('Digita el animal que buscas ').lower
#             if buscar in animal:
#                 print('si esta')
#             else:
#                 print(f'animal no esta')
#         case 5:
#             salir=True
#             print('culminado')
#         case otro:
#             print('error')

# arreglo=[1,0,4,8,5,7,6,8,7,5,6,4,3,1,9,2,4,4]
# elemento =4
# posiciones=[]

# for i in range(0,len(arreglo)):
#     if arreglo[i]==elemento:
#         posiciones.append(i)
# print(f'{posiciones}')

# arreglo=[33,55,77,81,48]

# intentos=3
# usuarios=["pepito89","supermongui","espernangacion"]
# contrasenas=["123456","password","qwerty123"]
# while intentos>0:
#     usuario=input('digita tu usuario: ').lower()
#     contrasena=input('digita tu contraseña: ')
#     if usuario in usuarios:
#         if contrasena in contrasenas :
#             if usuarios.index(usuario)==contrasenas.index(contrasena):
#                 print('bienvenido')
#                 intentos=0
#             else:
#                 print('error')
#         else:
#             print('error')
#     else:
#         print('error') 
#     intentos=intentos-1  

# matriz=[[],[],[],[],[]]
# """ for horizontal in range (5):
#     for vertical in range (10):
#         matriz[horizontal].append((vertical+1)+(horizontal*10))
# print(matriz) """

# """ 
# Dada una matriz de m*n diseñar un algoritmo para sumar
# cada una de las filas y guardar los resultados en un vector
# llamado sumafila, sumar cada una de las columnas y guardar 
# los resultados en el vector sumacol, finalmente mostrar 
# los dos vectores """

# matriz=[[],[],[],[]]
# sumahor=[]
# sumaver=[]
# for horizontal in range (4):
#     suma1=0
#     for vertical in range (6):
#         matriz[horizontal].append((vertical+1)+(horizontal*6))
#         suma1+=matriz[horizontal][vertical]
#     sumahor.append(suma1)
# for horizontal in range (4):
#     suma2=0
#     for vertical in range (6):
#         matriz[horizontal].append((vertical+1)+(horizontal*6))
#         suma2+=matriz[vertical][horizontal]
#     sumaver.append(suma2)
# print(matriz)
# print(sumahor)
# print(sumaver)


""" vector1=['1','a',3,6,5,4,3,2]
vector2=['a','b',2,3,4,5]
for i in range(len(vector1)):
    cont=0
    for j in range(len(vector2)): """
        # if i==j:
            
            # print("esta")
"""     if vector1[i]==vector2[j]:
                cont+=1
                break """
            #     print(f'{vector1[i]} {vector2[j]}')
""" if cont==0:
print('El valor diferente entre vector y vector 2, es ',vector1[i]) """
        # else:
        #     i!=j
        #     print("no esta")
        #     if vector1[i]!=vector2[j]:
        #         print(f'{vector1[i]} {vector2[j]}')


# """ 5 dias """
# import statistics
# num=0
# bogota = [19, 19, 17, 18, 20]
# medellin=[27, 26, 26, 26, 27]
# bucaramanga=[27, 26, 26, 27, 29]
# ciudad_1 = statistics.mean(list(bogota))
# print(f'bogota esta por encima de los °{(max) (bogota)} grados')
# print(f'bogota esta por debajo de los °{(min) (bogota)} grados')
# ciudad_2 = statistics.mean(list(medellin))
# print(f'medellin esta por encima de los °{(max)(medellin)} grados')
# print(f'medellin esta por debajo de los °{(min)(medellin)} grados')
# ciudad_3 = statistics.mean(list(bucaramanga))
# print(f'bucaramanga esta por encima de los °{(max)(bucaramanga)}')
# print(f'bucaramanga esta por debajo de los °{(min)(bucaramanga)}')

# print (f'bogota: {ciudad_1} | madellin: {ciudad_2} | bucaramanga: {ciudad_3}')


# curso = [],[],[],[],[]
# suma = 0
# n = int(input("alumnos a registrar: "))
# for i in range(n):
#     curso[0].append(input(f"esribe nombre del alumno {i+1}: "))
#     curso[1].append(input(f"nombre el curso de {curso[0][i]}: "))
#     curso[2].append(input(f"género del alumno {curso[0][i]}: "))
#     for j in range(3):
#         notaInd = float(input(f"dime tu nota {j+1} {curso[0][i]}: "))
#         while notaInd < 0 or notaInd > 5:
#             print("Error de rango.")
#             notaInd = float(input(f"dime tu nota {j+1} {curso[0][i]}: "))
#         suma+=notaInd
#     curso[3].append(suma/3)
#     if(curso[3][i]<3.0):
#         curso[4].append("reprobo")
#     if(curso[3][i]<=5.0):
#         curso[4].append("aprobo")
#     else:
#         print('error')

#     suma = 0
# print(curso)

# suma,promedio=0,0
# n=int(input('numero de estudiantes'))
# estudiantess=[]
# estudiantes = {}
# for i in range(n): 
#     estudiantes["nombre"] = input('digita nombre')
#     estudiantes["genero"] = input('digita genero')
#     estudiantes["curso"] = int(input('digita curso'))
#     while int(estudiantes["curso"]) < 0 or int(estudiantes["curso"]) > 11:
#         print('Error de rango.')
#         estudiantes["curso"] = int(input('digita curso'))
#     for j in range(3):
#         nota=float(input('digita nota'))
#         while nota < 0 or nota > 5:
#             print("Error de rango.")
#             nota=float(input('digita nota'))
#             notaInd = float(input(f"dime tu nota {j+1} {nota}: "))
#         while notaInd < 0 or notaInd > 5:
#             print("Error de rango.")
#             notaInd = float(input(f"dime tu nota {j+1} {nota}: "))
#             suma+=notaInd
#             promedio = suma / 3
#             estudiantes["nota"] = promedio
#     if(notaInd>=3.5):
#         estudiantes["calificacion"] = "aprobo"
#     else:
#         estudiantes["calificacion"] = "aprobo"
#     print(estudiantes)
#         suma=0
#     estudiantess[i].append(estudiantes)
#     estudiantes = {}
# print(estudiantess)
