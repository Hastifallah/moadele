import math

a=float(input("enter number a:"))
b=float(input("enter number b:"))
c=float(input("enter number c:"))
x=(b**b)-(4.0*a*c)
d=(-b+math.sqrt(b**2-4*a*c)/2)
z=(-b-math.sqrt(b**2-4*a*c)/2)
print(d)
print(z)
