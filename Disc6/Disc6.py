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