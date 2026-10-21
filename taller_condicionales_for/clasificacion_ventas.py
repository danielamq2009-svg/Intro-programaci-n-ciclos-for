N = int(input("Ingrese el número de ventas: "))
if N >= 0 and N <= 1000:
    importe = 0 
    cuantas_men_200 = 0
    cuantas_men_400 = 0
    cuantas_may_400 = 0
    for k in range(N):
        importe = int(input("Importe? "))
        if importe >= 0: 
            if importe <= 200:
                cuantas_men_200 = cuantas_men_200 + 1
            elif importe > 200 and importe < 400:
                cuantas_men_400 = cuantas_men_400 + 1
            elif importe >= 400:
                cuantas_may_400 = cuantas_may_400 + 1
    print("Grupo 1, 2 y 3:", cuantas_men_200, cuantas_men_400, cuantas_may_400)



