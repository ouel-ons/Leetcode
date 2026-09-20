a = ['a', 'b', 'c']

iterator = iter(a)


while True:
    try:
        x = next(iterator)
        print(x)
    except StopIteration:
        break