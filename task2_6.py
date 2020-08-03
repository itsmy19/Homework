import random

print("Я загадал число от 1 до 100. Попробуй угадай.")
print("Я буду давать подсказки")
the_number = random.randint(1, 100)
number_user = int(input("Твой вариант: "))
pop = 10
while number_user != the_number:
    if number_user > the_number:
        print("Меньше...")
    else:
        print("Больше...")
    if pop == 0:
        break
    number_user = int(input("Твой вариант: "))
    pop -= 1

if number_user != the_number:
    print("Ты истратил все попытки")
else:
    print("Молодец!")
