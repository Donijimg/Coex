"correccion de mision"
suma,promedio=0,0
coex=[[],[],[],[],[],[]]
notas=[]
opcion=0
sumatoria=0
contador=10
while opcion!=13:
    opcion=int(input('''
1. Solicite la cantidad N de talentos 
2. Registrar los datos de los talentos en una matriz 2xN (Código y Nombre)
3. Registrar nota de Misión 1
4. Registrar nota de Misión 2
5. Registrar nota de Misión 3
6. Registrar prueba de nivel final
7. Mostrar nombre y nota del talento con la mejor nota en la Misión 1
8. Mostrar nombre y nota del talento con la mejor nota en la Misión 2
9. Mostrar nombre y nota del talento con la mejor nota en la Misión 3
10.Mostrar el nombre y el promedio de cada talento (el promedio se obtiene
de las 4 pruebas)
11.Mostrar código, nombre, nota misión1, nota mision2 y nota misión 3, y
prueba final
12.Nombre de los talentos que desarrollaron el ejercicio
13.Salir
digita una opcion '''))
    match opcion:
        case 1:
            n=int(input("Solicito la cantidad de talentos: "))
        case 2:
                for i in range(n):
                    # coex[0].append(input(f"escribe nombre del talento{i+1}: "))
                    # while [0] =="":
                    #     contador+=coex
                    #     print('error')
                    #     coex[0].append(input(f"escribe nombre del talento{i+1}: "))
                    coex[1].append(input(f"digita codigo{i+1}: "))
                    while [1] in coex:
                        coex[1]+=contador
                        coex[1] = input(f"Ingresar el nombre del talento #{i+1}: ")
        # case 3:
        #     for i in range(n):
        #         nota1=float(input('digite mision 1: '))
        #         while nota1 < 0 or nota1 > 100:
        #             print("Error de rango.")
        #             nota1=float(input('digite mision 1: '))
        #         coex[2].append(nota1)
        # case 4:
        #     for i in range(n):
        #         nota2=float(input('digite mision 2: '))
        #         while nota2 < 0 or nota2 > 100:
        #             print("Error de rango.")
        #             nota2=float(input('digite mision 2 : '))
        #         coex[3].append(nota2)
                    
        # case 5:
        #     for i in range(n):
        #         nota3=float(input('digite mision 3: '))
        #         while nota3 < 0 or nota3 > 100:
        #             print("Error de rango.")
        #             nota3=float(input('digite mision 3 : '))
        #         coex[4].append(nota3)
        # case 6:
        #     for i in range(n):
        #         notaF=float(input('digite prueba de nivel final: '))
        #         while notaF < 0 or notaF > 100:
        #             print("Error de rango.")
        #             notaF=float(input('digite prueba de  nivel final: '))
        #         coex[5].append(notaF)
        # case 7:
        #     maximo1=max(coex[2])
        #     for i in range(n):
        #         if coex[2][i]==maximo1:
        #             print(f'nombre del talento:{coex[0][i]} y nota de su mision: {coex[2][i]}')
        # case 8:
        #     maximo2=max(coex[3])
        #     for i in range(n):
        #         if coex[3][i]==maximo2:
        #             print(f'nombre del talento:{coex[0][i]} y nota de su mision: {coex[3][i]}')
        # case 9:
        #     maximo3=max(coex[4])
        #     for i in range(n):
        #         if coex[4][i]==maximo3:
        #             print(f'nombre del talento:{coex[0][i]} y nota de su mision: {coex[4][i]}')
        # case 10:
        #     for i in range(n): #Columna
        #         for j in range (2,6): #Fila    
        #             sumatoria += coex[j][i]
        #             promedio = sumatoria/4
        #         print(f'nombre{coex[0][i]},nota promedio {promedio}')
        #         sumatoria = 0