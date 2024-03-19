"""
Module docstring: This module contains tests for the pipe function in main.py.
"""

import pytest

from main import pipe

translate_testdata = [
    ("Не ищи счастье – оно всегда у тебя внутри", "Яна заўсёды ў цябе ўнутры"),
    ("Отличная сегодня погода!", "Выдатная сёння надвор'е!"),
]


@pytest.mark.parametrize("inp,expected_output", translate_testdata)
def test_translate(inp, expected_output):
    """
    Function docstring: Test the pipe function with various input strings.
    """
    output = pipe(inp, max_length=50)[0]['translation_text']

    assert output == expected_output
