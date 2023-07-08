import pytest
from src.keyboard import Keyboard
kb = Keyboard('Dark Project KD87A', 9600, 5)

def test_change_lang():
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"

def test_error():

    # AttributeError: property 'language' of 'Keyboard' object has no setter
    with pytest.raises(AttributeError):
        assert kb.language == 'CH'

