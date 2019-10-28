# 16.7. Напишите метод, находящий максимальное из Двух .чисел 'без исiiолЬзования
# if-eise ил и любых других оnерёJТQров сравненйя.

def qwe(a, b):
    bin_str = format(a - b, 'b')
    try:
        int(bin_str[0])
        # a - b > 0
        sign = 1
    except Exception:
        # first leter is sign "-"
        sign = 0

    flip_sign = sign ^ 1
    return a  * sign + b * flip_sign

a = 12124
b = 1
print(qwe(a, b))


a = 12124
b = -10101
print(qwe(a, b))

a = 1
b = -10101
print(qwe(a, b))
a = 1
b = 65634
print(qwe(a, b))