from timeit import timeit
# print(timeit('num=5; num *=2', number=1))

from timeit import repeat
# print(repeat('num=5; num *=2', number=1, repeat=50))


def make_list_1():
    result = []
    for value in range(1000):
        result.append(value)
    return result

def make_list_2():
    result = [value for value in range(1000)]
    return result

# we call each function 1000 times
print('make_list_1 takes', timeit(make_list_1, number=1000), 'seconds')
print('make_list_2 takes', timeit(make_list_2, number=1000), 'seconds')
