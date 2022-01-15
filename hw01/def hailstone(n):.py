i = 1

def hailstone(n,i):
    while n > 1:
        print(n)
        i += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
    print(n)
    return i + 1

a = hailstone(10,i)
print(a)
