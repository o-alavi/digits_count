def dig1(n):
    return len(str(abs(n)))


def dig2(n):
    import math
    if n == 0:
        return 1
    else:
        return int(math.log10(abs(n))) + 1


def dig3(n):
    val = 1
    while True:
        if n % (10 ** val) == n:
            return val
        else:
            val += 1


print(dig1(123456))
print(dig2(123456))
print(dig3(123456))
