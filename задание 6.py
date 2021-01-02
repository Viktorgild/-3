# int_func = input("Введите слова >>>")
# print(int_func.title())

int_func = input("Введите слова >>>")
while int_func:
    def capitalize(line):
        return ' '.join([s[0].upper() + s[1:] for s in line.split(' ')])
     print(int_func)