def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    sum = 0
    for num in range(1, (number // 2) + 1):
        if number % num == 0:
            sum += num
    if sum == number:
        return "perfect"
    elif sum > number:
        return "abundant"
    elif sum < number:
        return "deficient"
