# Т1 и Т2 два очень больших бинарных дерева, причем Т1 значительно больше
# Т2. Создайте алгоритм, проверяющий, является ли Т2 поддеревом Тl.
# -
# Дерево Т2 считается поддеревом Tl, если существует такой узел п в Тl, что
# поддерево, «растущее» из п, идентично дереву Т2. ( И наче говоря, если вы­
# резать дерево в узле п, оно будет идентично Т2. )
# Подсказки: 4, 1 1 , 18, 3 1 , 37
#
#
# странные типы говорят, что дерево ну очень большое и при этом в подсказках говорят, что задачу можно решать рекурсивно,
# ахренеть интервьюверы, вы уж определитесь большое или рекурсия все же работает

# я так понял что деревья сравнимаются по значениям в узлах а не по ссылкам

# можно обойти деревья, сдампать их ввиде строки, и сравнить строки,
# проблема будет в том что пустые листья надо заполнять какими нибудь значениями чтоб потом можно было отличить что в
# одном дереве мы пропустили 5 пустых литьев а во втором 15, и при этом так же надо будет выранивать деревья потому как смотри пример
#     1       1
#    1 1     1 1
#   1           1
# в данном случае дамп будет одинаковым, но деревья разные
#
# поэтому наверное лучше делать все рекурсивно

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.inserted = False

    def __str__(self):
        return '\nvalue: ' + str(self.value) + ' \n\tnodes: ' + ' '.join(map(lambda x: str(x.value) if x else str(None), [self.left, self.right]))

    def __repr__(self):
        return self.__str__()


#       5                         #       5
#    3       7                    #    3
#  2  4    6   8        vs        #  2  4
# 1              9                # 1

q1 = Node(1)
q2 = Node(2)
q3 = Node(3)
q4 = Node(4)
q5 = Node(5)
q6 = Node(6)
q7 = Node(7)
q8 = Node(8)
q9 = Node(9)

q5.left = q3
q5.right = q7

q3.left = q2
q3.right = q4

q2.left = q1

q7.left = q6
q7.right = q8

q8.right = q9

root_big = q5


z1 = Node(10)
z2 = Node(2)
z3 = Node(3)
z4 = Node(4)
z5 = Node(5)
z6 = Node(6)
z7 = Node(7)
z8 = Node(8)
z9 = Node(9)

z5.left = z3

z3.left = z2
z3.right = z4

z2.left = z1

root_small = z3

class NotEqual(Exception):
    def __init__(self, msg):
        self.msg = msg

def search_equal_nodes_values_and_run_compare(rb, rs):
    if rb.value == rs.value:
        yield [rb, rs]
    if rb.left:
        yield from search_equal_nodes_values_and_run_compare(rb.left, rs)
    if rb.right:
        yield from search_equal_nodes_values_and_run_compare(rb.right, rs)


def comp(l:Node, r:Node):
    if l.value != r.value:
        raise NotEqual(1)

    if l.left and not r.left:
        raise NotEqual(2)
    if l.right and not r.right:
        raise NotEqual(3)

    if not l.left and r.left:
        raise NotEqual(4)
    if not l.right and r.right:
        raise NotEqual(5)

    if l.left and r.left:
        comp(l.left, r.left)

    if l.right and r.right:
        comp(l.right, r.right)

    return True

for ln,rn in search_equal_nodes_values_and_run_compare(root_big, root_small):
    try:
        comp(ln, rn)
    except NotEqual as e:
        print('Exc:', e)
    else:
        print('Equal')
