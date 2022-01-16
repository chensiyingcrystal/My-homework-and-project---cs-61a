HW_SOURCE_FILE = __file__

# """Q1 NUM EIGHTS"""
# def num_eights(pos, i = 0):
#     """Returns the number of times 8 appears as a digit of pos."""
#     def count_times(i):
#         if pos == 0:
#             return i 
#         elif pos % 10 == 8:
#             i += 1
#         return num_eights(pos // 10, i)
#     return count_times(i)

# # print(num_eights(3))
# # print(num_eights(28))
# # print(num_eights(88888888))
# # print(num_eights(2638))
# # print(num_eights(86380))
# # print(num_eights(12345))



# """Q2 Ping-pong"""
# """Return the nth element of the ping-pong sequence."""
# def pingpong(n):  
#     if n <= 8:
#         return n
#     else: 
#         return pingpong(n - 1) + direction(n) 

# def direction(i):
#     if i <= 8:
#         return 1
#     elif num_eights(i - 1) != 0 or (i - 1) % 8 == 0:
#         return direction(i - 1) * (-1)
#     else: 
#         return direction(i - 1)

# solution2 
# def pingpong(n):
#     def flag(x):
#         if x == 1:
#             return 1
#         if num_eights(x) or x % 8 == 0:
#             return -flag(x-1)
#         return flag(x-1)
#     if n == 1:
#         return 1
#     return pingpong(n-1) + flag(n-1)


# print(pingpong(8))
# print(pingpong(10))
# print(pingpong(15))
# print(pingpong(21))
# print(pingpong(22))
# print(pingpong(30))
# print(pingpong(68))
# print(pingpong(69))
# print(pingpong(80))
# print(pingpong(81))
# print(pingpong(82))
# print(pingpong(100))


# """Return the nth element of the ping-pong sequence."""
# def pingpong(n):  
#     if n == 1:
#         return (1,1)
#     pre = pingpong(n-1)
#     if num_eights(n - 1) != 0 or (n - 1) % 8 == 0:
#         return (pre[0] - pre[1], pre[1] * -1)
#     else: 
#         return (pre[0] + pre[1], pre[1])

# print(pingpong(8))
# print(pingpong(15))
# print(pingpong(21))
# print(pingpong(22))
# print(pingpong(30))
# print(pingpong(68))
# print(pingpong(69))
# print(pingpong(80))
# print(pingpong(81))
# print(pingpong(82))
# print(pingpong(100))

# """Q3 Missing digits"""
# def missing_digits(n):
#     """Given a number a that is in sorted, non-decreasing order,
#     return the number of missing digits in n. A missing digit is
#     a number between the first and last digit of a that is not in n."""
#     if n < 10:
#         return 0
#     number_missing = n % 10 - (n // 10) % 10 
#     if number_missing < 2:
#         return missing_digits(n // 10)
#     else:
#         return number_missing - 1 + missing_digits(n // 10)



# print(missing_digits(1248)) # 3, 5, 6, 7
#     # 4
# print(missing_digits(19)) # 2, 3, 4, 5, 6, 7, 8
#     # 7
# print(missing_digits(1122)) # No missing numbers
#     # 0
# print(missing_digits(123456)) # No missing numbers
#     # 0
# print(missing_digits(3558)) # 4, 6, 7
#     # 3
# print(missing_digits(35578)) # 4, 6
#     #2


"""Q4 count coins"""
# def ascending_coin(coin):
#     """Returns the next ascending coin in order.
#     >>> ascending_coin(1)
#     5
#     >>> ascending_coin(5)
#     10
#     >>> ascending_coin(10)
#     25
#     >>> ascending_coin(2) # Other values return None
#     """
#     if coin == 1:
#         return 5
#     elif coin == 5:
#         return 10
#     elif coin == 10:
#         return 25


# def descending_coin(coin):
#     """Returns the next descending coin in order.
#     >>> descending_coin(25)
#     10
#     >>> descending_coin(10)
#     5
#     >>> descending_coin(5)
#     1
#     >>> descending_coin(2) # Other values return None
#     """
#     if coin == 25:
#         return 10
#     elif coin == 10:
#         return 5
#     elif coin == 5:
#         return 1


# def count_coins(change):
#     """Return the number of ways to make change using coins of value of 1, 5, 10, 25."""
#     def count_change_base(change_base, change, count):
#         n = change // change_base
#         left = change % change_base
#         if n == 1:
#             if left == 0:
#                 return count + 1
#             else:
#                 return make_change(left, descending_coin(change_base), count)
#         else:
#             if left == 0:
#                 count += 1
#                 change -= change_base
#                 return count_change_base(change_base, change, make_change(change_base, descending_coin(change_base), count)
#             else: 
#                 count += make_change(left, descending_coin(change_base), count)  
#             return count_change_base(change_base, change - change_base, count)
#     def make_change(change, change_base, count):
#         if change_base == 1:
#             return count + 1
#         else:
#             return make_change(change, descending_coin(change_base), count_change_base(change_base, change, count))
#     return make_change(change, change_base = max_change(change), count = 0)

# def max_change(change):
#     if change >= 25:
#         return 25
#     elif change >= 10:
#         return 10
#     elif change >= 5:
#         return 5
#     else:
#         return 1

# def count_coins(change):
#     def make_change(change, base):
#         if change == 0:
#             return 1
#         elif change < 0:
#             return 0
#         elif base == 0:
#             return 0
#         elif base == 1:
#             return 1
#         else:
#             return make_change(change - base, base) + make_change(change, descending_coin(base))
#     return make_change(change, max_change(change))

# print(count_coins(5))
# # #     # 2
# print("counts are", count_coins(15))
# # #     # 6
# print(count_coins(10))
# # # #     # 4
# print("counts are", count_coins(20))
# # #     # 9
# print(count_coins(100)) # How many ways to make change for a dollar?
# # #     # 242
# print(count_coins(200))
#     # 1463


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    if n == 1:
        return print_move(start, end)
    else:
        move_stack(n - 1, start, empty(start, end))
        move_stack(1, start, end)
        move_stack(n - 1, empty(start, end), end)

def empty(start, end):
    return 6 - start - end 

# move_stack(1, 1, 3)
    # Move the top disk from rod 1 to rod 3
# move_stack(2, 1, 3)
    # Move the top disk from rod 1 to rod 2
    # Move the top disk from rod 1 to rod 3
    # Move the top disk from rod 2 to rod 3
move_stack(3, 1, 3)
    # Move the top disk from rod 1 to rod 3
    # Move the top disk from rod 1 to rod 2
    # Move the top disk from rod 3 to rod 2
    # Move the top disk from rod 1 to rod 3
    # Move the top disk from rod 2 to rod 1
    # Move the top disk from rod 2 to rod 3
    # Move the top disk from rod 1 to rod 3


# from operator import sub, mul


# def make_anonymous_factorial():
#     """Return the value of an expression that computes factorial.

#     >>> make_anonymous_factorial()(5)
#     120
#     >>> from construct_check import check
#     >>> # ban any assignments or recursion
#     >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
#     ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
#     True
#     """
#     return 'YOUR_EXPRESSION_HERE'
