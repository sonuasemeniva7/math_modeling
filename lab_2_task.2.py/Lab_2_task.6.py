a=9
for i in range(1, a+1):
     print(*range(i, i*a+1, i), sep='\t')