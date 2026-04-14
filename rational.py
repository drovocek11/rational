from secondary_funcs import canonize

class Rational:
    pass

def create(numer:int, denom:int):
    if denom == 0:
        return None
    res = Rational()
    res.numer, res.denom = canonize(numer, denom)
    return res

def to_str(r:Rational):
    if r is None:
        return None
    first_part = str(int(r.numer))
    second_part = str(int(r.denom))
    if first_part == "0" or second_part == "1":
        return first_part
    string = first_part + '/' + second_part
    return string

def to_float(r:Rational):
    if r is None:
        return
    res = round(r.numer / r.denom, 3)
    return res

def to_int(r:Rational):
    if r is None:
        return None
    res = create(r.numer, r.denom)
    if res.numer < 0:
        res.numer = -res.numer
        return -(res.numer // res.denom)
    return res.numer // res.denom

def add(a:Rational, b:Rational):
    if a is None or b is None:
        return None
    res = create(a.numer * b.denom + a.denom * b.numer, a.denom * b.denom)
    return res

def sub(a:Rational, b:Rational):
    if a is None or b is None:
        return None
    res = create(a.numer * b.denom + a.denom * b.numer, a.denom * b.denom)
    return res

def mul(a:Rational, b:Rational):
    if a is None or b is None:
        return None
    res = create(a.numer * b.numer, a.denom * b.denom)
    return res

def div(a:Rational, b:Rational):
    if a is None or b is None:
        return None
    res = create(a.numer * b.denom, a.denom * b.numer)
    return res

def power(r:Rational, power:int):
    if r is None:
        return None
    res = create(r.numer ** abs(power), r.denom ** abs(power))
    if power < 0:
        res.numer, res.denom = res.denom, res.numer
    return res

def compare(a:Rational, b:Rational):
    if a is None or b is None:
        return None
    numer1 = a.numer * b.denom
    numer2 = b.numer * a.denom
    if numer1 > numer2:
        return 1
    elif numer1 < numer2:
        return -1
    return 0

