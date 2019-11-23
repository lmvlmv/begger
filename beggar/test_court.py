import pytest
from beggar import Court

def test_court_permutationcount():
    a = Court()
    a.add('A', 4, 3)
    a.add('K', 3, 3)
    a.add('Q', 2, 3)
    a.add('J', 1, 3)
    print(a.permutations)
    assert a.permutations == sum(1 for x in a.permute())

def test_court_add_bad_label():
    a = Court()
    with pytest.raises(ValueError):
        a.add(-10000, 1, 2)

def test_court_add_bad_valuetype():
    a = Court()
    with pytest.raises(TypeError):
        a.add('A', 'bogon', 2)

def test_court_add_bad_valueneg():
    a = Court()
    with pytest.raises(ValueError):
        a.add('A', -1000, 2)

def test_court_add_bad_valuehigh():
    a = Court()
    with pytest.raises(ValueError):
        a.add('A', 100, 2)