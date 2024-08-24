def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print()

values_list = [2, 'string', False]
values_dict = {'a': 3, 'b': 'world', 'c': 4.5}
print_params(*values_list)
print_params(**values_dict)
print()

values_list_2 = [10, 'ten']
print_params(*values_list_2,42)