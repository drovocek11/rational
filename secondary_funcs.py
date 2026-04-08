def nod(a, b):
    while a:
        b, a = a, b % a
    return abs(b)

def canonize(numer: int, denom: int) -> tuple:
    n = nod(numer, denom)
    numer /= n
    numer = int(numer)
    denom /= n
    denom = int(denom)
    if denom < 0:
        denom = -denom
        numer = -numer
    return numer, denom
