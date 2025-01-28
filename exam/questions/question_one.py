"""Question One: Example Executable Examination."""

# Note: The imports in the following source code block may no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

from typing import List, Union

# Introduction: Read This First! {{{

# Keep in mind these considerations as you implement the required functions:

# --> You must implement Python functions to complete each of these steps,
# bearing in mind that one defective function may break another function.

# --> Your source code must adhere to industry best practices in, for instance,
# source code formatting, variable naming, and documentation.

# --> You may refer to the checks that are specified in the exam/gatorgrade.yml file
# in this GitHub repository for the configuration and name of each tool used
# to analyze the code inside of this file.

# }}}

# Part (a) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function find_minimum_value should:
# - Take a list of lists of integers, called matrix, as its parameter
# - Return an integer that represents the minimum value in the matrix

# Note: If the function is called with an invalid input (e.g., an empty
# matrix), it should return None.

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.


def find_minimum_value(matrix: List[List[int]]) -> Union[int, None]:
    """Return the minimum value in the provided matrix."""
    # confirm that there is a value in the [0][0] position
    if not matrix or not matrix[0]:
        return None
    minimum_value = matrix[0][0]
    for row in matrix:
        for value in row:
            if value < minimum_value:
                minimum_value = value
    return minimum_value


# }}}

# Part (b) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function find_maximum_value should:
# - Take a list of lists of integers, called matrix, as its parameter
# - Return an integer that represents the maximum value in the matrix

# Note: If the function is called with an invalid input (e.g., an empty
# matrix), it should return None.

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.


def find_maximum_value(matrix: List[List[int]]) -> Union[int, None]:
    """Return the maximum value in the provided matrix."""
    # confirm that there is a value in the [0][0] position
    if not matrix or not matrix[0]:
        return None
    maximum_value = matrix[0][0]
    for row in matrix:
        for value in row:
            if value > maximum_value:
                maximum_value = value
    return maximum_value


# }}}


# Part (c) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function find_average_value should:
# - Take a list of lists of integers, called matrix, as its parameter
# - Return a floating-point number that represents the average value of all numbers in the matrix

# Note: If the function is called with an invalid input (e.g., an empty
# matrix), it should return None.

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.


def find_average_value(matrix: List[List[int]]) -> Union[float, None]:
    """Find the average value in the provided matrix."""
    # check if the matrix is empty
    if not matrix or not matrix[0]:
        return None
    # initialize sum and count variables
    total_sum = 0
    count = 0
    # iterate over the matrix to calculate the sum and count the number of elements
    for row in matrix:
        for value in row:
            total_sum += value
            count += 1
    # calculate and return the average value
    return total_sum / count


# }}}
