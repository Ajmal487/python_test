#11. Write a program to find the intersection of two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = [x for x in list1 if x in list2]
print("Intersection of the two lists:", intersection)