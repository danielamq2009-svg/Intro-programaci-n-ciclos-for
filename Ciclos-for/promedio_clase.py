"""
Ejemplo:
Un profesor necesita crear un programa que le ayude a calcular el promeedio de notas de un salon de clases.
El ingresa el nombre y el valor de nota final de cada estudiante.
Al final el necesita saber cuál es el mejor estudiante y el promedio de todo el curso.
Cada nota es de 0 a 5.0.
"""
cantidad_est = int(input("Cantidad de estudiantes:"))
mejor_est = ""
nota_mayor = 0.0
suma = 0.0 
promedio = 0.0

for veces in range(cantidad_est):
    print("Estudiante #", veces)
    nombre = input("Nombre:")
    nota = float(input("Nota:"))

    suma = suma + nota # <- Acumuladores

    if nota > nota_mayor:
        nota_mayor = nota
        mejor_est = nombre
promedio = suma / cantidad_est

print("El promediio del curso es: ", promedio)
print("El mejor estudiante es: ", mejor_est, " con nota de: ", nota_mayor)
