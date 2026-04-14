import pytest
from rational import create, to_str, to_float, add, sub, mul, div, power, to_int, compare
from secondary_funcs import nod, canonize

@pytest.mark.parametrize("numer, denom, expected", [
    (1, 1, 1),
    (1, 2, 1),
    (4, 3, 1),
    (1, -1, 1),
    (-1, 1, 1),
    (-1, -1, 1),
    (-8, -6, 2),
    (-8, 6, 2),
    (8, -6, 2),
    (0, 6, 6),
    (0, -6, 6),
    (13*5, 12*5, 5),
    (13*5*3*2*4, 12*5*3*2*4, 5*3*2*4),
    (14*5*3*2*4, 12*5*3*2*4, 2*5*3*2*4),
])
def test_nod(numer, denom, expected):
    assert nod(numer, denom) == expected

@pytest.mark.parametrize("numer, denom, expected", [
    (1, 1, (1, 1)),
    (1, 2, (1, 2)),
    (4, 3, (4, 3)),
    (1, -1, (-1, 1)),
    (-1, 1, (-1, 1)),
    (-1, -1, (1, 1)),
    (-8, -6, (4, 3)),
    (-8, 6, (-4, 3)),
    (8, -6, (-4, 3)),
    (0, 6, (0, 1)),
    (0, -6, (0, 1)),
])
def test_canonical_form(numer, denom, expected):
    assert canonize(numer, denom) == expected

@pytest.mark.parametrize("numer, denom, expected",[
    (1, 1, (1, 1)),
    (1, 2, (1, 2)),
    (-1, 2, (-1, 2)),
    (1, -2, (-1, 2)),
    (2, 4, (1, 2)),
    (-2, 4, (-1, 2)),
    (2, -4, (-1, 2)),
    (4, 3, (4, 3)),
    (-4, 3, (-4, 3)),
    (4, -3, (-4, 3)),
    (0, 1, (0, 1)),
    (0, 3, (0, 1)),
    (0, -3, (0, 1)),
    (2, 0, None),
    (-2, 0, None),
    (0, 0, None),
    (0, 101, (0, 1))
])
def test_create(numer, denom, expected):
    r = create(numer, denom)
    assert (r.numer, r.denom) if r else r == expected

@pytest.mark.parametrize("numer, denom, expected", [
    (2, 3, "2/3"),
    (-2, 3, "-2/3"),
    (2, -3, "-2/3"),
    (1, 1, "1"),
    (-1, 1, "-1"),
    (1, -1, "-1"),
    (6, 8, "3/4"),
    (-6, 8, "-3/4"),
    (6, -8, "-3/4"),
    (0, 8, "0"),
    (-0, 8, "0"),
    (0, -8, "0"),
    (8, 0, None),
    (-8, 0, None),
    (8, -0, None)
])
def test_to_str(numer, denom, expected):
    r = to_str(create(numer, denom))
    assert r == expected

@pytest.mark.parametrize("numer, denom, expected", [
    (-3, 0, None),
    (3, 0, None),
    (0, -2, 0.0),
    (-0, 2, 0.0),
    (0, 2, 0.0),
    (7, -2, -3.5),
    (-7, 2, -3.5),
    (7, 2, 3.5),
    (2, 4, 0.5),
    (2, -3, -0.667),
    (-2, 3, -0.667),
    (2, 3, 0.667),
    (1, -1, -1.0),
    (-1, 1, -1.0),
    (1, 1, 1.0),
])
def test_to_float(numer, denom, expected):
    r = to_float(create(numer, denom))
    assert r == expected

@pytest.mark.parametrize("numer, denom, expected", [
    (1, 2, 0),
    (-1, 2, 0),
    (1, -2, 0),
    (2, 3, 0),
    (-2, 3, 0),
    (2, -3, 0),
    (3, 3, 1),
    (-3, 3, -1),
    (3, -3, -1),
    (0, 2, 0),
    (0, -2, 0),
    (2, 0, None),
    (0, 0, None)
])
def test_to_int(numer, denom, expected):
    r = to_int(create(numer, denom))
    assert r == expected

@pytest.mark.parametrize("first, second, expected", [
    ((2,3), (2,3), (4,3)),
    ((2,-3), (2,3), (0,1)),
    ((2,3), (2,-3), (0,1)),
    ((5,3), (3,3), (8,3)),
    ((5,3), (-2,3), (1,1)),
    ((-5,3), (2,3), (-1,1)),
    ((2,3), (6,5), (28,15)),
    ((0,3), (2,3), (2,3)),
    ((2,3), (0,3), (2,3)),
    ((0,3), (0,3), (0,1)),
    ((2,0), (2,3), None),
    ((2,3), (2,0), None)
])
def test_add(first, second, expected):
    r = add(create(first[0], first[1]), create(second[0], second[1]))
    assert (r.numer, r.denom) if r else r == expected

