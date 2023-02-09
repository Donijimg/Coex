""" cantidadN=int(input('numero de empledos: '))
diccionarios=[]
diccionario={
    "nombre":"",
    "antiguedad":"",
    "horas_labor":"",
    "pago_por_horas":"",
    "operacion":"",
}
for i in range(cantidadN): 
    diccionario["nombre"] = input('digita nombre: ')
    diccionario["antiguedad"] = int(input('digita antiguedad: '))
    diccionario["horas_labor"] = int(input('digita horas labor: '))
    diccionario["pago_por_horas"] = int(input('digita pago por hora: '))
    valorxhora=diccionario["horas_labor"]*diccionario["pago_por_horas"]
    valortotal=valorxhora+diccionario["antiguedad"]*30
    descuento=valortotal*13/100
    valorneto=descuento
    diccionarios.append(diccionario)
    diccionario["operacion"] = (f'valor por hora: {valorxhora},valor total:{valortotal},descuento: {descuento},valor neto: {valorneto}')
    print(f'{diccionarios},')
    diccionario={} """
promedio=0,0
dics=[]
dic = {}
opcion=0
while opcion!=3:
    opcion=int(input('''
1. ingresa cantidad de estudiantes
2. ingresa datos
3. salir
digita una opcion '''))
    match opcion:
        case 1:
            n=int(input('numero de estudiantes: '))
        case 2:
            for i in range(n): 
                dic["nombre"] = input('digita nombre: ')
                dic["codigo"] = input('digita codigo: ')
                dic["promedio"] = float(input('digita promedio: '))
        case 3:
            if >=7.0):
                dic["promedio"] = "aprobo"
            else:
                estudiantes["calificacion"] = "aprobo"

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