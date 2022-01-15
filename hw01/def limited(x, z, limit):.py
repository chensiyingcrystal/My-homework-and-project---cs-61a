def limited(x, z, limit):
    if x != 0:
        return min(z/x, limit)
    else:
        return limit

def invert_short(x, limit):
   return limited(x, 1, limit)

def change_short(x, y, limit):
    return limited(x, abs(y - x), limit)