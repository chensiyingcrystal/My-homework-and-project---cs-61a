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


"""Q2: Height"""
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


print(my_map(lambda x: x*x, [1, 2, 3]))
    # [1, 4, 9]