
even_count, odd_count = 0, 0
n = input("Введите натуральное число: ")
n1 = [int(x) for x in str(n)]
for i in n1:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers in the list: ", even_count)

print("Odd numbers in the list: ", odd_count)
