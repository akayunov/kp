def qwe(s):
    if len(s) <= 1:
        yield s
        return

    symbol = s[0]
    string = s[1:]
    for perm in qwe(string):
        for i in range(len(perm) + 1):
            yield perm[:i] + symbol + perm[i:]

count = 0
for permutation in qwe('abcd'):
    count += 1
    print(permutation)
print(count)

