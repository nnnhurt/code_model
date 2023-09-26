"""Test module main."""


from typing import List

import pytest

from main import get_possible_numbers

some_numbers = (
    ('56', ['56', '46', '26', '66', '86', '55', '53', '59']),
    ('120', ['120', '220', '420', '110', '150', '130', '128']),
    ('256', ['256', '156', '556', '356', '226', '246', '266', '286', '253', '255', '259']),
    ('1000', ['1000', '2000', '4000', '1800', '1080', '1008']),
)


@pytest.mark.parametrize('text, expected', some_numbers)
def test_password_detective(text: str, expected: List) -> None:
    """Test our detective function.

    Args:
        text: - input text parameter
        expected: - expected list parameter

    Asserts:
        True if answer is correct
    """
    assert sorted(get_possible_numbers(text)) == sorted(expected)
