n = int(input("Cantidad de empleados: "))

if n >= 1 and n <= 40:
    total_nomina = 0

    for i in range(n):
        identificador = int(input("Identificador: "))
        edad = int(input("Edad: "))
        antiguedad = int(input("Antigüedad: "))

        suma = 0

        for j in range(1, antiguedad + 1):
            suma = suma + j

        sueldo = (100 + edad + suma) / antiguedad

        print("Empleado:", identificador, "- Sueldo:", sueldo)

        total_nomina = total_nomina + sueldo

        if i == 0:
            mayor_sueldo = sueldo
            menor_sueldo = sueldo
            id_mayor = identificador
            id_menor = identificador
        else:
            if sueldo > mayor_sueldo:
                mayor_sueldo = sueldo
                id_mayor = identificador

            if sueldo < menor_sueldo:
                menor_sueldo = sueldo
                id_menor = identificador

    print("Total de la nómina:", total_nomina)
    print("Identificador del mayor sueldo:", id_mayor)
    print("Identificador del menor sueldo:", id_menor)

else:
    print("Error: N debe estar entre 1 y 40.")