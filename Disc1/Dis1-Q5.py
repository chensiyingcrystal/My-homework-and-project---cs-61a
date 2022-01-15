def is_prime(n):
    i = 2
    while n % i != 0 and i <= n:
        i += 1
    if i == n:
        return True
    else:
        return False

print(is_prime(38))
    
