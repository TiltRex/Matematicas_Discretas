
n=int(input("Cuantos numeros desea generar: "))
num=int(input("En que numero quiere inciar: "))

a=int(input("Defina el multiplicador: "))
c=int(input("Defina el desface: "))


for x in range(n):
    print(num)
    num=(a*num+c)%1000
    
