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


def fibonacci(n: int) -> List[int]:
    """
    Generates `n` Fibonacci sequence integers.

    Params
    ------
    `n` : `int`
        The size of the sequence.
    
    Returns
    -------
    `List[int]`
        The sequence integers.
    
    Raises
    ------
    `ValueError`
        If `n`, falls outside the range [`FIBONACCI_MIN_SEQUENCE_SIZE`, `FIBONACCI_MAX_SEQUENCE_SIZE`].
    """

    # Raise an error if the sequence size is invalid.
    if n < FIBONACCI_MIN_SEQUENCE_SIZE or n > FIBONACCI_MAX_SEQUENCE_SIZE:
        raise ValueError(f'Invalid Fibonacci sequence size given: {n}. Must be in range ' \
                         f'[{FIBONACCI_MIN_SEQUENCE_SIZE}, {FIBONACCI_MAX_SEQUENCE_SIZE}].')

    # Start the sequence with base-cases for the first 2 values.
    sequence = [1, 1]

    # If the requested sequence size can be handled by only base-cases, simply return the proper sublist.
    if n < 3:
        return sequence[:n]
    
    # For all values after the first 2 base-cases, calculate the value to be the sum of the two prior values.
    for i in range(2, n):
        sequence.append(sequence[i - 2] + sequence[i - 1])
    
    # Return the generated sequence.
    return sequence
