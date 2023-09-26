"""A simple module which solves educational task."""


def get_possible_numbers(number: str) -> list[int]:
    """
    Calculate possible phone numbers.

    Args:
        number: str -  string represents seen by detective number

    Returns:
        list[str] - possible phone numbers
    """
    matrix = {
        1: (2, 4),
        2: (1, 5, 3),
        3: (2, 6),
        4: (1, 5, 7),
        5: (2, 4, 6, 8),
        6: (3, 5, 9),
        7: (4, 8),
        8: (0, 5, 7, 9),
        9: (8, 6),
        0: (8, ),
    }
    answer = [number]
    for ix, digit in enumerate(number):
        for possible in matrix[int(digit)]:
            current = number[:ix]
            current += str(possible)
            current += number[ix + 1:]
            answer.append(current)
    return answer
