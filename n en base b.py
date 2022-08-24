try:
    n=int(input("Ingrese un numero entero: "))
    b=int(input("Ingrese un numero entero mayor a 1: "))

    if b<2:
        exit()

    
    list=[n%b]

    while n!=0:
        n=int(n/b)
        mod=n%b
        list.append(mod)

    list.reverse()
    list.remove(0)
    print(*list, sep = " ") 


except:
    print("Dato no valido, Intente de nuevo")
