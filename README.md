# Fibonacci
By Will Brandon

A simple Fibonacci sequence generator program implemented using Python built with the Bunucu software management tool.

This program is intended to be simple and demonstrate usage of Bunucu for a Python project building with `pyproject.toml` and including tests.

## Usage

    fibonacci <size>

### Arguments

`size` - The number of Fibonacci sequence numbers to generate. Must be in the range [0, 105].

### Output Streams

`stdio` - A string of Fibonacci sequence numbers delimitered by spaces and terminated by a newline character.

`stderr` - Any errors that may be generated by an impropper arguments.

### Return Codes

`0` - If the series was successfully generated and output.

`1` - If any error occurred generating and displaying the series due to improper arguments.

## Examples

 1. `fibonacci 0` \
    **Result:** No result is produced.

 2. `fibonacci 1` \
    **Result:** `1` followed by a newline

 3. `fibonacci 3` \
    **Result:** `1 1 2` followed by a newline

 4. `fibonacci 7` \
    **Result:** `1 1 2 3 5 8 13` followed by a newline

 5. `fibonacci 10` \
    **Result:** `1 1 2 3 5 8 13 21 34 5` followed by a newline
