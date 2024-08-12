from numpy_tasks.task_3 import workflow


def test_workflow():
    initial_array, transposed_array, reshaped_array, split_arrays, combined_array = workflow()

    assert initial_array.shape == (6, 6), "Initial array shape should be 6x6"
    assert transposed_array.shape == (6, 6), "Transposed array shape should be 6x6"
    assert reshaped_array.shape == (3, 12), "Reshaped array should have shape 3x12"
    assert all(arr.shape[0] == 1 for arr in split_arrays), "Each split array should have 1 row"
    assert combined_array.shape == (3, 12), "Combined array should have shape 3x12"
