import pytest

from roman import convert


@pytest.mark.parametrize(
    "roman, expected",
    [
        ("I", 1),
        ("V", 5),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000),
    ],
)
def test_basic_symbols(roman, expected):
    # Act
    result = convert(roman)

    # Assert
    assert result == expected


@pytest.mark.parametrize(
    "roman, expected",
    [
        ("II", 2),
        ("III", 3),
        ("VI", 6),
        ("XVI", 16),
    ],
)
def test_additive_numbers(roman, expected):
    # Act
    result = convert(roman)

    # Assert
    assert result == expected


@pytest.mark.parametrize(
    "roman, expected",
    [
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
    ],
)
def test_subtractive_numbers(roman, expected):
    # Act
    result = convert(roman)

    # Assert
    assert result == expected


def test_combined_number():
    # Arrange
    roman = "XIX"
    expected = 19

    # Act
    result = convert(roman)

    # Assert
    assert result == expected


@pytest.mark.parametrize(
    "roman",
    [
        "VX",
        "XXC",
    ],
)
def test_invalid_numbers_raise_error(roman):
    with pytest.raises(ValueError):
        convert(roman)