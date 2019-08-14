#Создайте алгоритм и напишите код поиска первого общего предка двух узлов
#бинарного дерева. Постарайтесь избежать хранения дополнительных узлов
#в структуре данных. Примечание: бинарное дерево не обязательно является
#бинарным деревом поиска.

#Подсказки: 10, 1 6, 28, 36, 46, 70, 80, 96

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return '\nvalue: ' + str(self.value) + ' \n\tnodes: ' + ' '.join(map(lambda x: str(x.value) if x else str(None), [self.left, self.right]))


#       1
#    2       3
#  4  5    6   7
#10          8  9

q1 = Node(1)
q2 = Node(2)
q3 = Node(3)
q4 = Node(4)
q5 = Node(5)
q6 = Node(6)
q7 = Node(7)
q8 = Node(8)
q9 = Node(9)
q10 = Node(10)

q1.left = q2
q1.right = q3

q2.left = q4
q2.right = q5

q3.left = q6
q3.right = q7

q4.left = q10

q7.left = q8
q7.right = q9

root = q1
first_candidate = None
second_candidate = None
result = None

def qwe(r: Node):
    global result, first_candidate, second_candidate
    result_left = result_right = 0

    if r is first_candidate:
        result_left = 1
    if r is second_candidate:
        result_right = 1

    if r.left:
        result_left += qwe(r.left)
    if r.right:
        result_right += qwe(r.right)

    if result_left + result_right == 2:
        result = r
        print('Common root: ', r)
        return 0

    return result_left + result_right


# tests
first_candidate = q1
second_candidate = q1
qwe(root)
assert result == q1 # если вслучае совпадения елементов нужно выводить не сам елемент, а его предка то как быть в конем, я бы лучше выводил сам елемент

first_candidate = q10
second_candidate = q10
qwe(root)
assert result == q10

first_candidate = q5
second_candidate = q10
qwe(root)
assert result == q2

first_candidate = q9
second_candidate = q10
qwe(root)
assert result == q1

first_candidate = q1
second_candidate = q10
qwe(root)
assert result == q1

first_candidate = q4
second_candidate = q10
qwe(root)
assert result == q4

