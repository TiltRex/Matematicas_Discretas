a=int(input("Numero 1: "))
b=int(input("Numero 2: "))

print("\n")

num1=a
num2=b

x0 = 1
x1 = 0
y0 = 0
y1 = 1

while b != 0:
    q = int(a/b)
    r = a%b
    x = x0 - q * x1
    y = y0 - q * y1

    print(f"{a}      {b}      {x0}      {y0}")

    a = b
    b = r

    x0 = x1
    x1 = x
    y0 = y1
    y1 = y


print(f"\n{a} = {num1}({x0}) + {num2}({y0})")
