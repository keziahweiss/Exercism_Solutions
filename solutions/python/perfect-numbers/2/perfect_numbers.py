def classify(number):
    """ A perfect number equals the sum of its positive divisors.
    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    number_sum = 0
    for num in range(1, (number // 2) + 1):
        if number % num == 0:
            number_sum += num
    if number_sum == number:
        return "perfect"
    if number_sum > number:
        return "abundant"
    if number_sum < number:
        return "deficient"
