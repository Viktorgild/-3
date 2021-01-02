x = int(input("Введите первое число >>>"))
y = int(input("Введите второе число >>>"))


def new(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 0


result = new(x, y)

print(result)
