"""
Example of slow and inefficient code patterns.
This file demonstrates common performance anti-patterns.
"""

import time


def inefficient_string_concatenation(items):
    """
    SLOW: Using += for string concatenation in a loop.
    Time Complexity: O(n²) due to string immutability.
    """
    result = ""
    for item in items:
        result += str(item) + ", "
    return result[:-2] if result else ""


def inefficient_list_membership_check(data, search_items):
    """
    SLOW: Using list for membership testing.
    Time Complexity: O(n*m) where n is len(data) and m is len(search_items).
    """
    found = []
    for item in search_items:
        if item in data:  # O(n) for each check
            found.append(item)
    return found


def inefficient_nested_loops(data):
    """
    SLOW: Unnecessary nested loops for duplicate finding.
    Time Complexity: O(n²).
    """
    duplicates = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j] and data[i] not in duplicates:
                duplicates.append(data[i])
    return duplicates


def inefficient_list_comprehension(data):
    """
    SLOW: Multiple passes over the same data.
    """
    # First pass to filter
    filtered = [x for x in data if x > 0]
    # Second pass to square
    squared = [x * x for x in filtered]
    # Third pass to filter again
    result = [x for x in squared if x > 100]
    return result


def inefficient_global_variable_access():
    """
    SLOW: Accessing global variables repeatedly in a loop.
    """
    global GLOBAL_COUNTER
    result = 0
    for i in range(10000):
        result += GLOBAL_COUNTER  # Global lookups are slower
    return result


GLOBAL_COUNTER = 5


def inefficient_function_calls_in_loop(data):
    """
    SLOW: Repeatedly calling expensive functions unnecessarily.
    """
    result = []
    for item in data:
        # len() is called every iteration unnecessarily
        if len(data) > 10:
            result.append(item * 2)
    return result


def inefficient_dictionary_get(dictionary, keys):
    """
    SLOW: Using try/except for dictionary access when default would work.
    """
    result = []
    for key in keys:
        try:
            result.append(dictionary[key])
        except KeyError:
            result.append(None)
    return result


def inefficient_file_operations():
    """
    SLOW: Opening and closing files multiple times.
    """
    data = ["line 1\n", "line 2\n", "line 3\n"]
    for line in data:
        # Opening file in each iteration is expensive
        with open("/tmp/example.txt", "a") as f:
            f.write(line)


# Benchmark function
def benchmark_function(func, *args, iterations=1000):
    """Helper function to benchmark code execution."""
    start = time.time()
    for _ in range(iterations):
        func(*args)
    end = time.time()
    return (end - start) / iterations


if __name__ == "__main__":
    # Test data
    test_items = list(range(1000))
    test_search = list(range(500, 1500))
    test_duplicates = [1, 2, 3, 2, 4, 5, 3, 6, 1]
    test_numbers = list(range(-100, 100))
    test_dict = {i: i * 2 for i in range(1000)}
    test_keys = list(range(0, 1500))

    print("=== Slow Code Benchmarks ===\n")

    # Benchmark string concatenation
    time_str = benchmark_function(
        inefficient_string_concatenation, test_items, iterations=100
    )
    print(f"String concatenation: {time_str*1000:.4f} ms")

    # Benchmark list membership
    time_list = benchmark_function(
        inefficient_list_membership_check, test_items, test_search, iterations=100
    )
    print(f"List membership check: {time_list*1000:.4f} ms")

    # Benchmark nested loops
    time_nested = benchmark_function(
        inefficient_nested_loops, test_duplicates, iterations=100
    )
    print(f"Nested loops for duplicates: {time_nested*1000:.4f} ms")

    # Benchmark multiple passes
    time_passes = benchmark_function(
        inefficient_list_comprehension, test_numbers, iterations=100
    )
    print(f"Multiple list passes: {time_passes*1000:.4f} ms")

    # Benchmark global access
    time_global = benchmark_function(inefficient_global_variable_access, iterations=100)
    print(f"Global variable access: {time_global*1000:.4f} ms")

    # Benchmark function calls in loop
    time_func = benchmark_function(
        inefficient_function_calls_in_loop, test_items, iterations=100
    )
    print(f"Redundant function calls: {time_func*1000:.4f} ms")

    # Benchmark dictionary get
    time_dict = benchmark_function(
        inefficient_dictionary_get, test_dict, test_keys, iterations=100
    )
    print(f"Dictionary access: {time_dict*1000:.4f} ms")
