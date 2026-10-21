A = int(input("Digite el valor de A: "))
B= int(input("Digite el valor de B: "))

if A <= 100 and A >= -100:
    if B <= 100 and B >= -100:
        if A <= B:
            print(list(range(A, B+1)))
        elif A > B:
            print(list(range(A, B-1, -1)))
else:
    print("A y B deben estar entre -100 y 100")


