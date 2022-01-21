"""Q2: Height"""
#Tree Data Abstraction
def tree(root_label, branches=[]):
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [root_label] + list(branches)


def label(tree):
        return tree[0]


def branches(tree):
        return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True    


def is_leaf(tree):
    return not branches(tree)


def height(t):
    """Return the height of a tree."""
    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(b) for b in branches(t)])


# t = tree(3, [tree(5, [tree(1)]), tree(2)])
# print(height(t))
#     # 2
# t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
# print(height(t))
#     # 3


"""Q3: Maximum Path Sum"""
def max_path_sum(t):
    """Return the maximum path sum of the tree.

    """
    if is_leaf(t):
        return label(t)
    else:
        return label(t) + max([max_path_sum(b) for b in branches(t)])


# t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
# print(max_path_sum(t))
#     # 11


"""Q4: Find Path"""
def find_path(t, x):
    """Write a function that takes in a tree and a value x and returns a list containing 
    the nodes along the path required to get from the root of the tree to a node containing x.
    If x is not present in the tree, return None. Assume that the entries of the tree are unique."""
    if label(t) == x:  #do not need to test the leaf, because it's also a unique branch
        return [label(t)]
    for b in branches(t):   #list comprehension has some restrictions, avoid using that when needed
        path = find_path(b, x)  #avoiding excuting twice
        if path:
            return [label(t)] + path  #A list concatenating a list should never be wrong
    # return None    #this is a redundant line


# t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
# print(find_path(t, 5))
#     # [2, 7, 6, 5]
# print(find_path(t, 10))  # returns None
#     # None


"""Q5: Map, Filter, Reduce"""
def my_map(fn, seq):
    """Applies fn onto each element in seq and returns a list."""
    return [fn(n) for n in seq]


# print(my_map(lambda x: x*x, [1, 2, 3]))
#     # [1, 4, 9]


def my_filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred."""
    return [n for n in seq if pred(n)]
    

# print(my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))  # new list has only even-valued elements
#     # [2, 4]


def my_reduce(combiner, seq):
    """Combines elements in seq using combiner.
    seq will have at least one element."""
    if len(seq) == 1:
        return seq[0]
    elif len(seq) == 0:
        return 0
    else:
        new_seq = [combiner(seq[0], seq[1])] + seq[2:]
        return my_reduce(combiner, new_seq)
            

# print(my_reduce(lambda x, y: x + y, [1, 2, 3, 4]))  # 1 + 2 + 3 + 4
#     # 10
# print(my_reduce(lambda x, y: x * y, [1, 2, 3, 4]))  # 1 * 2 * 3 * 4
#     # 24
# print(my_reduce(lambda x, y: x * y, [4]))
#     # 4
# print(my_reduce(lambda x, y: x + 2 * y, [1, 2, 3])) # (1 + 2 * 2) + 2 * 3
#     # 11


"""Q6: Count palindromes"""
def count_palindromes(L):
    """The number of palindromic words in the sequence of strings
    L (ignoring case)."""
    list_of_L = list(L)
    lower_case_list = my_map(lambda x: x.lower(), list_of_L)
    test_converse = lambda seq: my_filter(lambda x: seq[x] == seq[len(seq) - x - 1], range(0, len(seq)))
    test_result = my_map(test_converse, lower_case_list)
    times = my_filter(lambda i: len(test_result[i]) == len(lower_case_list[i]), range(0, len(lower_case_list)))
    return len(times)


# print(count_palindromes(("Acme", "Madam", "Pivot", "Pip")))
#     # 2


"""Q7: Perfectly Balanced"""
def sum_tree(t):
    """Add all elements in a tree."""
    return label(t) + sum([sum_tree(b) for b in branches(t)])

    
# t = tree(4, [tree(2, [tree(3)]), tree(6)])
# print(sum_tree(t))
#     # 15


def balanced(t):
    """
    Checks if each branch has same sum of all elements and
    if each branch is balanced.
    """
    return not False in [balanced(b) for b in branches(t)] and all(n == [sum_tree(b) for b in branches(t)][0] for n in [sum_tree(b) for b in branches(t)])
           
     
# t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
# print(balanced(t))
#     # True
# t = tree(1, [t, tree(1)])
# print(balanced(t))
#     # False
# t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
# print(balanced(t))
#     # False


"""Q8: Hailstone Tree"""
def hailstone_tree(n, h):
    """Generates a tree of hailstone numbers that will reach N, with height H."""
    if h == 0:
        return tree(n)
    if (n - 1) % 3 == 0 and ((n - 1) // 3) % 2 == 1 and (n - 1) // 3 > 1:
        return tree(n, [hailstone_tree(n * 2, h - 1), hailstone_tree((n - 1) // 3, h - 1)])
    else:
        return tree(n, [hailstone_tree(n * 2, h - 1)])


def print_tree(t):
    def helper(i, t):
        print("    " * i + str(label(t)))
        for b in branches(t):
            helper(i + 1, b)
    helper(0, t)


# print_tree(hailstone_tree(1, 0))
#     # 1
# print_tree(hailstone_tree(1, 4))
#     # 1
#     #     2
#     #         4
#     #             8
#     #                 16
print_tree(hailstone_tree(8, 3))
    # 8
    #     16
    #         32
    #             64
    #         5
    #             10
