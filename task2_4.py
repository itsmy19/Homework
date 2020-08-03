n = int(input('Введите количество элементов: '))
e = 1
s = 0
for i in range(n):
    s += e
    e /= -2
print('Их сумма:', s)