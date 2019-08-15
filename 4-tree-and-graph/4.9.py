# Бинарное дерево поиска было создано обходом массива слева направо и встав­
# кой каждого элемента. Для заданного бинарного дерева поиска с разными
# элементами выведите все возможные массивы, которые могли привести
# к созданию этого дерева.
# Пример:
# Ввод:  #       2
         #   1       3
# Вывод: { 2 , 1 , з } , { 2 , з , 1 }
# Подсказки: 39, 48, 66, 82

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


#       5
#    3       7
#  2  4    6   8
# 1              9

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

q8.left = q9


def get_suspected_nodes(r: Node):
    if r.inserted and r.left and not r.left.inserted:
        yield r.left
    if r.inserted and r.right and not r.right.inserted:
        yield r.right

    if r.left:
        yield from get_suspected_nodes(r.left)
    if r.right:
        yield from get_suspected_nodes(r.right)


def main():
    sns = list(get_suspected_nodes(root))
    if sns:
        for sn in sns:
            intermediate_result.append(sn)
            sn.inserted = True
            main()
            sn.inserted = False
            intermediate_result.pop(-1)
    else:
        print(' '.join((str(x.value) for x in intermediate_result)))
        answer.append(' '.join((str(x.value) for x in intermediate_result)))


#=================tests============
root = q1
intermediate_result = [root]
root.inserted = True
answer = []
main()
assert answer == ['1']
root.inserted = False
print('=' * 100)

root = q2
intermediate_result = [root]
root.inserted = True
answer = []
main()
assert answer == ['2 1']
root.inserted = False
print('=' * 100)

root = q3
intermediate_result = [root]
root.inserted = True
answer = []
main()
assert answer == ['3 2 4 1', '3 2 1 4', '3 4 2 1']
root.inserted = False
print('=' * 100)

root = q5
intermediate_result = [root]
root.inserted = True
answer = []
main()
assert answer != []  # too many elements
root.inserted = False
print('=' * 100)

