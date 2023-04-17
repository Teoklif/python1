n = int(input('Введите номер билета для расчета суммы цифр'))

a= n%10
b = n//10%10
c = n//100%10

a2 = n//1000%10
b2=n//10000%10
c2 = n//100000%10


sum1 = a+b+c
sum2 = a2+b2+c2

if sum1==sum2:
    print(f'sum1 = {sum1}, sum2 = {sum2}, yes')

else:
    print(f'sum1 = {(sum1)}, sum2 = {(sum2)}, no')
