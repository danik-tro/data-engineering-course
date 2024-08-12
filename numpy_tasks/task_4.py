"""Practical Task 4: Comprehensive Data Handling and Analysis with NumPy

Objective: Develop a set of Python functions using NumPy to handle
    reading/writing data and performing aggregate analyses on arrays.

Requirements:
    1. Array Creation:
        o Generate a multi-dimensional NumPy array with random values.
            The array should have a complex structure (e.g., a 10x10 matrix of integers)
            to clearly demonstrate changes through each manipulation.
    2. Data I/O Functions:
        o Save Function: Create a function to save the array
            to a text file, a CSV file, and a binary format (.npy or .npz).
        o Load Function: Develop a function to load the
            array from each of the saved formats back into NumPy arrays.
    3. Aggregate Functions:
        o Summation Function: Create a function to compute the summation of all elements.
        o Mean Function: Develop a function to calculate the mean of the array.
        o Median Function: Implement a function to find the median of the array.
        o Standard Deviation Function: Construct a function to calculate
            the standard deviation of the array.
        o Axis-Based Aggregate Functions: Create functions to apply these aggregate
            operations along different axes (row-wise and column-wise).
    4. Output Function:
        o Implement a separate function named print_array that takes
            any array and an optional message as input, and prints them to the console.
            This function will be used to display the state of the array before and after
            each manipulation, maintaining separation from the manipulation logic.
    5. Manipulation Workflow:
        o Array Creation and Saving: Create the initial array
            and save it in different formats using the save function.
        o Loading and Verification: Load the arrays back and verify
            their integrity using the load function and the print_array
            function to display the original and loaded arrays.
        o Aggregate Computation and Reporting: Compute aggregate
            functions on the original array and output the results of aggregate
            computations with appropriate messages.
    6. Execution and Verification:
        o Test the script to ensure that all functions execute as
            expected and that the console outputs correctly display the changes to the array.
        o Use assertions to verify that the dimensions and integrity
            of the array are maintained or appropriately altered after each manipulation.
            Also verify the results of aggregate functions.

Deliverables:
A Python script (.py file) containing all the functions, along with the code to create the initial
array, save/load it in different formats, perform aggregate calculations, and execute all
manipulations.
"""

from typing import Any

import numpy as np
import numpy.typing as npt


def create_random_array() -> npt.NDArray[Any]:
    np.random.seed(42)
    return np.random.randint(1, 100, size=(10, 10))


def save_array(array: npt.NDArray[Any], filename: str) -> None:
    np.savetxt(f"{filename}.txt", array, fmt="%d")
    np.savetxt(f"{filename}.csv", array, delimiter=",", fmt="%d")
    np.save(f"{filename}.npy", array)
    np.savez(f"{filename}.npz", array)


def load_array(filename: str, file_format: str) -> Any:
    if file_format == "txt":
        return np.loadtxt(f"{filename}.txt", dtype=int)
    if file_format == "csv":
        return np.loadtxt(f"{filename}.csv", delimiter=",", dtype=int)
    if file_format == "npy":
        return np.load(f"{filename}.npy")
    return np.load(f"{filename}.npz")["arr_0"]


def compute_sum(array: npt.NDArray[Any]) -> Any:
    return np.sum(array)


def compute_mean(array: npt.NDArray[Any]) -> Any:
    return np.mean(array)


def compute_median(array: npt.NDArray[Any]) -> Any:
    return np.median(array)


def compute_std(array: npt.NDArray[Any]) -> Any:
    return np.std(array)


def compute_sum_along_axis(array: npt.NDArray[Any], axis: int) -> Any:
    return np.sum(array, axis=axis)


def compute_mean_along_axis(array: npt.NDArray[Any], axis: int) -> Any:
    return np.mean(array, axis=axis)


def compute_median_along_axis(array: npt.NDArray[Any], axis: int) -> Any:
    return np.median(array, axis=axis)


def compute_std_along_axis(array: npt.NDArray[Any], axis: int) -> Any:
    return np.std(array, axis=axis)


def print_array(array: Any, message: str = "Array:") -> None:
    print(f"{message}\n{array}\n")


def workflow() -> Any:
    initial_array = create_random_array()
    print_array(initial_array, "Initial 10x10 Array:")
    save_array(initial_array, "test_array")

    print("Array saved in .txt, .csv, .npy, and .npz formats.\n")

    loaded_txt_array = load_array("test_array", "txt")
    loaded_csv_array = load_array("test_array", "csv")
    loaded_npy_array = load_array("test_array", "npy")
    loaded_npz_array = load_array("test_array", "npz")

    print_array(loaded_txt_array, "Loaded Array from .txt:")
    print_array(loaded_csv_array, "Loaded Array from .csv:")
    print_array(loaded_npy_array, "Loaded Array from .npy:")
    print_array(loaded_npz_array, "Loaded Array from .npz:")

    total_sum = compute_sum(initial_array)
    print(f"Total Sum of elements: {total_sum}\n")

    mean_value = compute_mean(initial_array)
    print(f"Mean of elements: {mean_value}\n")

    median_value = compute_median(initial_array)
    print(f"Median of elements: {median_value}\n")

    std_deviation = compute_std(initial_array)
    print(f"Standard Deviation of elements: {std_deviation}\n")

    sum_along_rows = compute_sum_along_axis(initial_array, axis=1)
    print_array(sum_along_rows, "Sum along rows:")

    sum_along_cols = compute_sum_along_axis(initial_array, axis=0)
    print_array(sum_along_cols, "Sum along columns:")

    mean_along_rows = compute_mean_along_axis(initial_array, axis=1)
    print_array(mean_along_rows, "Mean along rows:")

    mean_along_cols = compute_mean_along_axis(initial_array, axis=0)
    print_array(mean_along_cols, "Mean along columns:")

    median_along_rows = compute_median_along_axis(initial_array, axis=1)
    print_array(median_along_rows, "Median along rows:")

    median_along_cols = compute_median_along_axis(initial_array, axis=0)
    print_array(median_along_cols, "Median along columns:")

    std_along_rows = compute_std_along_axis(initial_array, axis=1)
    print_array(std_along_rows, "Standard Deviation along rows:")

    std_along_cols = compute_std_along_axis(initial_array, axis=0)
    print_array(std_along_cols, "Standard Deviation along columns:")

    return initial_array, loaded_txt_array, loaded_csv_array, loaded_npy_array, loaded_npz_array


if __name__ == "__main__":
    initial_array, loaded_txt_array, loaded_csv_array, loaded_npy_array, loaded_npz_array = (
        workflow()
    )

    assert np.array_equal(
        initial_array, loaded_txt_array
    ), "Loaded .txt array does not match the original."
    assert np.array_equal(
        initial_array, loaded_csv_array
    ), "Loaded .csv array does not match the original."
    assert np.array_equal(
        initial_array, loaded_npy_array
    ), "Loaded .npy array does not match the original."
    assert np.array_equal(
        initial_array, loaded_npz_array
    ), "Loaded .npz array does not match the original."
