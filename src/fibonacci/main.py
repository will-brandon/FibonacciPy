"""
File:   fibonacci/main.py
Type:   Python Entrypoint Module
Author: Will Brandon <dev.willbrandon@gmail.com>
Date:   Thu, Jul 4, 2024

Copyright (c) Will Brandon, 2024.


"""

from typing import NoReturn, List
import sys

from fibonacci.fibonacci import fibonacci


USAGE = 'Usage: fibonacci <size>'
"""
A string defining usage information about the `fibonacci` program.
"""


def err(msg: str, exit_code: int=1) -> NoReturn:
    """
    Displays a description of how to use the program followed by a given error message, then exits with the given code,
    or 1 by default. All output is sent to `stderr`.
    
    Params
    ------
    `msg` : `str`
        The error message string.
    `exit_code` : `int` (default: `1`)
        The program exit code.
    
    Note
    ----
    This function is marked to return `NoReturn` because the function is guaranteed to exit the program.

    Author
    ------
    Will Brandon <dev.willbrandon@gmail.com>
    """

    # Display the usage description.
    print(USAGE, file=sys.stderr)
  
    # Display the prefixed error message.
    print(f'Error: {msg}', file=sys.stderr)

    # Exit with the appropriate code.
    exit(exit_code)


def main(argv: List[str]) -> int:
    """
    Begins the `fibonacci` program.

    Params
    ------
    `argv` : `List[str]`
        The list of program arguments starting with the program name.
    
    Returns
    -------
    `int`
        The program exit code.
    
    Author
    ------
    Will Brandon <dev.willbrandon@gmail.com>
    """

    # Determine the number of command-line arguments provided including the program name.
    argc = len(argv)

    # If only one argument is present, i.e. just the program name with no explicit arguments, then show an error message
    # and exit.
    if argc == 1:
        err('A count argument is required.')
    
    # If more than two arguments are present, i.e. more than one explicit argument, then show an error message and exit.
    if argc > 2:
        err('Only one argument is allowed.')

    # If the argument cannot be interpreted as an integer value show an error message and exit.
    try:
        sequence_size = int(argv[1])
    except ValueError:
        err('The sequence size argument must be castable into an integer.')
    
    # If a sequence size of zero is given, simply do nothing and return successfully.
    if sequence_size == 0:
        return 0
    
    # Try to create the sequence. If the sequence size is not within the expected range then show the error message and
    # exit.
    try:
        sequence = fibonacci(sequence_size)
    except ValueError as exc:
        err(str(exc))

    # Print all members of the sequence delimitered by spaces. This requires converting each to a string first.
    print(' '.join([str(item) for item in sequence]))

    # Return successfully.
    return 0


def entrypoint() -> NoReturn:
    """
    Begins the Fibonacci sequence Python program.

    Note
    ----
    This function is marked to return `NoReturn` because the function is guaranteed to exit the program.

    Author
    ------
    Will Brandon <dev.willbrandon@gmail.com>
    """

    # Exit with the code returned from the main function, and provide the main function with the list of program
    # arguments.
    sys.exit(main(sys.argv))
