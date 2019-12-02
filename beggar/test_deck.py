import pytest
from beggar import Deck
from beggar import Court

def test_deck_validcourt():
    
    with pytest.raises(TypeError):
        Deck(3, 52)

def test_deck_uneven():
    from beggar import Court
    with pytest.raises(ValueError):
        Deck(Court(), 1)

def test_deck_short():
    with pytest.raises(ValueError):
        Deck(Court().default(), 2)

def test_deck_len():
    assert 52 == len(Deck(Court().default(), 52))

def test_court_prop():
    assert isinstance(Deck(Court().default(), 52).court, Court)

def test_decksize_prop():
    assert 52 == Deck(Court().default(), 52).decksize
