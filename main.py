import random

def remove_duplicates(numbers):
    """
    Given a list of 10 numbers between 1 to 100, removes the duplicates and sorts the remaining numbers in descending order.

    here is my assumptions:

    The list of numbers is provided as a Python list object.
    The numbers in the list are between 1 and 100, inclusive.
    The list contains exactly 10 numbers.
    There are 4 duplicates in the list.
    """
    # Remove duplicates while preserving the order of the original list
    single_numbers = []
    for num in numbers:
        if num not in single_numbers:
            single_numbers.append(num)

    # Sort the unique list in descending order
    single_numbers.sort(reverse=True)

    return single_numbers



# Generate a list of 10 random integers between 1 and 100
numbers = [random.randint(1, 100) for _ in range(10)]

# Print the original list
print("Original list:", numbers)

# Remove duplicates and sort the remaining numbers in descending order
single_numbers = remove_duplicates(numbers)

# Print the result
print("Sorted list with duplicates removed:", single_numbers)
