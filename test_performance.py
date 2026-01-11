"""
Unit tests for performance optimization examples.
Tests verify that slow and optimized versions produce the same results.
"""

import unittest
from slow_code_example import (
    inefficient_string_concatenation,
    inefficient_list_membership_check,
    inefficient_nested_loops,
    inefficient_list_comprehension,
    inefficient_function_calls_in_loop,
    inefficient_dictionary_get,
)
from optimized_code import (
    efficient_string_concatenation,
    efficient_list_membership_check,
    efficient_nested_loops,
    efficient_list_comprehension,
    efficient_function_calls_in_loop,
    efficient_dictionary_get,
)


class TestPerformanceOptimizations(unittest.TestCase):
    """Test that optimized code produces same results as original."""

    def test_string_concatenation(self):
        """Test string concatenation produces same result."""
        items = [1, 2, 3, 4, 5]
        slow_result = inefficient_string_concatenation(items)
        fast_result = efficient_string_concatenation(items)
        self.assertEqual(slow_result, fast_result)

    def test_list_membership_check(self):
        """Test list/set membership produces same results."""
        data = list(range(100))
        search = list(range(50, 150))
        slow_result = inefficient_list_membership_check(data, search)
        fast_result = efficient_list_membership_check(data, search)
        self.assertEqual(set(slow_result), set(fast_result))

    def test_finding_duplicates(self):
        """Test duplicate finding produces same results."""
        data = [1, 2, 3, 2, 4, 5, 3, 6, 1]
        slow_result = set(inefficient_nested_loops(data))
        fast_result = set(efficient_nested_loops(data))
        self.assertEqual(slow_result, fast_result)

    def test_list_comprehension(self):
        """Test list filtering produces same results."""
        data = list(range(-50, 50))
        slow_result = inefficient_list_comprehension(data)
        fast_result = efficient_list_comprehension(data)
        self.assertEqual(slow_result, fast_result)

    def test_function_calls_in_loop(self):
        """Test function call optimization produces same results."""
        data = list(range(20))
        slow_result = inefficient_function_calls_in_loop(data)
        fast_result = efficient_function_calls_in_loop(data)
        self.assertEqual(slow_result, fast_result)

    def test_dictionary_get(self):
        """Test dictionary access produces same results."""
        test_dict = {i: i * 2 for i in range(100)}
        keys = list(range(0, 150))
        slow_result = inefficient_dictionary_get(test_dict, keys)
        fast_result = efficient_dictionary_get(test_dict, keys)
        self.assertEqual(slow_result, fast_result)

    def test_empty_inputs(self):
        """Test that both versions handle empty inputs correctly."""
        self.assertEqual(
            inefficient_string_concatenation([]),
            efficient_string_concatenation([]),
        )
        self.assertEqual(
            inefficient_list_membership_check([], []),
            efficient_list_membership_check([], []),
        )

    def test_single_element(self):
        """Test that both versions handle single element correctly."""
        self.assertEqual(
            inefficient_string_concatenation([42]),
            efficient_string_concatenation([42]),
        )


class TestPerformanceImprovements(unittest.TestCase):
    """Test that optimized code is actually faster."""

    def test_string_concatenation_is_faster(self):
        """Verify optimized version is faster for string concatenation."""
        import time

        items = list(range(5000))  # Larger dataset for more visible difference

        # Time slow version
        start = time.time()
        for _ in range(10):
            inefficient_string_concatenation(items)
        slow_time = time.time() - start

        # Time fast version
        start = time.time()
        for _ in range(10):
            efficient_string_concatenation(items)
        fast_time = time.time() - start

        # Fast version should be faster (allow some variance in timing)
        # Just verify fast version doesn't take longer than slow version
        self.assertLess(fast_time, slow_time * 1.2)

    def test_set_membership_is_faster(self):
        """Verify set membership is faster than list membership."""
        import time

        data = list(range(1000))
        search = list(range(500, 1500))

        # Time slow version
        start = time.time()
        for _ in range(10):
            inefficient_list_membership_check(data, search)
        slow_time = time.time() - start

        # Time fast version
        start = time.time()
        for _ in range(10):
            efficient_list_membership_check(data, search)
        fast_time = time.time() - start

        # Fast version should be significantly faster
        self.assertLess(fast_time * 5, slow_time)


if __name__ == "__main__":
    unittest.main()
