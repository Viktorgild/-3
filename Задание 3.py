a = int(input("Введите первый аргумент >>>"))
b = int(input("Введите второй аргумент >>>"))
c = int(input("Введите третий аргумент >>>"))


def my_func(a, b, c):
    s = sorted((a, b, c), reverse=True)
    return s[0] + s[1]
resilt = my_func(a, b, c)

print(resilt)
