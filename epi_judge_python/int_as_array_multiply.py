from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    sign = -1 if (num1[0] < 0 and num2[0] > 0) or (num1[0] > 0 and num2[0] < 0) else 0
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])
    results = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            results[i+j+1] += num1[i] * num2[i]
            results[i+j] = results[i+j+1] % 10
            results[i+j+1] %= 10
    results = results[next((i for i, x in enumerate(results) if x != 0), len(results)):] or [0]
    return [sign * results[0]] + results[1:]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
