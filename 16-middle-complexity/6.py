# Для двух целочисленных массивов найдите пару значений (по одному зна­
# чению из каждого массива) с минимальной (неотрицательной) разностью.
# Верните эту разность.
# Пример:
# Ввод: { 1 , 3, 15 , 11, 2 } , {23, 127, 235, 19, 8}
# Вывод: 3 для пары ( 11 , 8).
# Подсказки: 632, 670, 679

# предварительная сортировка массивов будет в данном случае предпочтительнее так как сортировка это Nlog(N)
# а перебор всех возможных разностей A*B(A,B - длинны массивов)


def f(a, b):
    if not a or not b:
        return
    min_diff = abs(a[0] - b[0])
    pointer_a = 0
    pointer_b = 0

    while True:
        if a[pointer_a] < b[pointer_b]:
            if len(a) == pointer_a + 1:
                return min_diff
            pointer_a += 1
        else:
            if len(b) == pointer_b + 1:
                return min_diff
            pointer_b += 1

        if min_diff > abs(a[pointer_a] - b[pointer_b]):
            min_diff = abs(a[pointer_a] - b[pointer_b])

print(f(sorted((1 , 3, 15 , 11, 2 )) , sorted((23, 127, 235, 19, 8))))
print(f(sorted(()) , sorted(())))
print(f(sorted([0]) , sorted([0])))
print(f(sorted([0,1,2,3,4]) , sorted([5])))

