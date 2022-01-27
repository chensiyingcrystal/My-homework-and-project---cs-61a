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


#Tracing
# is_even = lambda x: x % 2 == 0
# print(list(filter_iter(range(5), is_even))) # a list of the values yielded from the call to filter_iter
#     # [0, 2, 4]
# all_odd = (2*y-1 for y in range(5))
# print(list(filter_iter(all_odd, is_even)))
#     # []
# naturals = (n for n in range(1, 100))
# s = filter_iter(naturals, is_even)
# print(next(s))
#     # 2
# print(next(s))
#     # 4


"""Q5: Merge"""
def merge(a, b):
    """Write a generator function merge that takes in two infinite generators a and b 
that are in increasing order without duplicates and returns a generator 
that has all the elements of both generators, in increasing order, without duplicates."""
    a_element = next(a)
    b_element = next(b)
    while True:
        if a_element == b_element:
            yield a_element
            a_element = next(a)
            b_element = next(b)
        elif a_element < b_element:
            yield a_element
            a_element = next(a)
        else:
            yield b_element
            b_element = next(b)


# #Tracing
# def sequence(start, step):
#     while True:
#         yield start
#         start += step
# a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
# b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
# result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
# print([next(result) for _ in range(10)])
#     # [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]


"""Q6: Primes Generator"""
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

def primes_gen(n):
    """Generates primes in decreasing order."""
    if n <= 1:
        return
    if is_prime(n):
        yield n
    yield from primes_gen(n - 1)


# pg = primes_gen(7)
# print(list(pg))
#     # [7, 5, 3, 2]


def primes_gen_ascend(n):
    """Generates primes in increasing order."""
    if n > 1:
        yield from primes_gen_ascend(n - 1)
        if is_prime(n):
            yield n
    

dg = primes_gen_ascend(7)
print(list(dg))
    # [7, 5, 3, 2]