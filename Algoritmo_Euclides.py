a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))

if a>b:
    mayor=a
    menor=b
    r=mayor%menor
    while r!=0:
        r1=menor%r
        r2=r
        menor=r
        r=r1

else:
    mayor=b
    menor=a
    r=mayor%menor
    while r!=0:
        r1=menor%r
        r2=r
        menor=r
        r=r1

print(f"El mcd es: {r2}")

    




