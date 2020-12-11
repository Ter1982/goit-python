import math

a = 1
b = 4
c = 3
d = b**2 - 4 * a * c
print(F"Дискриминант D = {d}")   
x1 = (-1.0 + math.sqrt(d)) / (2 * a)
x2 = (-3.0 - math.sqrt(d)) / (2 * a)       
print(f"X1={x1} X2={x2}")