@pytest.mark.parametrize("first, second, expected", [
    ((2,3), (2,3), (0,1)),
    ((2,-3), (2,3), (-4,3)),
    ((2,3), (2,-3), (4,3)),
    ((5,3), (3,3), (2,3)),
    ((5,3), (-2,3), (7,3)),
    ((-5,3), (2,3), (-7,3)),
    ((2,3), (6,5), (-8,15)),
    ((0,3), (2,3), (-2,3)),
    ((2,3), (0,3), (2,3)),
    ((0,3), (0,3), (0,1)),
    ((2,0), (2,3), None),
    ((2,3), (2,0), None)
])
def test_sub(first, second, expected):
    r = sub(create(first[0], first[1]), create(second[0], second[1]))
    assert (r.numer, r.denom) if r else r == expected

@pytest.mark.parametrize("first, second, expected", [
    ((2,3), (2,3), (4,9)),
    ((2,-3), (2,3), (-4,9)),
    ((2,3), (2,-3), (-4,9)),
    ((5,3), (3,3), (5,3)),
    ((5,3), (-2,3), (-10,9)),
    ((-5,3), (2,3), (-10,9)),
    ((2,3), (6,5), (4,5)),
    ((0,3), (2,3), (0,1)),
    ((2,3), (0,3), (0,1)),
    ((0,3), (0,3), (0,1)),
    ((2,0), (2,3), None),
    ((2,3), (2,0), None)
])
def test_mul(first, second, expected):
    r = mul(create(first[0], first[1]), create(second[0], second[1]))
    assert (r.numer, r.denom) if r else r == expected

def test_not_a_number_ops():
    assert create(4, 0) == None
    assert to_str(create(4, 0)) == None
    assert to_float(create(4, 0)) == None
    assert to_int(create(4, 0)) == None
    assert add(create(4, 0), create(1, 2)) == None
    assert add(create(4, 2), create(4, 0)) == None
    assert add(create(2, 0), create(1, 0)) == None
    assert sub(create(4, 0), create(1, 2)) == None
    assert sub(create(4, 2), create(4, 0)) == None
    assert sub(create(2, 0), create(1, 0)) == None
    assert mul(create(4, 0), create(1, 2)) == None
    assert mul(create(4, 2), create(4, 0)) == None
    assert mul(create(2, 0), create(1, 0)) == None
    assert div(create(4, 0), create(1, 2)) == None
    assert div(create(4, 2), create(4, 0)) == None
    assert div(create(2, 0), create(1, 0)) == None
    assert power(create(4, 0), 0) == None
    assert power(create(4, 0), -2) == None
    assert power(create(4, 0), 2) == None
    assert compare(create(4, 0), create(1, 2)) == None
    assert compare(create(4, 2), create(1, 0)) == None
    assert compare(create(4, 0), create(1, 0)) == None

@pytest.mark.parametrize("first, second, expected", [
    ((1,2), (1,2), (1,1)),
    ((1,-2), (1,2), (-1,1)),
    ((1,2), (1,-2), (-1,1)),
    ((4,7), (3,9), (12,7)),
    ((-4,7), (3,9), (-12,7)),
    ((4,7), (-3,9), (-12,7)),
    ((4,-7), (3,-9), (12,7)),
    ((0,7), (3,9), (0,1)),
    ((4,7), (0,9), None),
    ((4,7), (3,0), None),
    ((4,0), (3,9), None)
])
def test_div(first, second, expected):
    r = div(create(first[0], first[1]), create(second[0], second[1]))
    assert (r.numer, r.denom) if r else r == expected

@pytest.mark.parametrize("rational, power_check, expected", [
    ((1, 1), 2, (1, 1)),
    ((1, -1), 2, (1, 1)),
    ((1, -1), -2, (1, 1)),
    ((1, 2), 2, (1, 4)),
    ((1, 2), -2, (4, 1)),
    ((1, -2), -2, (4, 1)),
    ((1, 2), -3, (8, 1)),
    ((1, -2), -3, (-8, 1)),
    ((44, 21), 0, (1, 1)),
    ((44, -21), 0, (1, 1)),
    ((0, 21), 3, None),
    ((0, -21), 3, None),
    ((0, 21), -3, None),
    ((33, 0), 3, None),
    ((-21, 0), -2, None),
    ((-21, 0), 0, None),
    ((0, 22), 0, None),
    ((0, 8), 3, (0, 1))
])
def test_power(rational, power_check, expected):
    r = power(create(rational[0], rational[1]), power_check)
    assert (r.numer, r.denom) if r else r == expected

@pytest.mark.parametrize("first, second, expected", [
    ((1,2), (1,2), 0),
    ((-1,2), (1,2), -1),
    ((1,2), (-1,2), 1),
    ((2,4), (1,2), 0),
    ((3,2), (5,2), -1),
    ((-2,4), (-1,2), 0),
    ((0,2), (1,2), -1),
    ((1,2), (0,2), 1),
    ((0,2), (0,2), 0),
    ((1,0), (1,2), None),
    ((1,2), (1,0), None),
    ((1,0), (1,0), None),
])
def test_compare(first, second, expected):
    assert compare(create(first[0], first[1]), create(second[0], second[1])) == expected

pytest.main(["test_rational.py", ""])