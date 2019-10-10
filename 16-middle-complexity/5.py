# Напишите алгоритм, вычисляющий число завершающих нулей в n ! .

# 0 появляется только если есть умножение 5 на 2 = 10
# двоек очевидно больше чем пятерок так что просто считаем сколько раз в нашем факториале будут перемножаться пятерки
# для этоге не обязательно раскалыдвать каждый множитель факториала на простые множители
# достаточно просто проверить сколько раз в его простые множители входит 5 а значит просто поделить множитель на 5

def f(x):
    r = 0
    for i in range(5, x + 1, 5):
        while i % 5 == 0:
            r += 1
            i /= 5
    return r

def f3(num):
    count = 0
    if num < 0:
        return - 1
    # сколько 5 находиться в разложении данного множителяб например 10 / 5 = 2 - два раза 5 будет
    # и еще надо учесть что в некоторые множители 5 может входить по нескольку раз
    # например 25, 25/5 = 5, но 5-рок в разложении будет 6 штук так как 25 = 5*5
    i = 5
    while num/i >= 1:
        # в первом цикле учли пятерки, во втором 25-ки, в третем 125 и тд
        count += num / i
        i *= 5
    return int(count)


print(f3(25))
print(f(25))
print(f3(125))
print(f(125))
print(f(20))
print(f(17))
print(f(10))
print(f(5))

