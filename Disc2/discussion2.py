# Q1: make make_keeper

# def make_keeper(n):
#     def cond_evaluate(cond):
#         i = 1
#         while i <= n:
#             if cond(i):
#                 print(i)
#             i += 1
#     return cond_evaluate

# def is_even(x):
#     return x % 2 == 0

# make_keeper(5)(is_even)

# Q3: curry2 Lambda
# curry2 = lambda h : lambda x : lambda y : h(x, y)
# make_adder = curry2(lambda x, y: x + y)
# add_three = make_adder(3)
# add_four = make_adder(4)
# five = add_three(2)
# print(five)

# """Q4: make keeper redux"""
# def make_keeper_redux(n):
#     def make_keeper(cond):
#         i = 1
#         while i <= n:
#             if cond(i):
#                 print(i)
#             i += 1
#         return make_keeper_redux(n)
#     return make_keeper

# def multiple_of_4(x):
#     return x % 4 == 0
# def ends_with_1(x):
#     return x % 10 == 1
# k = make_keeper_redux(11)(multiple_of_4)
# k = k(ends_with_1)

# """Q5: print N"""
# def print_n(n):
#     def inner_print(x):
#         if n <= 0:
#             print("done")
#         else:
#             print(x)
#         return print_n(n - 1)
#     return inner_print

# # f = print_n(2)
# # f = f("hi")
# # f = f("hello")
# # f = f("bye")
# g = print_n(1)
# g("first")("second")("third")

# """Q8: Match Maker"""
# def match_k(k):
#     def check_match(x):
#         while x // (10 ** k):
#             last = x % 10
#             apart_last = (x // (10 ** k)) % 10
#             if last != apart_last:
#                 return False
#             x = x // 10
#         return True
#     return check_match

# print(match_k(2)(1010))
# print(match_k(2)(2010))
# print(match_k(1)(2111111111111111))
# print(match_k(3)(123123))
# print(match_k(2)(123123))


# """Q9 Three Memory"""
# def three_memory(n):
#     def f(x, y, z):
#         def g(i):
#             if i == x:
#                 print("Found")
#             else:
#                 print("Not found")
#             return f(y, z, i)
#         return g
#     return f(None, None, n)

# f = three_memory('first')
# f = f('first')
# f = f('second')
# f = f('third')
# f = f('second')
# f = f('second')


# # """Q10 Natural Chain"""

# def chain_function():
#     def g(x, y, break_point):
#         def h(n):
#             if n - y == 1 or x == 0 or y == 0:
#                 return g(y, n, break_point)
#             else:
#                 return print(y + 1, break_point + 1) or g(y, n, break_point + 1)
#         return h
#     return g(0, 0, break_point = 0)

# # tester = chain_function()
# # x = tester(1)(2)(4)(5)(2)(8)(3)(4)(5)(9)(10)

# # y = tester(4)(5)(8)
# # y = y(2)(3)(10)