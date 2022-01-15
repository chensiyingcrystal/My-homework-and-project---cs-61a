def largest_factor(n):
    a = n - 1
    while a >= 1:
        if n % a == 0:
            return a
        else:
            a -= 1
print(largest_factor(80))

