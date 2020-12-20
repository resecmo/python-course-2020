import argparse
from multiprocessing import Pool


def factorize(n):
    possible_divisor = 2
    divisors = []
    while n != 1:
        while n % possible_divisor == 0:
            n //= possible_divisor
            divisors.append(possible_divisor)
        possible_divisor += 1
    return divisors


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("integers", type=int, nargs='*')
    numbers = vars(parser.parse_args())['integers']

    with Pool() as p:
        factorized = p.map(factorize, numbers)

    for pair in zip(numbers, factorized):
        print(f"{pair[0]}:", *pair[1])
