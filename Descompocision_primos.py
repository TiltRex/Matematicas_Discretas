import math

num=int(input("Ingrese un numero: "))

list=[2]
list2=[]
y=2
n=0

for x in range(2,int(num/2)+1):
    if x%y!=0:
        list.append(x)

while num!=1:
    if num%list[n]==0:
        list2.append(list[n])
        num=num/list[n]
    else:
        n+=1


print(list2)