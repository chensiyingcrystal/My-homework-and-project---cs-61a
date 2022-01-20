def find_base(n, b):
    i, new = 0, 0
    while n > 0:
        mod = n % b
        new += mod * 10 ** i
        i += 1
        n = n // b
    return new

print(find_base(560, 6))
        

def count_paths(t, total):
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total - label(t)) for b in branches(t)])

