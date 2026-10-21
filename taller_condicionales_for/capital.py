C = int(input("Ingrese el capital, C: "))
I = float(input("Ingrese la tasa, I: "))
M = int(input("Ingrese el número de años, M: "))
if C >= 0 and I > 0 and I < 100 and M >= 0 and M < 50:
    saldo = C
    for k in range(1, M+1):
        saldo = saldo * (1 + I/100)
    print("El saldo es de: ", saldo)
else:
    print("Valores no validos.")