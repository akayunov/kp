#8.2)
#Робот стоит в левом верхнем углу сетки, состоящей из r строк и с столбцов.
#Робот может перемещаться в двух направлениях: вправо и вниз, но некоторые
#ячейки сетки заблокированы, то есть робот через них проходить не может.
#Разработайте алгоритм построения маршрута от левого верхнего до правого
#нижнего угла.
#Подсказки: 33 1 , 360, 388


class Cell:
    def __init__(self, lock=False):
        self.lock = lock  # cell can be visited or not
        self.flag = False  # was cell visited or not?


def qwe():
    if not s or not s[0]:
        print('Empty s')
        return
    if not s[0][0].lock:
        s[0][0].flag = True
    else:
        print('Impossible to find path because of first sell is locked')
        return

    current_cells = [(0, 0)]

    while current_cells:
        temp = []
        for x, y in current_cells:
            if x + 1 <= len(s) - 1 and not s[x + 1][y].lock:
                s[x + 1][y].flag = True
                if (x + 1, y) not in temp:  # in one cell we can walk by different paths so check it
                                            # all path which lead to cell will have same length because we walk only by corner with 90 gradusov
                    temp.append((x + 1, y))
            if y + 1 <= len(s[0]) - 1 and not s[x][y + 1].lock:
                s[x][y + 1].flag = True
                if (x , y + 1) not in temp:  # in one cell we can walk by different paths so check it
                                             # all path which lead to cell will have same length because we walk only by corner with 90 gradusov
                    temp.append((x , y + 1))
        # print(temp)
        current_cells = temp

    x = (len(s) - 1, len(s[0]) - 1)
    if not s[x[0]][x[1]].flag:
        print('Impossible to find path')
        return

    print(x)
    flag = True  # to get path next to diagonal we need to change next way of cell
                 # you can delete it but always will get only maximality top or bottom path
    while x != (0, 0):
        if flag:
            if x[0] > 0 and s[x[0] - 1][x[1]].flag:
                x = (x[0] - 1, x[1])
                print(x)
                continue
            if x[1] > 0 and s[x[0]][x[1] - 1].flag:
                x = (x[0], x[1] - 1)
                print(x)
                continue
        else:
            if x[1] > 0 and s[x[0]][x[1] - 1].flag:
                x = (x[0], x[1] - 1)
                print(x)
                continue
            if x[0] > 0 and s[x[0] - 1][x[1]].flag:
                x = (x[0] - 1, x[1])
                print(x)
                continue
            flag = not flag


# tests ===================
s = [
    [Cell(True), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(True), Cell(), Cell()],
    [Cell(), Cell(True), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(True), Cell(), Cell(True), Cell()]
]
qwe()


s = [
    [Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(True), Cell(), Cell()],
    [Cell(), Cell(True), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(True), Cell(), Cell(True), Cell(True)]
]
qwe()

s = [
    [Cell(), Cell(), Cell(True), Cell(), Cell()],
    [Cell(), Cell(), Cell(True), Cell(), Cell()],
    [Cell(), Cell(), Cell(True), Cell(), Cell()],
    [Cell(), Cell(), Cell(True), Cell(), Cell()],
    [Cell(), Cell(), Cell(True), Cell(), Cell()]
]
qwe()

s = [
    [Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(True), Cell(), Cell()],
    [Cell(), Cell(), Cell(True), Cell(), Cell()],
    [Cell(), Cell(), Cell(True), Cell(), Cell()],
    [Cell(), Cell(), Cell(True), Cell(), Cell()]
]
qwe()

s = [
    [Cell()]
]
qwe()

s = [
    []
]
qwe()

s = []
qwe()

s = [
    [Cell(True), Cell(True)],
    [Cell(True), Cell(True)],
]
qwe()
