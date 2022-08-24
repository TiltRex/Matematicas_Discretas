a=int(input("Numero 1: "))
b=int(input("Numero 2: "))

num1=a
num2=b
 
u0 = 1
u1 = 0
v0 = 0
v1 = 1

while b != 0:
    q = a//b
    r = a - b * q
    u = u0 - q * u1
    v = v0 - q * v1

    a = b
    b = r

    u0 = u1
    u1 = u
    v0 = v1
    v1 = v

print(f"{a} = {num1}({u0}) + {num2}({v0})")