"""
Performance comparison script that runs both slow and optimized versions side-by-side.
This demonstrates the actual performance improvements achieved.
"""

import time
import sys
from slow_code_example import (
    inefficient_string_concatenation,
    inefficient_list_membership_check,
    inefficient_nested_loops,
    inefficient_list_comprehension,
    inefficient_global_variable_access,
    inefficient_function_calls_in_loop,
    inefficient_dictionary_get,
)
from optimized_code import (
    efficient_string_concatenation,
    efficient_list_membership_check,
    efficient_nested_loops,
    efficient_list_comprehension,
    efficient_global_variable_access,
    efficient_function_calls_in_loop,
    efficient_dictionary_get,
)


def benchmark_comparison(slow_func, fast_func, *args, iterations=100):
    """Compare performance of slow vs fast implementation."""
    # Benchmark slow version
    start = time.time()
    for _ in range(iterations):
        slow_func(*args)
    slow_time = (time.time() - start) / iterations

    # Benchmark fast version
    start = time.time()
    for _ in range(iterations):
        fast_func(*args)
    fast_time = (time.time() - start) / iterations

    # Calculate speedup
    speedup = slow_time / fast_time if fast_time > 0 else float("inf")

    return slow_time * 1000, fast_time * 1000, speedup


def print_comparison(name, slow_time, fast_time, speedup):
    """Print formatted comparison results."""
    print(f"\n{name}:")
    print(f"  Slow version: {slow_time:.4f} ms")
    print(f"  Fast version: {fast_time:.4f} ms")
    print(f"  Speedup: {speedup:.2f}x faster")
    print(f"  Improvement: {((speedup - 1) * 100):.1f}% faster")


def main():
    print("=" * 70)
    print("PERFORMANCE COMPARISON: SLOW vs OPTIMIZED CODE")
    print("=" * 70)

    # Constants
    DATA_MULTIPLIER = 100  # Multiplier to make test data larger for better benchmarking

    # Test data
    test_items = list(range(1000))
    test_search = list(range(500, 1500))
    test_duplicates = [1, 2, 3, 2, 4, 5, 3, 6, 1] * DATA_MULTIPLIER  # Make it bigger for better comparison
    test_numbers = list(range(-100, 100))
    test_dict = {i: i * 2 for i in range(1000)}
    test_keys = list(range(0, 1500))

    # 1. String concatenation
    slow, fast, speedup = benchmark_comparison(
        inefficient_string_concatenation, efficient_string_concatenation, test_items
    )
    print_comparison("1. String Concatenation", slow, fast, speedup)

    # 2. List membership check
    slow, fast, speedup = benchmark_comparison(
        inefficient_list_membership_check,
        efficient_list_membership_check,
        test_items,
        test_search,
    )
    print_comparison("2. List/Set Membership Check", slow, fast, speedup)

    # 3. Finding duplicates
    slow, fast, speedup = benchmark_comparison(
        inefficient_nested_loops, efficient_nested_loops, test_duplicates
    )
    print_comparison("3. Finding Duplicates", slow, fast, speedup)

    # 4. List comprehension with filtering
    slow, fast, speedup = benchmark_comparison(
        inefficient_list_comprehension, efficient_list_comprehension, test_numbers
    )
    print_comparison("4. List Filtering", slow, fast, speedup)

    # 5. Global variable access
    slow, fast, speedup = benchmark_comparison(
        inefficient_global_variable_access, efficient_global_variable_access
    )
    print_comparison("5. Global Variable Access", slow, fast, speedup)

    # 6. Function calls in loop
    slow, fast, speedup = benchmark_comparison(
        inefficient_function_calls_in_loop, efficient_function_calls_in_loop, test_items
    )
    print_comparison("6. Function Calls in Loop", slow, fast, speedup)

    # 7. Dictionary access
    slow, fast, speedup = benchmark_comparison(
        inefficient_dictionary_get, efficient_dictionary_get, test_dict, test_keys
    )
    print_comparison("7. Dictionary Access", slow, fast, speedup)

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(
        """
Key Takeaways:
1. Use str.join() instead of += for string concatenation
2. Use sets for membership testing instead of lists
3. Use Counter or set operations instead of nested loops
4. Combine filter operations into single pass
5. Cache global variables in local scope
6. Move invariant computations out of loops
7. Use dict.get() instead of try/except for missing keys

These optimizations can provide speedups ranging from 2x to 100x+
depending on the data size and operation type.
"""
    )


if __name__ == "__main__":
    main()
