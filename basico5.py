
def generate_primes():
    primes = [2, 3, 5, 7]  # optimization: avoid 2 here
    yield 1
    for number in primes:
        yield number
    number = 9
    max_divisor = 4
    while True:
        number += 2
        max_divisor += 2
        if not number & 0b1:  # optimization: remove
            continue
        divisible_by_known = False
        for known in primes:
            if known > max_divisor:  # not found
                break
            if not number % known:  # exact division
                divisible_by_known = True
                break
        if divisible_by_known:
            continue
        yield number


def get_is_prime(number, known_primes=[]):
    while known_primes[-1] < number:
        known_primes.append(next(prime_generator))
    return number in known_primes


def trace_function(frame, event, arg):
    # 'call', 'line', 'return', 'exception', 'c_call', 'c_return', or 'c_exception'
    if event in ('call', 'line', 'return', 'exception'):
        if frame.f_code.co_filename == 'basico5.py':
            visited_lines[frame.f_lineno] += 1
        return trace_function

import collections
visited_lines = collections.defaultdict(int)

import sys
sys.settrace(trace_function)

if __name__ == '__main__':
    import pprint
    import itertools
    pprint.pprint([
        prime
        for prime in itertools.takewhile(
            lambda x : 100 > x,
            generate_primes()
        )
    ])
    pprint.pprint(visited_lines)
