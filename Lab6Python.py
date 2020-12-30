import math

def f(x, y):
    funres = (x**2)-(y**2)
    return funres

def g(x, y, z):
    funres = (x + y) / (4 * z * x)
    return funres



a= float(input("Введіть а "))
b= float(input("Введіть b "))
c= float(input("Введіть c "))
d= float(input("Введіть d "))

res = (f(a, b) + f(c, d) / math.sqrt(g(a, b, c))) + ((c-g(a, b, c)+1)/f(b, c) - f(a, b))*(1+(g(a, b, c)/(f(b, c)-f(a, c))))
print(res)


