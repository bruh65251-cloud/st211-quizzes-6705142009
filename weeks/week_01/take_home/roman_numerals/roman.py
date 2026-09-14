import re


ROMAN_VALUES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


VALID_ROMAN_PATTERN = (
    r"^M{0,3}"
    r"(CM|CD|D?C{0,3})"
    r"(XC|XL|L?X{0,3})"
    r"(IX|IV|V?I{0,3})$"
)


def convert(number: str) -> int:
    if not number:
        raise ValueError("Roman numeral cannot be empty")

    if not re.fullmatch(VALID_ROMAN_PATTERN, number):
        raise ValueError("Invalid Roman numeral")

    total = 0

    for index in range(len(number)):
        current_value = ROMAN_VALUES[number[index]]

        if index + 1 < len(number):
            next_value = ROMAN_VALUES[number[index + 1]]

            if current_value < next_value:
                total -= current_value
            else:
                total += current_value
        else:
            total += current_value

    return total