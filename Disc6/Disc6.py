"""Q2: Add This Many"""
def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs in s."""
    add_list = []

    for e in s:
        if e == x:
            add_list.append(el)

    s.extend(add_list)
    return s


#tracing
# s = [1, 2, 4, 2, 1]
# add_this_many(1, 5, s)
# print(s)
#     # [1, 2, 4, 2, 1, 5, 5]
# add_this_many(2, 2, s)
# print(s)
#     # [1, 2, 4, 2, 1, 5, 5, 2, 2]


"""Q4: Filter-Iter"""
def filter_iter(iterable, fn):
    """Implement a generator function called filter_iter(iterable, fn) 
        that only yields elements of iterable for which fn returns True."""
    for n in iterable:
        if fn(n):
            yield n


is_even = lambda x: x % 2 == 0
print(list(filter_iter(range(5), is_even))) # a list of the values yielded from the call to filter_iter
    # [0, 2, 4]
all_odd = (2*y-1 for y in range(5))
print(list(filter_iter(all_odd, is_even)))
    # []
naturals = (n for n in range(1, 100))
s = filter_iter(naturals, is_even)
print(next(s))
    # 2
print(next(s))
    # 4