
def calc():
    a = float(input("Первое число > "))
    if a == 0:
        print('Exit')
        return
    else:
        b = float(input("Второе число > "))

    oper = input("Операция? (+, -, *, /) >>> ")
    c = ""
    if b == 0:
        if oper == "/":
            try:
                print(1 / 0)
            except ZeroDivisionError:
                print('А-о...На ноль делить нельзя')
                calc()
    else:
        if oper == "*":
            c = a * b
        elif oper == "/":
            c = a / b
        elif oper == "+":
            c = a + b
        elif oper == "-":
            c = a - b
        else:
            c = "Выбрана неверная операция!"
            calc()
        print(c)
        calc()
calc()