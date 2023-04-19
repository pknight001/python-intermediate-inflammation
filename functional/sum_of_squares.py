def sum_of_squares(sequence):
    from functools import reduce

    #integers = [int(x) for x in sequence if str(x)[0] != '#']
    #squares = [x * x for x in integers]
    integers = (int(x) for x in sequence if str(x)[0] != '#')
    squares = (x * x for x in integers)
    return reduce(lambda a, b: a + b, squares)

print(sum_of_squares([0]))
print(sum_of_squares([1]))
print(sum_of_squares([1, 2, 3]))
print(sum_of_squares([-1]))
print(sum_of_squares([-1, -2, -3]))
print(' ')
print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))
print(sum_of_squares(['1', '2', '#100', '3']))
print('')

seq = range(10000)
print(sum_of_squares(seq))