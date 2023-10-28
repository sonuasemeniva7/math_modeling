a = [4, 16, 10, 5, 7, 1, 8]
sslice = a[2:5:1] #вырезаем кусок
print(sslice)

import numpy as np
 
a = [1, 5, 3, 6]
ssslice = a[0:2:1]
print(ssslice)
 
sslice = a[3:0:-1]
print(sslice)

sllice = a[::-1]
print(sllice)

b = np.array([a, np.array(a)*3])
print(b)

slicce = b[1,2:3:1]
print(slicce)




sliice = b[::, 1]
print(sliice)
