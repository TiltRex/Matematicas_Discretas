a=int(input("Ingrese un numero entero positivo para la base: "))
n=int(input("Ingrese un numero entero positivo para el exponente: "))

list=[a%2] #Numero binario
list2=[] #Exponentes
list3=[] #Potencias


exp=0
num=1
rta=1



while n!=0:
    n=int(n/2)
    mod=n%2
    list.append(mod)

for x in range(len(list)-1):
    list2.append(num)
    num*=2

    exp=list[x]*list2[x]
    list2.append(exp)
    list2.pop(x)
    

list.reverse()
list.remove(0)

for x in range(len(list2)):
    list3.append(a)
    a=a*a

for x in range(len(list2)):
    if list2[x]!=0:
        rta*=list3[x]

print(rta)



