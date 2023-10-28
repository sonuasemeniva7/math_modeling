import lec_3_my_module
print(lec_3_my_module.a)

b = lec_3_my_module.b * 3
print(b)

print(lec_3_my_module.c[2])

import lec_3_my_module as mm
print(mm.a)

b = mm.b * 3
print(b)

print(mm.c[2] + b + mm.c[0])

from lec_3_my_module import a, b

print( a* b)
from lec_3_my_module import *
 
print(c[2] * c[1])