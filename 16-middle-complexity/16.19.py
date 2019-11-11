def check(x, y, s):
    if x < 0 or y < 0 or x > len(qwe) - 1 or y > len(qwe[x]) - 1:
        return s

    if qwe[x][y] is None or qwe[x][y] != 0:
        return s
    s += 1
    # print(x,y,qwe[x][y])
    qwe[x][y] = None

    s = check(x - 1, y - 1, s)
    s = check(x - 1, y, s)
    s = check(x - 1, y + 1, s)
    s = check(x, y - 1, s)
    s = check(x, y + 1, s)

    s = check(x + 1, y - 1, s)
    s = check(x + 1, y, s)
    s = check(x + 1, y + 1, s)
    return s


def main(qwe):
    result = []
    for ir, row in enumerate(qwe):
        for ik, k in enumerate(row):
            if k is not None:
                ss = check(ir, ik, 0)
                if ss:
                    result.append(ss)
            else:
                continue
    return result


qwe = [
    [0, 2, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 1]
]

print(main(qwe))

qwe = [[]]
print(main(qwe))

qwe = [
    [0]
]
print(main(qwe))

qwe = [
    [0, 0, 0, 0]
]
print(main(qwe))
qwe = [
    [1, 1, 1, 1]
]
print(main(qwe))
