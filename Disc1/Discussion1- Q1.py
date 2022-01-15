def wears_jacket_with_if(temp, raining) :
    if temp < 60 or raining:
        return True
    else:
        return False
    
print(wears_jacket_with_if(100, True))


def wears_jacket(temp, raining):
    return (True if temp < 60 or raining else False)

print(wears_jacket(40, False))