def nod(a, b):
    while a:
        b, a = a, b % a
    return abs(b)

def canonize(numer: int, denom: int) -> tuple:
    n = nod(numer, denom)
    numer /= n
    denom /= n
    if denom < 0:
        denom = -denom
        numer = -numer
    return numer, denom

class Rational:
    pass

def create(numer:int, denom:int):
    if denom == 0:
        return None
    res = Rational()
    res.numer, res.denom = canonize(numer, denom)
    return res

def to_str(r:Rational):
    if not r:
        return "None"
    first_part = str(int(r.numer))
    second_part = str(int(r.denom))
    if first_part == "0" or second_part == "1":
        return first_part
    string = first_part + '/' + second_part
    return string

def to_float(r:Rational):
    if not r:
        return
    res = round(r.numer / r.denom, 3)
    return res

def to_int(r:Rational):
    if not r:
        return None
    if r.numer < 0:
        r.numer = -r.numer
        return -(r.numer // r.denom)
    return r.numer // r.denom

def add(a:Rational, b:Rational):
    if not a or not b:
        return None
    res = Rational()
    res.denom = a.denom * b.denom
    res.numer = a.numer * b.denom + a.denom * b.numer
    res.numer, res.denom = canonize(res.numer, res.denom)
    return res

def sub(a:Rational, b:Rational):
    if not a or not b:
        return None
    res = Rational()
    res.denom = a.denom * b.denom
    res.numer = a.numer * b.denom - a.denom * b.numer
    res.numer, res.denom = canonize(res.numer, res.denom)
    return res

def mul(a:Rational, b:Rational):
    if not a or not b:
        return None
    res = Rational()
    res.denom = a.denom * b.denom
    res.numer = a.numer * b.numer
    res.numer, res.denom = canonize(res.numer, res.denom)
    return res

def div(a:Rational, b:Rational):
    if not a or not b or b.numer == 0:
        return None
    b.numer, b.denom = canonize(b.denom, b.numer)
    res = mul(a, b)
    return res

def power(r:Rational, power:int):
    if not r or r.numer == 0:
        return None
    if power < 0:
        r.numer, r.denom = r.denom ** -power, r.numer ** -power
    else:
        r.numer **= power
        r.denom **= power
    r.numer, r.denom = canonize(r.numer, r.denom)
    return r

# def power_papa(r:Rational, power:int):
#     if not r:
#         return None
#     r.numer **= abs(power)
#     r.denom **= abs(power)
#     if power < 0:
#         r.numer, r.denom = r.denom, r.numer
#     r.numer, r.denom = canonize(r.numer, r.denom)
#     return r


def compare(a:Rational, b:Rational):
    if not a or not b:
        return None
    a.numer *= b.denom
    b.numer *= a.denom
    if a.numer > b.numer:
        return 1
    elif a.numer < b.numer:
        return -1
    else:
        return 0

