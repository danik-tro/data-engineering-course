"""Practical Task 3: Array Manipulation with Separate Output Function in NumPy

Objective: Develop a set of Python functions using NumPy to manipulate arrays through operations
such as transposing, reshaping, splitting, and combining.

Requirements:
    1. Array Creation:
        o Generate a multi-dimensional NumPy array with random values.
            The array should have a complex structure (e.g., a 6x6 matrix of integers)
            to clearly demonstrate changes through each manipulation.
    2. Array Manipulation Functions:
        o Transpose Function: Create a function to transpose the array and return the result.
        o Reshape Function: Develop a function to reshape the array into a
            new configuration (e.g., from a 6x6 matrix to a 3x12 matrix)
            and return the reshaped array.
        o Split Function: Implement a function that splits the array into multiple
            sub-arrays along a specified axis and returns the sub-arrays.
        o Combine Function: Construct a function that combines
            several arrays into one and returns the combined array.
    3. Output Function:
        o Implement a separate function named print_array that
            takes an array and an optional message as input,
            and prints them to the console. This function will be used to display the
            state of the array before and after
            each manipulation, maintaining separation from the manipulation logic.
    4. Manipulation Workflow:
        o Call each manipulation function sequentially on the initial
            array, passing the output of one function as input to the next where necessary.
            After each manipulation, use the print_array function to output the
            results to the console with appropriate messages.
    5. Execution and Verification:
        o Test the script to ensure that all functions execute as
            expected and that the console outputs correctly display the changes to the array.
        o Use assertions to verify that the dimensions and
            integrity of the array are maintained or appropriately altered after each manipulation.

Deliverables:
A Python script (.py file) containing all the functions, along with the code to create the initial
array and execute all manipulations.
"""

from typing import Any

import numpy as np
import numpy.typing as npt


def create_random_array() -> npt.NDArray[Any]:
    np.random.seed(42)
    return np.random.randint(1, 100, size=(6, 6))


def transpose_array(array: npt.NDArray[Any]) -> npt.NDArray[Any]:
    return np.transpose(array)


def reshape_array(array: npt.NDArray[Any], new_shape: tuple[int, int]) -> npt.NDArray[Any]:
    return np.reshape(array, new_shape)


def split_array(array: npt.NDArray[Any], num_splits: int, axis: int = 0) -> list[npt.NDArray[Any]]:
    return np.array_split(array, num_splits, axis=axis)


def combine_arrays(arrays: list[npt.NDArray[Any]], axis: int = 0) -> npt.NDArray[Any]:
    return np.concatenate(arrays, axis=axis)


def print_array(array: npt.NDArray[Any], message: str = "Array:") -> None:
    print(f"{message}\n{array}\n")


def workflow(prints: bool = False) -> Any:
    initial_array = create_random_array()

    if prints:
        print_array(initial_array, "Initial 6x6 Array:")

    transposed_array = transpose_array(initial_array)
    if prints:
        print_array(transposed_array, "Transposed Array:")

    reshaped_array = reshape_array(transposed_array, (3, 12))
    if prints:
        print_array(reshaped_array, "Reshaped Array (3x12):")

    split_arrays = split_array(reshaped_array, 3, axis=0)
    for i, arr in enumerate(split_arrays):
        if prints:
            print_array(arr, f"Split Array {i+1}:")

    combined_array = combine_arrays(split_arrays, axis=0)

    if prints:
        print_array(combined_array, "Combined Array:")

    return initial_array, transposed_array, reshaped_array, split_arrays, combined_array


if __name__ == "__main__":
    workflow(prints=True)
