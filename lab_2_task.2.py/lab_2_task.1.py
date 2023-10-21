a = int(input('введите первый член:'))
q = int(input('введите знаменатель:'))
n = int(input('Введите число элементов: '))

for i in range(1, n + 1):
    s= a * q ** (i-1)
    print(s)
    


    
