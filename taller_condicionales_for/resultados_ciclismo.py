N = int(input("Número de ciclistas: "))
if N >= 1 and N <= 20:
    tiempo = 0
    velocidad = 0
    for k in range(N):
        id = int(input("identificador: "))
        min = int(input("Minutos: "))
        sec = int(input("Segundos: "))
        cent = int(input("Centesimas: "))
        if id >= 0 and min >= 0 and sec >= 0 and sec <= 59 and cent >= 0 and cent <= 99:
            tiempo = 60 * min + sec + cent / 100
            velocidad = 900 / tiempo
    print(id, velocidad, "Km/h")
    
