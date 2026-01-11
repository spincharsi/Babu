"""
Optimized versions of the slow code examples.
This file demonstrates efficient alternatives to common anti-patterns.
"""

import time


def efficient_string_concatenation(items):
    """
    FAST: Using join() for string concatenation.
    Time Complexity: O(n) - single pass through data.
    Performance gain: 10-100x faster for large datasets.
    """
    return ", ".join(str(item) for item in items)


def efficient_list_membership_check(data, search_items):
    """
    FAST: Using set for membership testing.
    Time Complexity: O(n+m) where n is len(data) and m is len(search_items).
    Performance gain: Up to 1000x faster for large datasets.
    """
    data_set = set(data)  # O(n) to create set
    found = [item for item in search_items if item in data_set]  # O(1) per check
    return found


def efficient_nested_loops(data):
    """
    FAST: Using set operations or Counter for duplicate finding.
    Time Complexity: O(n).
    Performance gain: Can be 100x faster for large lists.
    """
    from collections import Counter

    counts = Counter(data)
    duplicates = [item for item, count in counts.items() if count > 1]
    return duplicates


def efficient_list_comprehension(data):
    """
    FAST: Single pass with combined filtering.
    Performance gain: 3x faster by reducing iterations.
    """
    # Single pass with all conditions
    result = [x * x for x in data if x > 0 and x * x > 100]
    return result


def efficient_global_variable_access():
    """
    FAST: Caching global variables in local scope.
    Performance gain: 2-3x faster due to faster local variable lookup.
    """
    global GLOBAL_COUNTER
    local_counter = GLOBAL_COUNTER  # Cache in local variable
    result = 0
    for i in range(10000):
        result += local_counter  # Local lookups are faster
    return result


GLOBAL_COUNTER = 5


def efficient_function_calls_in_loop(data):
    """
    FAST: Moving invariant computations out of loop.
    Performance gain: Significant speedup by avoiding redundant calls.
    """
    result = []
    data_length = len(data)  # Calculate once
    if data_length > 10:
        result = [item * 2 for item in data]
    return result


def efficient_dictionary_get(dictionary, keys):
    """
    FAST: Using dict.get() with default value.
    Performance gain: Cleaner and faster than try/except for missing keys.
    """
    return [dictionary.get(key, None) for key in keys]


def efficient_file_operations(file_path="/tmp/example.txt"):
    """
    FAST: Opening file once and performing all operations.
    Performance gain: Dramatically faster by minimizing I/O operations.
    
    Args:
        file_path: Path to write the file (default: /tmp/example.txt)
    """
    data = ["line 1\n", "line 2\n", "line 3\n"]
    # Open file once and write all data
    with open(file_path, "w") as f:
        f.writelines(data)


def efficient_list_filtering_with_filter(data, threshold):
    """
    FAST: Using filter() and generator expressions for large datasets.
    Memory efficient and faster for large data.
    """
    return list(filter(lambda x: x > threshold, data))


def efficient_loop_with_enumerate(data):
    """
    FAST: Using enumerate() instead of range(len()).
    More Pythonic and slightly faster.
    """
    result = []
    for idx, item in enumerate(data):
        if idx % 2 == 0:
            result.append(item)
    return result


def efficient_string_formatting(name, age, city):
    """
    FAST: Using f-strings (Python 3.6+) for string formatting.
    Performance gain: Faster and more readable than % or .format().
    """
    return f"Name: {name}, Age: {age}, City: {city}"


def efficient_avoid_repeated_attribute_lookup(data):
    """
    FAST: Caching method references in loops.
    """
    result = []
    append = result.append  # Cache the append method
    for item in data:
        append(item * 2)
    return result


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

    print("=== Optimized Code Benchmarks ===\n")

    # Benchmark string concatenation
    time_str = benchmark_function(efficient_string_concatenation, test_items, iterations=100)
    print(f"String concatenation: {time_str*1000:.4f} ms")

    # Benchmark set membership
    time_set = benchmark_function(
        efficient_list_membership_check, test_items, test_search, iterations=100
    )
    print(f"Set membership check: {time_set*1000:.4f} ms")

    # Benchmark Counter for duplicates
    time_counter = benchmark_function(
        efficient_nested_loops, test_duplicates, iterations=100
    )
    print(f"Counter for duplicates: {time_counter*1000:.4f} ms")

    # Benchmark single pass
    time_single = benchmark_function(
        efficient_list_comprehension, test_numbers, iterations=100
    )
    print(f"Single list pass: {time_single*1000:.4f} ms")

    # Benchmark local variable caching
    time_local = benchmark_function(efficient_global_variable_access, iterations=100)
    print(f"Cached local variable: {time_local*1000:.4f} ms")

    # Benchmark hoisted function calls
    time_hoisted = benchmark_function(
        efficient_function_calls_in_loop, test_items, iterations=100
    )
    print(f"Hoisted function calls: {time_hoisted*1000:.4f} ms")

    # Benchmark dict.get()
    time_get = benchmark_function(
        efficient_dictionary_get, test_dict, test_keys, iterations=100
    )
    print(f"Dictionary get: {time_get*1000:.4f} ms")
