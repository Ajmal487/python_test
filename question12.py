#12. Write a program to rotate a list by K positions.
def rotate_list(lst, k):
    n = len(lst)
    k = k % n  
    return lst[-k:] + lst[:-k]
my_list = [1, 2, 3, 4, 5]
k = 2
rotated_list = rotate_list(my_list, k)
print("Original list:", my_list)
print(f"List rotated by {k} positions:", rotated_list)
