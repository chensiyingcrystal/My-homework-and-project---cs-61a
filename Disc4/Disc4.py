"""Q1: Count Stair Ways"""
def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time."""
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)

# print(count_stair_ways(4))
    # 5

"""Q2: Count K"""
def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time."""
    if n < 0:
        return 0
    if k == 1:
        return 1
    if n == 0:
        return 1
    else:
        number_of_ways, i = 0, 1
        while i <= k:
            number_of_ways += count_k(n - i, k)
            i += 1
        return number_of_ways
      
# print(count_k(3, 3)) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
#     # 4
# print(count_k(4, 4))
# #     # 8
# print(count_k(10, 3))
# #     # 274
# print(count_k(300, 1)) # Only one step at a time
# #     # 1

"""Q4: Even weighted"""
def even_weighted(s):
    """Write a function that takes a list s and returns a new list 
    that keeps only the even-indexed elements of s and multiplies 
    them by their corresponding index."""
    return [i * s[i] for i in range(0, len(s)) if i % 2 == 0]

# x = [1, 2, 3, 4, 5, 6]
# print(even_weighted(x))
    # [0, 6, 20]


"""Q5: Max Product"""
def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s."""
    if len(s) == 0:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        return max(s[0] * max_product(s[2:]), max_product(s[1:]))


# print(max_product([10,3,1,9,2])) # 10 * 9
#     # 90
# print(max_product([5,10,5,10,5])) # 5 * 5 * 5
#     # 125
# print(max_product([]))
    # 1
