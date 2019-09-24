# Для двух строк напишите метод, определяющий, явля�тся ли одна строка
# перестановкой другой.


def f(s, c):
    if len(s) == len(c):
        if sorted(s) == sorted(c):
            return True
    return False

qwe = 'qwe'
asd = 'ewq'
print(f(qwe, asd))

qwe = ''
asd = ''
print(f(qwe, asd))

qwe = ''
asd = '2'
print(f(qwe, asd))

# либо посчитать число всех символов и сравнить их количество