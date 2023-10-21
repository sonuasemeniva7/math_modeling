print("ax^2 + bx + c = 0:")
import
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)
 
if discr > 0:
    r = (-b + math.sqrt(discr)) / (2 * a)
    f = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (r, f))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")