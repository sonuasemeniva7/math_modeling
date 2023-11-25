from const import g
def pop(m, v, h, g):
    d = m * g * h
    f = (m * (v ** 2)) / 2
    y = d + f
    return d, f, y
m = int(input())
v = int(input())
h = int(input())
print(pop(m, v, h, g))