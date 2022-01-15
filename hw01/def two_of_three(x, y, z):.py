def two_of_three(x, y, z):
    return pow(x, 2) + pow(y, 2) + pow(z, 2) - pow(max(x,y,z), 2)

print(two_of_three(1, 2, 3))


