# 16.9. Напишите методы, реализующие операции умножения, вычитания и деления
# целых чисел. Результатом во всех сrrучаях должно быть целое чисiiо. В коде
# разрешается испол�;.зовать только оператор сложения.

def neg(a):
    # да выглядит так как будто есть знаки минус - то ест ькак бы используем вычитание 0 - 1
    # но в предложенном решение есть строка  int newSign = а < 0 ? 1 : -1; - то есть как бы тоже есть знак минус, ну и чего тогда мудрить
    return -a


def substract(a, b):
    return a + neg(b)


def multiply(a, b):
    res = 0
    if abs(a) < abs(b):  # быстрее складывать меньшее число раз
        for i in range(abs(a)):
            res += b
        if a < 0:
            res = -res
        return res
    else:
        for i in range(abs(b)):
            res += a
        if b < 0:
            res = -res
        return res


def devide(a, b):
    # a/b
    if a == 0:
        return 0
    res = 0
    for i in range(abs(a)):
        res += b
        if abs(res) > abs(a):
            if multiply(a,b) < 0:
                return -i
            return i


# print(substract(3, 1))
# print(substract(-10, 1))

# print(multiply(1, 3))
# print(multiply(10, 3))
# print(multiply(-1, 3))
# print(multiply(1, -3))
# print(multiply(0, -3))
# print(multiply(0, 0))

print(devide(10, 3))
print(devide(10, -3))
print(devide(-10, 3))
print(devide(10, 0))
print(devide(0, -3))
print(devide(-0, -3))