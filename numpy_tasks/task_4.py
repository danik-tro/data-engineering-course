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
