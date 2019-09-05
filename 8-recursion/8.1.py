#8.1.
#Ребенок поднимается п о лестнице и з п ступенек. З а оди н шаг о н может пере­
#меститься на одну, две или три ступеньки. Реализуйте метод, рассчитывающий
#количество возможных вариантов перемещения ребенка по лестнице.
#Подсказки: 152, 178, 2 17, 237, 262, 359

# можно решать в лоб, как то так, но для 100 вычислисть на обычном компутере врядли удастся быстро
# def asd(n):
#     qwe = [v for v in [1, 2, 3] if v <= n]
#
#     while True:
#         start_qwe_len = len(qwe)
#
#         for i, v in enumerate(qwe):
#             qwe[i] = v + 1 if v+1 <= n else v
#
#         for i, v in enumerate(qwe[:start_qwe_len]):
#             if v + 1 <= n:
#                 qwe.append(v + 1)
#
#         for i, v in enumerate(qwe[:start_qwe_len]):
#             if v + 2 <= n:
#                 qwe.append(v + 2)
#
#         # print(len(qwe) , start_qwe_len)
#         if len(qwe) == start_qwe_len:
#             break
#
#     print(n, len(qwe))
#     return

# а можно вот так через кеширование
r = {
    1: 1,
    2: 2,
    3: 4
}

def asd(n):
    if n in r:
        print(n, r[n])
        return r[n]
    for i in range(4, n + 1):
        r[i] = r[i-3] + r[i-2] + r[i-1]
    print(n, r[n])

# tests============
asd(1)
asd(2)
asd(3)
asd(4)
asd(5)
asd(6)
asd(7)
asd(8)
asd(9)
asd(100)


