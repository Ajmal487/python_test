#17. Write a program to sort a dictionary by values.
def sort_dict_by_values(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

my_dict = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = sort_dict_by_values(my_dict)
print("Original dictionary:", my_dict)
print("Dictionary sorted by values:", sorted_dict)