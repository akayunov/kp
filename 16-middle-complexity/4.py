#16.4. Разработайте алгоритм, проверяющий результат игры в крестики-нолики.

# 0 - empty
# 1 - x
# 2 - 0

# пройти по всем строкам, столбцам, диагоналям и посмотреть нет ли последовательностей одинаковых символом длинной 3

def check_list(line):
    counter_map = {
        1:0,
        2:0
    }
    previous_symbol = line[0]
    counter_map[line[0]] = 1
    for current_symbol in line[1:]:
        if previous_symbol == current_symbol:
            counter_map[current_symbol] += 1
            if counter_map[1] >= 3:
                return 'x win'

            if counter_map[2] >= 3:
                return 'o win'
        else:
            counter_map[previous_symbol] = 0
            counter_map[current_symbol] = 1
def f(t):
    # строки
    for line in t:
        result = check_list(line)
        if result:
            return result
    # стoлбцы
    for column_count in range(len(t[0])):
        result = check_list([line[column_count] for line in t])
        if result:
            return result
    # диагонали
    r1 = []
    r2 = []
    for line_count in range(len(t)):
        r1.append(t[line_count][line_count])
        r2.append(t[line_count][len(t) - 1 - line_count])

    print(r1, r2)
    return check_list(r1) or check_list(r2)

t = [
    [1, 2, 1],
    [0, 1, 2],
    [0, 0, 1],
]


print(f(t))

t = [
    [1, 1, 1],
    [0, 2, 2],
    [0, 0, 1],
]


print(f(t))

t = [
    [1, 2, 1],
    [0, 2, 2],
    [0, 2, 1],
]


print(f(t))
