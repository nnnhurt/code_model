def get_possible_numbers(number: str):
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
    for i, digit in enumerate(number):
        for possible in matrix[int(digit)]:
            print(i)
            answer.append(number[:i] + str(possible) + number[i+1:])
    return answer