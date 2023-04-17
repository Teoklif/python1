n = int(input('Введите n: '))
m = int(input('Введите m: '))
k = int(input('Введите k: '))

if k<n*m and (k % n==10 or k % m ==0):
        print('yes')
else:
        print('no')