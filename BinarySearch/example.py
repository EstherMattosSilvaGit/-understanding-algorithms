"""
Binary Search Algorithm Usage Example
Run this file to test the algorithm with predefined values.
You can modify all values below to experiment and learn how the algorithm works.

To run this file, use:
    python -m BinarySearch.example
"""

from BinarySearch.binarySearch import BinarySearch

# Create an instance of BinarySearch
search = BinarySearch()

# Sorted list of numbers to search in
# FEEL FREE TO MODIFY THIS LIST for testing
nums = [-1, 0, 3, 5, 9, 12]

print("=" * 50)
print("BINARY SEARCH EXAMPLES")
print("=" * 50)
print(f"\nList: {nums}\n")

# Example searches
examples = [
    (9, "number in the middle of the list"),
    (-1, "number at the beginning of the list"),
    (12, "number at the end of the list"),
    (4, "number that does NOT exist in the list"),
    (0, "number that exists in the list"),
]

for target, description in examples:
    result = search.search(nums, target)
    if result != -1:
        print(f"✓ Searching {target:3} ({description}): Found at index {result}")
    else:
        print(f"✗ Searching {target:3} ({description}): Not found (returns -1)")

print("\n" + "=" * 50)
print("Test with your own values:")
print("=" * 50)

# MODIFY THESE VALUES TO TEST THE ALGORITHM
# - Change 'my_nums' to any sorted list of numbers
# - Change 'my_target' to any number you want to search for
# Example: my_nums = [10, 20, 30, 40, 50] and my_target = 30
my_nums = [1, 3, 5, 7, 9, 11, 13, 15]
my_target = 7

result = search.search(my_nums, my_target)
print(f"\nList: {my_nums}")
print(f"Searching for: {my_target}")
print(f"Result: {'Found at index ' + str(result) if result != -1 else 'Not found'}")
