#Для двух отрезков, заданных начальной и конечной точками, вычислите
#точку пересечения (если она существует).

import math

def f(x, y):
    # y = ax + b
    #x[0][1] = a * x[0][0] + b
    #x[1][1] = a * x[1][0] + b
    # то что здесь может быть зеро девижион уж не будем проверять
    slope_x = (x[0][1] - x[1][1])/(x[0][0] - x[1][0])
    shift_x = x[0][1] - slope_x * x[0][0]

    slope_y = (y[0][1] - y[1][1])/(y[0][0] - y[1][0])
    shift_y = y[0][1] - slope_y * y[0][0]

    print(slope_x, shift_x, slope_y, shift_y)

    if slope_x != slope_y:
        # slope_x * cros_x + shift_x = slope_y * cros_x + shift_y
        cros_x = (shift_y - shift_x)/(slope_x - slope_y)
        cros_y = slope_y * cros_x + shift_y

        print(cros_x, cros_y)

        # чтоб проверить что точка лежит внутри отрезка нужно проверить, что
        # расстояние до точки пересечения от обоих концов отрезка должно быть меньше длинны отрезка
        # и проверять для обоих отрезков

        x_length = math.sqrt((x[0][0] - x[1][0]) ** 2 + (x[0][1] - x[1][1]) ** 2)
        y_length = math.sqrt((y[0][0] - y[1][0]) ** 2 + (y[0][1] - y[1][1]) ** 2)

        for xx in x:
            if math.sqrt((xx[0] - cros_x) ** 2 + (xx[1] - cros_y) ** 2) > x_length:
                return False

        for yy in y:
            if math.sqrt((yy[0] - cros_x) ** 2 + (yy[1] - cros_y) ** 2) > y_length:
                return False
        return cros_x, cros_y
    else:
        # прямые паралельны
        if shift_y != shift_x:
            return False
        # прямая одна, проверить что отрезки пересекаются
        if y[0][0] <= x[0][0] <= y[1][0] or y[0][0] <= x[1][0] <= y[1][0]:
            return True
        else:
            return False




# одна прямая отрезки не пересекаются
x = [(0, 0), (2, 2)]
y = [(3, 3), (5, 5)]

assert False == f(x, y)

# одна прямая отрезки пересекаются
x = [(0, 0), (2, 2)]
y = [(1, 1), (5, 5)]

assert True == f(x, y)

# прямые паралельны
x = [(0, 0), (2, 2)]
y = [(0, 1), (2, 3)]

assert False == f(x, y)

# прямые пересекаются отрезки тоже
x = [(0, 0), (2, 2)]
y = [(1, 0), (-2, 1)]

assert (0.25, 0.25) == f(x, y)


# прямые пересекаются отрезки нет
x = [(2, 2), (3, 3)]
y = [(1, 0), (-2, 1)]

assert False == f(x, y)


