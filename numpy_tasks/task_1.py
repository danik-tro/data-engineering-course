"""Practical Task 1: Basic Array Creation and Manipulation with NumPy
Objective:
Introduce basic operations in NumPy by creating and manipulating simple arrays.
Requirements:
1. Array Creation:
    - Create a one-dimensional NumPy array with values ranging from 1 to 10.
    - Create a two-dimensional NumPy array (matrix) with shape (3, 3)
        containing values from 1 to 9.
2. Basic Operations:
    - Indexing and Slicing:
        1. Access and print the third element of the one-dimensional array.
        2. Slice and print the first two rows and
            columns of the two-dimensional array.
    - Basic Arithmetic:
        1. Add 5 to each element of the one-dimensional array and print the result.
        2. Multiply each element of the two-dimensional array by 2 and print the result.
3. Output Function:
    - Implement a separate function named print_array that
        takes an array and an optional message as input,
        and prints them to the console. This function will be used to display
        the state of the array,
        maintaining separation from the manipulation logic.
4. Manipulation Workflow:
    - Create the initial arrays.
    - Perform each basic operation sequentially.
        Using the print_array function to output the arrays and output results to the console,
        when needed.
5. Execution and Verification: Test the script to ensure that code executes as expected and that
    the console outputs correctly display the changes to the array.

Deliverables:
A Python script (.py file) containing all the functions along with
    the code to create the initial arrays and execute all manipulations.
"""

from typing import Any

import numpy as np
import numpy.typing as npt


def print_array(array: npt.NDArray[Any], message: str = "Array:") -> None:
    print(f"{message} {array}\n")  # noqa: T201


if __name__ == "__main__":
    one_d_array = np.arange(1, 11)
    print_array(one_d_array, "One-dimensional array:")

    two_d_array = np.arange(1, 10).reshape(3, 3)
    print_array(two_d_array, "Two-dimensional array (3x3):\n")

    third_element = one_d_array[2]
    print_array(third_element, "Third element of the one-dimensional array:")

    sliced_array = two_d_array[:2, :2]
    print_array(sliced_array, "First two rows and columns of the two-dimensional array:\n")

    added_array = one_d_array + 5
    print_array(added_array, "One-dimensional array after adding 5:\n")

    multiplied_array = two_d_array * 2
    print_array(multiplied_array, "Two-dimensional array after multiplying by 2:\n")
