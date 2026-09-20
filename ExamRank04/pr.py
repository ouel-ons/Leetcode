
a = [0, 0, 3, 1, 1]
# print(any(a))
# print(all(a))

a = [(1,1), (0,1)]
# for row, cow in a:
#     print(row, cow)



s = [['.', '*', '.'], ['*', '*', '*'], ['.', '*', '.']]
for row in s:
    print(row)
print((q := [''.join(_) for _ in s]))
print("q --> ", q)
print(w := (_ for _ in q))
print("w --> ", w)
print("-------")
for i in q:
    print(i)
