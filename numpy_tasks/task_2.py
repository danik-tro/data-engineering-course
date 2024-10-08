"""Practical Task 2: Analyzing and Visualizing E-Commerce Transactions with NumPy
Objective:
Develop a set of Python functions using NumPy to manipulate and analyze a simulated
    e-commerce dataset.

Requirements:
    1. Array Creation:
        - Generate a multi-dimensional NumPy array with predefined values to simulate
            e-commerce transactions. The array should include
            transaction_id, user_id, product_id, quantity, price, and timestamp.
    2. Data Analysis Functions:
        - Total Revenue Function: Create a function to calculate
            the total revenue generated by multiplying quantity and price, and summing the result.
        - Unique Users Function: Develop a function
            to determine the number of unique users who made transactions.
        - Most Purchased Product Function: Implement a
            function to identify the most purchased product based on the quantity sold.
        - Type Casting and Checking Functions:
            - Create a function to convert the price array from float to integer.
            - Develop a function to check the data types of each column in the array.
    3. Array Manipulation Functions:
        - Product Quantity Array Function: Create a function that returns
            a new array with only the product_id and quantity columns.
        - User Transaction Count Function: Implement a function to
             generate an array of transaction counts per user.
        - Masked Array Function: Create a function to generate a masked
            array that hides transactions where the quantity is zero.
    4. Arithmetic and Comparison Functions:
        - Price Increase Function: Develop a function to increase
            all prices by a certain percentage (e.g., 5% increase).
        - Filter Transactions Function: Implement a function to filter
             transactions to only include those with a quantity greater than 1.
        - Revenue Comparison Function: Create a function to compare
             the revenue from two different time periods.
    5. Indexing and Slicing Functions:
        - User Transactions Function: Create a function to extract all
            transactions for a specific user.
        - Date Range Slicing Function: Develop a function to slice the
            dataset to include only transactions within a specific date range.
        - Top Products Function: Implement a function using advanced
            indexing to retrieve transactions of the top 5 products by revenue.
    6. Output Function:
        - Implement a separate function named print_array that takes an
            array and an optional message as input,
            and prints them to the console. This function will be used to display the
            state of the array, maintaining separation from the manipulation logic.
    7. Manipulation Workflow:
        - Call each analysis and manipulation function sequentially on the array.
        Use the print_array function to output arrays to the console with appropriate messages.
        Also output results to the console, when needed.
    8. Execution and Verification:
        - Test the script to ensure that all functions execute as expected and that
        the console outputs correctly display the changes to the array.
        - Use assertions to verify that the dimensions and integrity of the array
        are maintained or appropriately altered after each manipulation.

Deliverables:
A Python script (.py file) containing all the functions,
along with the code to create the initial array and execute all manipulations.
"""

import datetime
from typing import Any

import factory
import numpy as np
import numpy.typing as npt
from faker import Faker

fake = Faker()


class Transaction:
    def __init__(
        self,
        transaction_id: int,
        user_id: int,
        product_id: int,
        quantity: int,
        price: int,
        timestamp: npt.DTypeLike,
    ) -> None:
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.timestamp = timestamp


class TransactionFactory(factory.Factory):  # type: ignore[misc]
    class Meta:
        model = Transaction

    transaction_id = factory.Sequence(lambda n: n + 1)
    user_id = factory.LazyAttribute(lambda _: fake.random_int(min=100, max=105))
    product_id = factory.LazyAttribute(lambda _: fake.random_int(min=40, max=65))
    quantity = factory.LazyAttribute(lambda _: fake.random_int(min=1, max=10))
    price = factory.LazyAttribute(
        lambda _: round(fake.random_number(digits=3, fix_len=False) + 1, 2)
    )
    timestamp = factory.LazyAttribute(
        lambda _: np.datetime64(
            fake.date_time_between_dates(
                datetime.date.today() - datetime.timedelta(weeks=6), datetime.date.today()
            )
        )
    )


def generate_transactions_array(num_transactions: int = 10) -> npt.NDArray[Any]:
    transactions = [TransactionFactory() for _ in range(num_transactions)]
    return np.array(
        [
            [t.transaction_id, t.user_id, t.product_id, t.quantity, t.price, t.timestamp]
            for t in transactions
        ]
    )


def print_array(array: npt.NDArray[Any], message: str = "Array:") -> None:
    print(f"{message}\n\n\n{array}\n")


def calculate_total_revenue(data: npt.NDArray[Any]) -> float:
    quantities = data[:, 3].astype(float)
    prices = data[:, 4].astype(float)
    total_revenue: float = np.sum(quantities * prices)
    return total_revenue


def count_unique_users(data: npt.NDArray[Any]) -> int:
    unique_users = np.unique(data[:, 1])
    return len(unique_users)


def most_purchased_product(data: npt.NDArray[Any]) -> npt.NDArray[Any]:
    products, quantities = np.unique(data[:, 2], return_counts=True)
    max_index = np.argmax(quantities)
    return products[max_index]  # type: ignore[no-any-return]


def convert_price_to_int(data: npt.NDArray[Any]) -> npt.NDArray[Any]:
    data[:, 4] = data[:, 4].astype(float).astype(int)
    return data


