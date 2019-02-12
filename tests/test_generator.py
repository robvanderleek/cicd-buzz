"""Test generator.py with pytest"""
import unittest
from buzz import generator


def test_sample_single_word():
    list_ = ('foo', 'bar', 'foobar')
    word = generator.sample(list_)
    assert word in list_


def test_sample_multiple_words():
    list_ = ('foo', 'bar', 'foobar')
    words = generator.sample(list_, 2)
    assert len(words) == 2
    assert words[0] in list_
    assert words[1] in list_
    assert words[0] is not words[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
