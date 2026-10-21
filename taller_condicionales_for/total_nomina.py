N = int(input("Número de empleados: "))
if N > 0 and N <= 1000:
    nomina = 0
    for k in range(1, N+1):
        sueldo = int(input("Sueldo por empleado "+str(k)))
        nomina = sueldo + nomina
    print("El valor de la nomina es: ", nomina)
else:
    print("Valor invalido.")
