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
