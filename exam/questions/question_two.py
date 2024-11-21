"""Python Exam: Executable Examination Questions."""

# Note: The imports in the following source code block adhere to the
# industry best practices for Python source code.

from typing import List, Union, Tuple

# Introduction: Read This First! {{{

# Keep in mind these considerations as you implement the required functions:

# --> You must implement Python functions to complete each of these steps,
# bearing in mind that one defective function may break another function.

# --> Your source code must adhere to industry best practices in, for instance,
# source code formatting, variable naming, and documentation.

# }}}

# Part (a) {{{

# Function specification:
# The function count_elements should:
# - Take a list of integers, called numbers, as its parameter.
# - Return a dictionary where each key is a unique integer from the list,
#   and its value is the count of that integer in the list.

# Note: If the function is called with an empty list, it should return an empty dictionary.


def count_elements(numbers: List[int]) -> dict[int, int]:
    """Count the occurrences of each element in the list."""
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    return counts


# }}}

# Part (b) {{{

# Function specification:
# The function find_pairs_with_sum should:
# - Take a list of integers, called numbers, and an integer, target_sum, as its parameters.
# - Return a list of unique tuples, where each tuple contains two numbers from the list
#   that add up to the target_sum. Ensure each pair is listed only once.

# Note: If no pairs exist, the function should return an empty list.


def find_pairs_with_sum(numbers: List[int], target_sum: int) -> List[Tuple[int, int]]:
    """Find unique pairs of numbers that add up to a target sum."""
    seen = set()
    pairs = set()
    for number in numbers:
        complement = target_sum - number
        if complement in seen:
            pairs.add(tuple(sorted((number, complement))))
        seen.add(number)
    return list(pairs)


# }}}

# Part (c) {{{

# Function specification:
# The function matrix_transpose should:
# - Take a list of lists of integers, called matrix, as its parameter.
# - Return a new list of lists that represents the transpose of the input matrix.

# Note: If the matrix is empty or has inconsistent row lengths, return None.


def matrix_transpose(matrix: List[List[int]]) -> Union[List[List[int]], None]:
    """Transpose the given matrix."""
    if not matrix or any(len(row) != len(matrix[0]) for row in matrix):
        return None
    return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]


# }}}