"""Confirm the correctness of functions in question_two."""

import pytest

# ruff: noqa: PLR2004
from questions.question_two import (
    count_elements,
    find_pairs_with_sum,
    matrix_transpose,
)


@pytest.mark.question_two_part_a
def test_count_elements():
    """Confirm correctness of the count_elements function."""
    # check 1: List with repeated elements
    numbers = [1, 2, 2, 3, 3, 3]
    counts = count_elements(numbers)
    assert counts == {1: 1, 2: 2, 3: 3}, "Count elements in list with repetitions"
    # check 2: List with unique elements
    numbers = [1, 2, 3, 4]
    counts = count_elements(numbers)
    assert counts == {
        1: 1,
        2: 1,
        3: 1,
        4: 1,
    }, "Count elements in list with unique values"
    # check 3: Empty list
    numbers = []
    counts = count_elements(numbers)
    assert counts == {}, "Count elements in an empty list"


@pytest.mark.question_two_part_b
def test_find_pairs_with_sum():
    """Confirm correctness of the find_pairs_with_sum function."""
    # check 1: List with valid pairs
    numbers = [1, 2, 3, 4, 5]
    target_sum = 6
    pairs = find_pairs_with_sum(numbers, target_sum)
    assert sorted(pairs) == sorted([(1, 5), (2, 4)]), "Find pairs with valid sums"
    # check 2: List with no valid pairs
    numbers = [1, 2, 3]
    target_sum = 10
    pairs = find_pairs_with_sum(numbers, target_sum)
    assert pairs == [], "No pairs found with the target sum"
    # check 3: List with duplicates
    numbers = [1, 2, 2, 4]
    target_sum = 6
    pairs = find_pairs_with_sum(numbers, target_sum)
    assert sorted(pairs) == sorted([(2, 4)]), "Find pairs with duplicates in the list"
    # check 4: Empty list
    numbers = []
    target_sum = 6
    pairs = find_pairs_with_sum(numbers, target_sum)
    assert pairs == [], "Find pairs in an empty list"


@pytest.mark.question_two_part_c
def test_matrix_transpose():
    """Confirm correctness of the matrix_transpose function."""
    # check 1: Square matrix
    matrix = [[1, 2], [3, 4]]
    transposed = matrix_transpose(matrix)
    assert transposed == [[1, 3], [2, 4]], "Transpose of a square matrix"
    # check 2: Rectangular matrix
    matrix = [[1, 2, 3], [4, 5, 6]]
    transposed = matrix_transpose(matrix)
    assert transposed == [[1, 4], [2, 5], [3, 6]], "Transpose of a rectangular matrix"
    # check 3: Matrix with inconsistent row lengths
    matrix = [[1, 2], [3]]
    transposed = matrix_transpose(matrix)
    assert transposed is None, "Transpose of a matrix with inconsistent row lengths"
    # check 4: Empty matrix
    matrix = []
    transposed = matrix_transpose(matrix)
    assert transposed is None, "Transpose of an empty matrix"