def check_data_types(data: npt.NDArray[Any]) -> list[Any]:
    return [(i, type(data[0, i])) for i in range(data.shape[1])]


def product_quantity_array(data: npt.NDArray[Any]) -> npt.NDArray[Any]:
    return data[:, [2, 3]]


def user_transaction_count(data: npt.NDArray[Any]) -> npt.NDArray[Any]:
    users, counts = np.unique(data[:, 1], return_counts=True)
    return np.column_stack((users, counts))


def masked_array(data: npt.NDArray[Any]) -> npt.NDArray[Any]:
    mask = data[:, 3].astype(int) > 0
    return data[mask]


def increase_prices(data: npt.NDArray[Any], percentage: int) -> npt.NDArray[Any]:
    data[:, 4] = data[:, 4].astype(float) * (1 + percentage / 100)
    return data


def filter_transactions(data: npt.NDArray[Any]) -> npt.NDArray[Any]:
    return data[data[:, 3].astype(int) > 1]


def compare_revenue(
    data: npt.NDArray[Any], start_date: datetime.datetime, end_date: datetime.datetime
) -> float:
    start_date_np = np.datetime64(start_date)
    end_date_np = np.datetime64(end_date)
    mask = (data[:, 5] >= start_date_np) & (data[:, 5] <= end_date_np)
    filtered_data = data[mask]
    return calculate_total_revenue(filtered_data)


def user_transactions(data: npt.NDArray[Any], user_id: int) -> npt.NDArray[Any]:
    return data[data[:, 1] == user_id]  # type: ignore[no-any-return]


def date_range_slicing(
    data: npt.NDArray[Any], start_date: datetime.datetime, end_date: datetime.datetime
) -> npt.NDArray[Any]:
    start_date_np = np.datetime64(start_date)
    end_date_np = np.datetime64(end_date)
    mask = (data[:, 5] >= start_date_np) & (data[:, 5] <= end_date_np)
    return data[mask]


def top_products(data: npt.NDArray[Any]) -> npt.NDArray[Any]:
    unique_products = np.unique(data[:, 2])

    total_revenues = np.zeros(unique_products.shape)

    for i, product in enumerate(unique_products):
        product_mask = data[:, 2] == product
        product_data = data[product_mask]

        quantities = product_data[:, 3].astype(float)
        prices = product_data[:, 4].astype(float)
        total_revenues[i] = np.sum(quantities * prices)

    top_indices = np.argsort(total_revenues)[-5:]
    top_products = unique_products[top_indices]
    top_revenues = total_revenues[top_indices]

    return np.column_stack((top_products, top_revenues))


if __name__ == "__main__":
    transaction_data = generate_transactions_array(20)
    print_array(transaction_data, "Initial Transaction Data:")

    total_revenue = calculate_total_revenue(transaction_data)
    print(f"Total Revenue: {total_revenue}\n")

    unique_users = count_unique_users(transaction_data)
    print(f"Unique Users: {unique_users}\n")

    most_product = most_purchased_product(transaction_data)
    print(f"Most Purchased Product ID: {most_product}\n")

    transaction_data = convert_price_to_int(transaction_data)
    print_array(transaction_data, "Transaction Data after Converting Prices to Int:")

    data_types = check_data_types(transaction_data)
    print(f"Data Types: {data_types}\n")

    product_quantity = product_quantity_array(transaction_data)
    print_array(product_quantity, "Product and Quantity Array:")

    user_transactions_count = user_transaction_count(transaction_data)
    print_array(user_transactions_count, "User Transaction Count Array:")

    masked_data = masked_array(transaction_data)
    print_array(masked_data, "Masked Array (Excluding Quantity=0):")

    transaction_data = increase_prices(transaction_data, 5)
    print_array(transaction_data, "Transaction Data after 5% Price Increase:")

    filtered_transactions = filter_transactions(transaction_data)
    print_array(filtered_transactions, "Filtered Transactions (Quantity > 1):")

    revenue_period_1 = compare_revenue(
        transaction_data,
        datetime.datetime.now() - datetime.timedelta(weeks=4),
        datetime.datetime.now() - datetime.timedelta(weeks=2),
    )
    revenue_period_2 = compare_revenue(
        transaction_data,
        datetime.datetime.now() - datetime.timedelta(weeks=2),
        datetime.datetime.now(),
    )
    print(f"Revenue Comparison: Period 1: {revenue_period_1}, Period 2: {revenue_period_2}\n")

    user_specific_transactions = user_transactions(transaction_data, 101)
    print_array(user_specific_transactions[:, 0], "Transaction ids for User 101:")

    last_week = date_range_slicing(
        transaction_data,
        datetime.datetime.now() - datetime.timedelta(weeks=1),
        datetime.datetime.now(),
    )
    print_array(last_week[:, 0], "Date Range Sliced Data for the last week:")

    top_5_products = top_products(transaction_data)
    print_array(top_5_products, "Top 5 Products by Revenue:")

    assert transaction_data.shape[1] == 6, "Data array should have 6 columns."  # noqa: PLR2004
