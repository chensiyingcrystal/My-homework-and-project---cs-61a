HW_SOURCE_FILE = __file__


"""Q2: Insert Items"""
def insert_items(lst, entry, elem):
    """Inserts elem into lst after each occurence of entry and then returns lst."""
    i = 0
    while i < len(lst):
        if lst[i] == entry:
            lst.insert(i + 1, elem)
            i = i + 2
        else:
            i = i + 1
    return lst


#Wrong solution:
# def insert_items(lst, entry, elem):
#     """Inserts elem into lst after each occurence of entry and then returns lst."""
#     for i in range(0, len(lst)):       # Wrong reason: in the range function, len(lst) will not counted as lst changes
#         if lst[i] == entry:
#             lst.insert(i + 1, elem)    # Can't manipunate the "i"
#     return lst


# test_lst = [1, 5, 8, 5, 2, 3]
# new_lst = insert_items(test_lst, 5, 7)
# print(new_lst)
#     # [1, 5, 7, 8, 5, 7, 2, 3]
# double_lst = [1, 2, 1, 2, 3, 3]
# double_lst = insert_items(double_lst, 3, 4)
# print(double_lst)
#     # [1, 2, 1, 2, 3, 4, 3, 4]
# large_lst = [1, 4, 8]
# large_lst2 = insert_items(large_lst, 4, 4)
# print(large_lst2)
#     # [1, 4, 4, 8]
# large_lst3 = insert_items(large_lst2, 4, 6)
# print(large_lst3)
#     # [1, 4, 6, 4, 6, 8]
# print(large_lst3 is large_lst)
#     # True
# # Ban creating new lists
# from construct_check import check


"""Q4: Count Occurrences"""
def count_occurrences(t, n, x):
    """Return the number of times that x appears in the first n elements of iterator t."""
    i, times = 0, 0
    while i < n:
        if next(t) == x:
            times += 1
        i += 1
    return times


s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
print(count_occurrences(s, 10, 9))
    # 3
s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
print(count_occurrences(s2, 3, 10))
    # 2
s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
print(count_occurrences(s, 1, 3))
    # 1
print(count_occurrences(s, 4, 2))
    # 3
print(next(s))
    # 2
s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
print(count_occurrences(s2, 6, 6))
    # 2

def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row.
    Iterate through the items such that if the same iterator is passed into
    the function twice, it continues in the second call at the point it left
    off in the first.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
