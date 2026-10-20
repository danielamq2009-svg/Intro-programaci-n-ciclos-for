"""
Ejemplo:
Calcular el factorial de un numero.

fact(n): 1 * 2 * 3.....* n; 0! = 1

ejemplo: 
5! = 5*4*3*2*1 = 120
"""
n = int(input("n?"))
if n == 0:
    print("1")
elif n > 0: 
    fact = 1
    for num in range(1, n+1):
        fact = fact * num
    print(n,"! =", fact)
else: 
    print("Error. n debe ser mayor o igual a cero")