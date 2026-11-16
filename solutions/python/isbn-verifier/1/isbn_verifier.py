def is_valid(isbn):
    number = ""
    for digit in isbn:
        if digit != "-":
            number += digit
    if len(number) != 10:
        return False
    total = 0
    for i, num in enumerate(number):
        if num == "X" and i == 9:
            value = 10
        elif num.isdigit():
            value = int(num)
        else:
            return False
        total += value * (10 - i)
    return total % 11 == 0