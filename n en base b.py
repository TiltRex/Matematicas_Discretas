try:
    n=int(input("Ingrese un numero entero: "))
    b=int(input("Ingrese un numero entero mayor a 1: "))

    c=n
    list=[n%b]

    while c!=1:
        c=int(c/b)
        mod=c%b
        list.append(mod)

    list.reverse()
    print(*list, sep = " ") 


except:
    print("Dato no valido, Intente de nuevo")
