# data-engineering-course
CE Data engineering course

## Tasks
### NumPy Tasks

The tasks related to NumPy are located in the `numpy_tasks` directory. Each task is implemented as a separate Python script. You can run each task individually by executing the corresponding script, named `task_1.py`, `task_2.py`, `task_3.py`, `task_4.py`.

#### Running the Tasks

To run a specific task, navigate to the `numpy_tasks` directory and execute the desired script using Python. For example, to run the first task:

```bash
python numpy_tasks/task_1.py
```

## Setup

Follow these steps to set up the project environment and install all dependencies.

1. **Activate Virtual Environment:**

   Ensure you have a virtual environment set up. If not, create one:

    ```bash
    python3 -m venv venv
    ```

   Then activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```

3. **Install Poetry:**

   Poetry is used for dependency management in this project. Install it by running:

    ```bash
    pip install poetry
    ```

4. **Install Project Dependencies:**

   With Poetry installed, you can now install all project dependencies:

    ```bash
    poetry install
    ```

5. **Set Up Pre-commit Hooks:**

   To ensure code quality and consistency, this project uses `pre-commit` hooks. Install them with:

    ```bash
    pre-commit install
    ```

Or just run all commands in the one single command

```bash
make setup
```

After completing these steps, your environment should be set up and ready for development.
