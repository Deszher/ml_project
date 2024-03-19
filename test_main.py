import pytest

from main import pipe

translate_testdata = [
    ("Не ищи счастье – оно всегда у тебя внутри", "Яна заўсёды ў цябе ўнутры"),
    ("Отличная сегодня погода!", "Выдатная сёння надвор'е!"),
]


@pytest.mark.parametrize("input,expected_output", translate_testdata)
def test_translate(input, expected_output):
    output = pipe(input, max_length=50)[0]['translation_text']

    assert output == expected_output
  
