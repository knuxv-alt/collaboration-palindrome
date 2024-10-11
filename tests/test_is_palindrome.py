import pytest
from palin import is_palindrome

def test_is_palindrome_regular():
    assert is_palindrome("madam") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False

def test_is_palindrome_mixed_case():
    assert is_palindrome("MadAm") == True

def test_is_palindrome_empty_string():
    assert not is_palindrome("")
    assert not is_palindrome("a")

def test_is_palindrome_accents():
    assert is_palindrome("réifier")

def test_is_palindrome_special_characters():
    assert is_palindrome("A man, a plan, a canal, Panama") == False  # Special chars should invalidate
