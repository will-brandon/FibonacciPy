"""
File:   fibonacci/fibonacci.py
Type:   Python Module
Author: Will Brandon <dev.willbrandon@gmail.com>
Date:   Thu, Jul 4, 2024

Copyright (c) Will Brandon, 2024.

Defines functionality to create Fibonacci sequences.
"""

from typing import List


FIBONACCI_MIN_SEQUENCE_SIZE = 0
"""
The minimum Fibonacci sequence size supported.
"""

FIBONACCI_MAX_SEQUENCE_SIZE = 93
"""
The maximum Fibonacci sequence size supported.
"""


def fibonacci(n: int) -> List[str]:
    """
    Generates `n` Fibonacci sequence integers.

    Params
    ------
    `n` : `int`
        The size of the sequence.
    
    Returns
    -------
    `List[int]`
        The memory buffer to the sequence was written to.
    
    Raises
    ------
    `ValueError`
        If `n`, falls outside the range [`FIBONACCI_MIN_SEQUENCE_SIZE`, `FIBONACCI_MAX_SEQUENCE_SIZE`].
    """

    if n < FIBONACCI_MIN_SEQUENCE_SIZE or n > FIBONACCI_MAX_SEQUENCE_SIZE:
        raise ValueError(f'Invalid Fibonacci sequence size given: {n}. Must be in range ' \
                         f'[{FIBONACCI_MIN_SEQUENCE_SIZE}, {FIBONACCI_MAX_SEQUENCE_SIZE}].')

    sequence = [1, 1]

    if n < 3:
        return sequence[:n]
    
    for i in range(2, n):
        sequence.append(sequence[i - 2] + sequence[i - 1])
    
    return sequence
