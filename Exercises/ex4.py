def is_prime(number):
    if type(number) != int or number <= 1:
        return False
    return len([i for i in range(
        1, number + 1) if (number % i == 0)]) <= 2


def get_prime_numbers_till(limit):
    if type(limit) != int or limit <= 1:
        return []
    return [number for number in range(2, limit + 1) if is_prime(number)]


print(get_prime_numbers_till(3))
