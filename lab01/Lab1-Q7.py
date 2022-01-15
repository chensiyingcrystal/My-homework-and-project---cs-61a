def double_eigths(n):
    while n > 10: 
        a = n % 10
        n = n // 10
        x = n % 10
        if a == x and a == 8:
            return True
    return False

print(double_eigths(280282240))