# Performance Optimization Guide

This repository demonstrates common performance issues in code and their optimized solutions.

## 📊 Performance Issues Identified and Fixed

### 1. String Concatenation in Loops
**Problem:** Using `+=` operator in loops creates new string objects each iteration due to string immutability.

**Slow Code (O(n²)):**
```python
result = ""
for item in items:
    result += str(item) + ", "
```

**Fast Code (O(n)):**
```python
result = ", ".join(str(item) for item in items)
```

**Performance Gain:** 10-100x faster for large datasets

---

### 2. List Membership Testing
**Problem:** Using `in` operator with lists requires O(n) scan for each lookup.

**Slow Code (O(n×m)):**
```python
for item in search_items:
    if item in data:  # O(n) lookup
        found.append(item)
```

**Fast Code (O(n+m)):**
```python
data_set = set(data)  # O(n) to create
found = [item for item in search_items if item in data_set]  # O(1) per lookup
```

**Performance Gain:** Up to 1000x faster for large datasets

---

### 3. Finding Duplicates with Nested Loops
**Problem:** Nested loops create O(n²) complexity.

**Slow Code (O(n²)):**
```python
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] == data[j]:
            duplicates.append(data[i])
```

**Fast Code (O(n)):**
```python
from collections import Counter
counts = Counter(data)
duplicates = [item for item, count in counts.items() if count > 1]
```

**Performance Gain:** 100x faster for large lists

---

### 4. Multiple Passes Over Data
**Problem:** Iterating over the same data multiple times.

**Slow Code:**
```python
filtered = [x for x in data if x > 0]
squared = [x * x for x in filtered]
result = [x for x in squared if x > 100]
```

**Fast Code:**
```python
result = [x * x for x in data if x > 0 and x * x > 100]
```

**Performance Gain:** 3x faster by reducing iterations

---

### 5. Global Variable Access in Loops
**Problem:** Global variable lookups are slower than local variable lookups.

**Slow Code:**
```python
for i in range(10000):
    result += GLOBAL_COUNTER  # Global lookup each time
```

**Fast Code:**
```python
local_counter = GLOBAL_COUNTER  # Cache in local variable
for i in range(10000):
    result += local_counter  # Local lookup
```

**Performance Gain:** 2-3x faster

---

### 6. Redundant Function Calls in Loops
**Problem:** Calling functions with unchanging results inside loops.

**Slow Code:**
```python
for item in data:
    if len(data) > 10:  # len() called every iteration
        result.append(item * 2)
```

**Fast Code:**
```python
data_length = len(data)  # Calculate once
if data_length > 10:
    result = [item * 2 for item in data]
```

**Performance Gain:** Significant speedup for expensive function calls

---

### 7. Dictionary Access with try/except
**Problem:** Using try/except for control flow is slower than dict.get().

**Slow Code:**
```python
try:
    value = dictionary[key]
except KeyError:
    value = None
```

**Fast Code:**
```python
value = dictionary.get(key, None)
```

**Performance Gain:** Cleaner and faster code

---

## 🚀 How to Run the Examples

### Run Slow Code Benchmark
```bash
python slow_code_example.py
```

### Run Optimized Code Benchmark
```bash
python optimized_code.py
```

### Run Side-by-Side Comparison
```bash
python performance_comparison.py
```

## 📈 Expected Results

Running the performance comparison should show significant improvements:

- String concatenation: **10-50x faster**
- Set membership: **100-1000x faster**
- Finding duplicates: **50-100x faster**
- Single-pass filtering: **2-3x faster**
- Local variable caching: **2-3x faster**
- Hoisted function calls: **Variable speedup**
- Dictionary get: **1.5-2x faster**

## 🔍 How to Identify Slow Code

### 1. Profiling Tools
- **cProfile**: Built-in Python profiler
  ```bash
  python -m cProfile -s cumtime your_script.py
  ```
- **line_profiler**: Line-by-line profiling
- **memory_profiler**: Track memory usage

### 2. Common Patterns to Watch For
- Nested loops (especially with large datasets)
- String concatenation in loops
- List operations where sets/dicts would be better
- Repeated calculations in loops
- Multiple iterations over the same data
- Excessive I/O operations
- Blocking operations without async/await

### 3. Big O Complexity Analysis
Always consider the time complexity:
- O(1) - Constant time (best)
- O(log n) - Logarithmic (very good)
- O(n) - Linear (good)
- O(n log n) - Linearithmic (acceptable)
- O(n²) - Quadratic (slow for large n)
- O(2ⁿ) - Exponential (very slow)

## 💡 General Optimization Tips

### 1. Use Built-in Functions
Python's built-in functions are implemented in C and are highly optimized.

### 2. Choose Right Data Structures
- **Lists**: Sequential access, ordered
- **Sets**: Membership testing, uniqueness
- **Dicts**: Key-value lookup
- **Deque**: Fast append/pop from both ends

### 3. Use List Comprehensions
List comprehensions are faster than equivalent for loops.

### 4. Avoid Premature Optimization
> "Premature optimization is the root of all evil" - Donald Knuth

Profile first, optimize only bottlenecks.

### 5. Use Generators for Large Datasets
Generators are memory-efficient for processing large amounts of data.

```python
# Memory efficient
def generate_numbers(n):
    for i in range(n):
        yield i * i
```

### 6. Cache Expensive Computations
Use `functools.lru_cache` for memoization:

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(n):
    # Expensive computation
    return result
```

## 🛠 Tools for Performance Analysis

1. **timeit**: Accurate timing of small code snippets
2. **cProfile**: Full program profiling
3. **py-spy**: Sampling profiler (no code changes needed)
4. **Scalene**: CPU, GPU, and memory profiler
5. **Pyflame**: Statistical profiler

## 📚 Additional Resources

- [Python Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
- [High Performance Python Book](https://www.oreilly.com/library/view/high-performance-python/9781492055013/)
- [Python Patterns Guide](https://python-patterns.guide/)

## 🎯 Key Takeaways

1. **Measure first**: Always profile before optimizing
2. **Choose right data structures**: Sets for lookups, lists for sequences
3. **Minimize iterations**: Single pass is better than multiple passes
4. **Cache computations**: Don't recalculate unchanged values
5. **Use built-ins**: They're optimized in C
6. **Consider Big O**: Algorithmic improvements beat micro-optimizations
7. **Test performance**: Always benchmark your optimizations

## 📝 Contributing

Feel free to add more examples of performance optimizations or suggest improvements to existing ones.
