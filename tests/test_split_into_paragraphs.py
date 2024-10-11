"""
Created by kevin-desktop, on the 11/10/2024
"""
import pytest
from palin import split_into_paragraphs

def test_split_into_paragraphs_regular():
    text = "First paragraph.\n\nSecond paragraph."
    assert split_into_paragraphs(text) == ["First paragraph.", "Second paragraph."]

def test_split_into_paragraphs_single_paragraph():
    text = "This is a single paragraph without newlines."
    assert split_into_paragraphs(text) == ["This is a single paragraph without newlines."]

def test_split_into_paragraphs_empty():
    text = ""
    assert split_into_paragraphs(text) == []

def test_split_into_paragraphs_multiple_newlines():
    text3n = "First paragraph.\n\n\nSecond paragraph."
    text4n = "First paragraph.\n\n\n\nSecond paragraph."
    assert split_into_paragraphs(text3n) == ["First paragraph.",  "Second paragraph."]
    assert split_into_paragraphs(text4n) == ["First paragraph.", "Second paragraph."]
