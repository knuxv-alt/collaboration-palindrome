import pytest
from palin import count_palindromes

def test_count_palindromes_regular():
    paragraph = "Anna went to the civic center to see a kayak race."
    assert count_palindromes(paragraph) == ["anna", "civic", "kayak"]

def test_count_palindromes_no_palindromes():
    paragraph = "This is a normal sentence without palindromes."
    assert count_palindromes(paragraph) == []

def test_count_palindromes_with_punctuation():
    paragraph = "Madam, in Eden, I'm ELLE."
    assert count_palindromes(paragraph) == ["madam", "elle"]  # Should ignore punctuation

def test_count_palindromes_empty_paragraph():
    assert count_palindromes("") == []
