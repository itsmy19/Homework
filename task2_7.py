number = int(input('Введите число: '))
a = 0
for i in range(1,number+1):
    a += i
b = number * (number + 1) // 2
print(a)
print(b)