# Python Data Structures, Algorithms, and Best Practices

## Terms
- **O(1)**: Constant time complexity.
- **O(n)**: Linear time complexity.
- **O(n log n)**: Linearithmic time complexity.
- **O(log n)**: Logarithmic time complexity.
- **O(n^2)**: Quadratic time complexity.
- **O(n!)**: Factorial time complexity.
- **Space Complexity**: Memory used by the algorithm.
- **DFS (Depth-First Search)**: Graph traversal algorithm.
- **BFS (Breadth-First Search)**: Graph traversal algorithm.
- **Dynamic Programming**: Optimization technique using overlapping subproblems.
- **Divide and Conquer**: Breaking problem into smaller subproblems and solving them independently.
- **Pivot Element**: The element around which a list is partitioned in Quick Sort.
- **Heuristic**: A function that estimates the cost of the cheapest path from a node to the goal.
- **Interned**: A method of storing only one copy of each distinct immutable value, which must be used in multiple places.
- **Arithmetic Summation**: The process of adding a sequence of numbers.
- **Brute Force**: A straightforward approach to solving a problem by trying all possible solutions until the correct one is found.
- **Dynamic Programming**: A method for solving complex problems by breaking them down into simpler subproblems and solving each subproblem just once, storing the solutions.
- **Prime Factorization**: The process of determining the prime numbers that multiply together to give a particular integer.
- **Sieve of Eratosthenes**: An ancient algorithm used to find all primes up to a specified integer.
- **Sliding Window**: A technique used to reduce the complexity of nested loops by using a fixed-size window that slides over the data structure.
- **Euclidean Algorithm**: An efficient method for computing the greatest common divisor (GCD) of two numbers.
- **Factorial**: The product of all positive integers less than or equal to a given positive integer.
- **Binomial Coefficient**: A coefficient of any of the terms in the expansion of the binomial theorem.
- **Memoization**: An optimization technique used to speed up computer programs by storing the results of expensive function calls.
- **Permutations**: Different ways of arranging a set of items.
- **Combinatorics**: The study of counting, arranging, and finding patterns in sets.
- **Palindrome**: A sequence of characters that reads the same backward as forward.
- **Least Common Multiple (LCM)**: The smallest positive integer that is divisible by both numbers.
- **Greatest Common Divisor (GCD)**: The largest positive integer that divides two numbers without leaving a remainder.
- **Reciprocal Cycle**: The repeating sequence of digits in the decimal representation of a fraction.
- **Triangle Number**: A number that can form an equilateral triangle. The nth triangle number is the sum of the first n natural numbers.
- **Pentagonal Number**: A number that can be arranged in the shape of a pentagon. The nth pentagonal number is given by the formula n(3n-1)/2.
- **Hexagonal Number**: A number that can be arranged in the shape of a hexagon. The nth hexagonal number is given by the formula n(2n-1).
- **Goldbach's Conjecture**: A conjecture stating that every even integer greater than 2 can be expressed as the sum of two primes.
- **Prime Checking**: The process of determining if a number is a prime number.
- **Arithmetic Sequence**: A sequence of numbers in which the difference between consecutive terms is constant.
- **Digit Manipulation**: Techniques involving the handling and manipulation of individual digits of numbers.
- **Factoradic Number System**: A mixed radix numeral system adapted to enumerating permutations.
- **Pythagorean Triplet**: A set of three positive integers a, b, and c, such that a^2 + b^2 = c^2.
- **Palindrome Check**: The process of verifying if a sequence is the same forward and backward.
- **Modulus Operation**: An operation that finds the remainder when one number is divided by another.
- **Recursion**: The process in which a function calls itself as a subroutine.
- **Backtracking**: A general algorithm for finding all solutions to some computational problems, notably constraint satisfaction problems.
- **Divisor Sum**: The sum of all positive divisors of a number.
- **Bitwise Operations**: Operations that directly manipulate bits of binary numbers.
- **Hashing**: The process of converting an input (or 'key') into a fixed-size string of bytes, typically for quick data retrieval.

## 1. Built-in Data Structures

### 1.1 Lists
- **Usage**: Ordered collection of items, supports indexing, slicing, and iteration.
- **Common Algorithms**:
  - **Sorting**:
    - **Quick Sort**: A fast, divide-and-conquer algorithm that selects a pivot element and partitions the array into subarrays. Average case O(n log n), worst case O(n^2), space complexity O(log n).
      - **Best Practices**: Use for general-purpose sorting, especially when average-case performance is more important than worst-case performance.
      - **Efficiency**: Most efficient when the pivot divides the list into balanced subarrays. Less efficient when the pivot results in highly unbalanced partitions.
      - **Edge Cases**: When the list is already sorted or contains many duplicate elements, leading to unbalanced partitions.
      - **Packages to Import**: None
      <details>
        <summary>Quick Sort Example</summary>

        ```python
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quick_sort(left) + middle + quick_sort(right)

        # Regular Implementation
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted_arr = quick_sort(arr) 
        print(sorted_arr)  # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

        # Best Practices Implementation: Using a cached version for repeated sorting
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def quick_sort_cached(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quick_sort_cached(tuple(left)) + tuple(middle) + quick_sort_cached(tuple(right))

        arr = tuple([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        sorted_arr = quick_sort_cached(arr)
        print(sorted_arr)  # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        ```

        **Worst-Case Example**: When the list is already sorted in ascending or descending order.
        ```python
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted_arr = quick_sort(arr)
        print(sorted_arr)  # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        ```
      </details>

    - **Merge Sort**: A stable, divide-and-conquer algorithm that divides the array into halves, sorts each half, and merges them. Time complexity O(n log n), space complexity O(n).
      - **Best Practices**: Use when a stable sort is required, and when working with large data sets that don't fit in memory (external sorting).
      - **Efficiency**: Most efficient for large datasets due to its stable time complexity. Less efficient due to higher space complexity.
      - **Edge Cases**: Lists with a large number of elements.
      - **Packages to Import**: None
      <details>
        <summary>Merge Sort Example</summary>

        ```python
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)
        
        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        # Regular Implementation
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_arr = merge_sort(arr)
         print(sorted_arr)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

        # Best Practices Implementation: Using a cached version for repeated sorting
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def merge_sort_cached(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort_cached(tuple(arr[:mid]))
            right = merge_sort_cached(tuple(arr[mid:]))
            return merge(left, right)

        arr = tuple([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        sorted_arr = merge_sort_cached(arr)
        print(sorted_arr)  # Output: (1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9)
        ```

        **Worst-Case Example**: Large lists with complex data structures.
        ```python
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_arr = merge_sort(arr)
        ```
      </details>

    - **Tim Sort**: A hybrid sorting algorithm derived from merge sort and insertion sort, used by Python's built-in `sorted()` function. Time complexity O(n log n), space complexity O(n).
      - **Best Practices**: Use for general-purpose sorting, especially when stability and performance are crucial.
      - **Efficiency**: Most efficient for real-world data, which often contains runs of ordered elements. Less efficient in scenarios with highly random data.
      - **Edge Cases**: Lists with a mix of ordered and unordered segments.
      - **Packages to Import**: None
      <details>
        <summary>Tim Sort Example</summary>

        ```python
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_arr = sorted(arr)  # Uses Tim Sort internally
        print(sorted_arr)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

        # Regular Implementation
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_arr = sorted(arr)
        print(sorted_arr)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

        # Best Practices Implementation: Sorting large datasets with multiple runs
        large_arr = [i % 10 for i in range(1000000)]
        sorted_large_arr = sorted(large_arr)
        print(sorted_large_arr[:10])  # Output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ```

        **Worst-Case Example**: Highly random or pathological data sequences.
        ```python
        arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        sorted_arr = sorted(arr)
        print(sorted_arr)  # Output: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        ```
      </details>


  - **Searching**:
    - **Linear Search**: A simple search algorithm that checks each element until the target is found. Time complexity O(n), space complexity O(1).
      - **Best Practices**: Use for small or unsorted datasets.
      - **Efficiency**: Most efficient for small datasets. Less efficient for large datasets.
      - **Edge Cases**: When the target element is not in the list or at the end of the list.
      - **Packages to Import**: None
      <details>
        <summary>Linear Search Example</summary>

        ```python
        def linear_search(arr, target):
            for i in range(len(arr)):
                if arr[i] == target:
                    return i
            return -1

        # Regular Implementation
        arr = [1, 2, 3, 4, 5]
        index = linear_search(arr, 6)
        print(index)  # Output: -1

        # Best Practices Implementation: Implementing a linear search with early stopping
        def linear_search_early_stop(arr, target):
            for i in range(len(arr)):
                if arr[i] == target:
                    return i
                if arr[i] > target:
                    return -1
            return -1

        arr = [1, 2, 3, 4, 5]
        index = linear_search_early_stop(arr, 6)
        print(index)  # Output: -1
        ```

        **Worst-Case Example**: Target element not present in the list.
        ```python
        arr = [1, 2, 3, 4, 5]
        index = linear_search(arr, 6)
        print(index)  # Output: -1
        ```
      </details>

    - **Binary Search**: An efficient search algorithm that works on sorted arrays by repeatedly dividing the search interval in half. Time complexity O(log n), space complexity O(1).
      - **Best Practices**: Use for large, sorted datasets.
      - **Efficiency**: Most efficient for large, sorted datasets. Less efficient for unsorted datasets.
      - **Edge Cases**: When the target element is not in the list.
      - **Packages to Import**: None
      <details>
        <summary>Binary Search Example</summary>

        ```python
        def binary_search(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        # Regular Implementation
        arr = [1, 2, 3, 4, 5]
        index = binary_search(arr, 6)
        print(index)  # Output: -1

        # Best Practices Implementation: Using a recursive binary search with memoization
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def binary_search_recursive(arr, left, right, target):
            if right >= left:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    return binary_search_recursive(arr, left, mid - 1, target)
                else:
                    return binary_search_recursive(arr, mid + 1, right, target)
            else:
                return -1

        arr = tuple([1, 2, 3, 4, 5])
        index = binary_search_recursive(arr, 0, len(arr) - 1, 6)
        print(index)  # Output: -1
        ```

        **Worst-Case Example**: Target element not present in the list.
        ```python
        arr = [1, 2, 3, 4, 5]
        index = binary_search(arr, 6)
        print(index)  # Output: -1
        ```
      </details>

  - **Best Practices**: Use list comprehensions for concise and readable code; avoid excessive appending in loops for large data to improve performance.
    - **Packages to Import**: None
    <details>
      <summary>Best Practices Example</summary>

      ```python
      squares = [x**2 for x in range(10)]  # List comprehension for concise code
      print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
      ```
    </details>
  
  - **Thread-Safe Implementation**: Using threading.Lock
    - **Packages to Import**: threading 
    <details>
      <summary>Thread-Safe Implementation Example</summary>

      ```python
      from threading import Lock, Thread
      import time

      lock = Lock()
      shared_list = []

      def add_to_list(value):
          with lock:
              time.sleep(0.1)  # Simulate I/O-bound task
              shared_list.append(value)

      threads = [Thread(target=add_to_list, args=(i,)) for i in range(5)]
      for t in threads:
          t.start()
      for t in threads:
          t.join()

      print("Final List:", shared_list)  # Output: Final List: [0, 1, 2, 3, 4]
      ```
    </details>

### 1.2 Tuples
- **Usage**: Immutable ordered collection of items.
- **Common Algorithms**:
  - **Hashing**: Often used as keys in dictionaries because they are immutable. O(1) average, O(n) worst-case time complexity for lookup, O(1) space complexity.
    - **Best Practices**: Use tuples as keys in dictionaries and sets when the data needs to be immutable.
    - **Efficiency**: Most efficient for small, immutable collections. Less efficient for large, mutable collections.
    - **Edge Cases**: Large tuples with complex data structures.
    - **Packages to Import**: None
    <details>
      <summary>Hashing Example</summary>

      ```python
      person_info = {("John", "Doe"): 12345, ("Jane", "Smith"): 67890}

      # Regular Implementation
      person_info = {("John", "Doe"): 12345, ("Jane", "Smith"): 67890}
      print(person_info)  # Output: {('John', 'Doe'): 12345, ('Jane', 'Smith'): 67890}

      # Best Practices Implementation: Using a namedtuple for readability
      from collections import namedtuple

      Person = namedtuple('Person', ['first_name', 'last_name'])
      person_info = {Person("John", "Doe"): 12345, Person("Jane", "Smith"): 67890}
      print(person_info)  # Output: {Person(first_name='John', last_name='Doe'): 12345, Person(first_name='Jane', last_name='Smith'): 67890}
      ```

      **Worst-Case Example**: Large tuples as dictionary keys.
      ```python
      large_tuple = tuple(range(1000000))
      person_info = {large_tuple: 12345}
      print(person_info)  # Output: {(0, 1, 2, ..., 999999): 12345}
      ```
    </details>
  - **Best Practices**: Use for fixed collections of related items; prefer over lists for read-only purposes to ensure data integrity.
    - **Packages to Import**: None
    <details>
      <summary>Best Practices Example</summary>

      ```python
      coordinates = (10, 20)  # Tuple for fixed coordinates
      print(coordinates)  # Output: (10, 20)
      ```
  - **Thread-Safe Implementation**: Using threading.Lock
    - **Packages to Import**: threading 
    <details>
      <summary>Thread-Safe Implementation Example</summary>

      ```python
      from threading import Lock, Thread
      import time

      lock = Lock()
      shared_tuple = (0,)

      def add_to_tuple(value):
          global shared_tuple
          with lock:
              time.sleep(0.1)  # Simulate I/O-bound task
              shared_tuple += (value,)

      threads = [Thread(target=add_to_tuple, args=(i,)) for i in range(5)]
      for t in threads:
          t.start()
      for t in threads:
          t.join()

      print("Final Tuple:", shared_tuple)  # Output: Final Tuple: (0, 1, 2, 3, 4)

      ```
    </details>

    
### 1.3 Dictionaries
- **Usage**: Key-value pairs, efficient lookup, insertion, and deletion.
- **Common Algorithms**:
  - **Hashing**: Dictionary operations (insert, lookup) typically O(1) average case due to hash tables, O(n) worst-case time complexity, O(n) space complexity.
    - **Best Practices**: Use for fast lookups and insertions, and when the data structure needs to be dynamic.
    - **Efficiency**: Most efficient for operations involving key-value pairs. Less efficient when there are frequent collisions in the hash table.
    - **Edge Cases**: Large dictionaries with many collisions.
    - **Packages to Import**: None
    <details>
      <summary>Hashing Example</summary>

      ```python
      phone_book = {"Alice": "123-456-7890", "Bob": "987-654-3210"}
      print(phone_book)  # Output: {'Alice': '123-456-7890', 'Bob': '987-654-3210'}

      # Regular Implementation
      phone_book = {"Alice": "123-456-7890", "Bob": "987-654-3210"}
      print(phone_book)  # Output: {'Alice': '123-456-7890', 'Bob': '987-654-3210'}

      # Best Practices Implementation: Using defaultdict for safe access to dictionary values
      from collections import defaultdict

      phone_book = defaultdict(lambda: 'Number not found', {"Alice": "123-456-7890", "Bob": "987-654-3210"})
      print(phone_book["Alice"])  # Output: 123-456-7890
      print(phone_book["Charlie"])  # Output: Number not found
      ```

      **Worst-Case Example**: Large dictionaries with many collisions.
      ```python
      large_dict = {i: i for i in range(1000000)}
      value = large_dict[999999]
      print(value)  # Output: 999999
      ```
    </details>
  - **Best Practices**: Use dictionary comprehensions; ensure keys are immutable types.
    - **Packages to Import**: None
    <details>
      <summary>Best Practices Example</summary>

      ```python
      squares = {x: x**2 for x in range(10)}  # Dictionary comprehension
      print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
      ```
    </details>

  - **Thread-Safe Implementation**: Using threading.Lock
    - **Packages to Import**: threading 
    <details>
      <summary>Thread-Safe Implementation Example</summary>

      ```python
      from threading import Lock, Thread
      import time

      lock = Lock()
      shared_dict = {}

      def update_dict(key, value):
          with lock:
              time.sleep(0.1)  # Simulate I/O-bound task
              shared_dict[key] = value

      threads = [Thread(target=update_dict, args=(i, i * 10)) for i in range(5)]
      for t in threads:
          t.start()
      for t in threads:
          t.join()

      print("Final Dictionary:", shared_dict)  # Output: Final Dictionary: {0: 0, 1: 10, 2: 20, 3: 30, 4: 40}
      ```
    </details>


### 1.4 Sets
- **Usage**: Unordered collection of unique items.
- **Common Algorithms**:
  - **Set Operations**: Union, Intersection, Difference (all O(1) average case, O(n) worst-case time complexity, O(n) space complexity).
    - **Best Practices**: Use sets to eliminate duplicates and perform membership tests efficiently.
    - **Efficiency**: Most efficient for operations involving unique elements. Less efficient when handling large datasets with frequent insertions and deletions.
    - **Edge Cases**: Large sets with many duplicates.
    - **Packages to Import**: None
    <details>
      <summary>Set Operations Example</summary>

      ```python
      set_a = {1, 2, 3, 4}
      set_b = {3, 4, 5, 6}
      union = set_a | set_b  # Union
      intersection = set_a & set_b  # Intersection
      difference = set_a - set_b  # Difference
      print(union)  # Output: {1, 2, 3, 4, 5, 6}
      print(intersection)  # Output: {3, 4}
      print(difference)  # Output: {1, 2}

      # Regular Implementation
      set_a = {1, 2, 3, 4}
      set_b = {3, 4, 5, 6}
      union = set_a | set_b
      intersection = set_a & set_b
      difference = set_a - set_b
      print(union)  # Output: {1, 2, 3, 4, 5, 6}
      print(intersection)  # Output: {3, 4}
      print(difference)  # Output: {1, 2}

      # Best Practices Implementation: Using set methods for better readability
      set_a = {1, 2, 3, 4}
      set_b = {3, 4, 5, 6}
      union = set_a.union(set_b)
      intersection = set_a.intersection(set_b)
      difference = set_a.difference(set_b)
      print(union)  # Output: {1, 2, 3, 4, 5, 6}
      print(intersection)  # Output: {3, 4}
      print(difference)  # Output: {1, 2}
      ```

      **Worst-Case Example**: Large sets with many duplicates.
      ```python
      large_set_a = set(range(1000000))
      large_set_b = set(range(500000, 1500000))
      union = large_set_a | large_set_b
      print(len(union))  # Output: 1500000
      ```
    </details>
  - **Best Practices**: Use sets to eliminate duplicates and perform membership tests efficiently.
    - **Packages to Import**: None
    <details>
      <summary>Best Practices Example</summary>

      ```python
      unique_numbers = set([1, 2, 2, 3, 4])  # Set to eliminate duplicates
      print(unique_numbers)  # Output: {1, 2, 3, 4}
      ```
    </details>

  - **Thread-Safe Implementation**: Using threading.Lock
    - **Packages to Import**: threading 
    <details>
      <summary>Thread-Safe Implementation Example</summary>

      ```python
      from threading import Lock, Thread
      import time

      lock = Lock()
      shared_set = set()

      def add_to_set(value):
          with lock:
              time.sleep(0.1)  # Simulate I/O-bound task
              shared_set.add(value)

      threads = [Thread(target=add_to_set, args=(i,)) for i in range(5)]
      for t in threads:
          t.start()
      for t in threads:
          t.join()

      print("Final Set:", shared_set)  # Output: Final Set: {0, 1, 2, 3, 4}
      ```
    </details>


## 2. Collections Module

### 2.1 deque (Double-ended queue)
- **Usage**: Supports O(1) append and pop operations from both ends.
- **Common Algorithms**:
  - **Sliding Window**: Useful in problems involving a moving window of elements. O(n) time complexity, O(k) space complexity.
    - **Best Practices**: Use for implementing queues and sliding window problems.
    - **Efficiency**: Most efficient for operations requiring quick access to both ends of the deque. Less efficient when random access is required.
    - **Edge Cases**: Large deques with frequent operations on both ends.
    - **Packages to Import**: `from collections import deque`
    <details>
      <summary>max_sliding_window</summary>

      ```python
      from collections import deque

      def max_sliding_window(nums, k):
          dq = deque()
          result = []
          for i, num in enumerate(nums):
              if dq and dq[0] == i - k:
                  dq.popleft()
              while dq and nums[dq[-1]] < num:
                  dq.pop()
              dq.append(i)
              if i >= k - 1:
                  result.append(nums[dq[0]])
          return result

      # Regular Implementation
      nums = [i for i in range(100)]
      k = 10
      max_values = max_sliding_window(nums, k)
      print(max_values)  # Output: [9, 19, 29, 39, 49, 59, 69, 79, 89, 99]

      # Best Practices Implementation: Using a pre-allocated deque
      def max_sliding_window_optimized(nums, k):
          dq = deque(maxlen=k)
          result = []
          for i, num in enumerate(nums):
              if dq and dq[0] == i - k:
                  dq.popleft()
              while dq and nums[dq[-1]] < num:
                  dq.pop()
              dq.append(i)
              if i >= k - 1:
                  result.append(nums[dq[0]])
          return result

      nums = [i for i in range(100)]
      k = 10
      max_values = max_sliding_window_optimized(nums, k)
      print(max_values)  # Output: [9, 19, 29, 39, 49, 59, 69, 79, 89, 99]
      ```

      **Worst-Case Example**: Large sliding windows with frequent maximum updates.
      ```python
      nums = [i for i in range(100000)]
      k = 50000
      max_values = max_sliding_window(nums, k)
      print(max_values)  # Output: [9, 19, 29, 39, 49, 59, 69, 79, 89, 99]
      ```
    </details>
  - **Best Practices**: Use `deque` for queue-like operations to avoid O(n) operations of lists.
    - **Packages to Import**: `from collections import deque`
    <details>
      <summary>Best Practices Example</summary>

      ```python
      dq = deque([1, 2, 3])
      dq.appendleft(0)
      dq.append(4)
      print(dq)  # Output: deque([0, 1, 2, 3, 4])
      ```
    </details>

### 2.2 Counter
- **Usage**: Count the frequency of elements.
- **Common Algorithms**:
  - **Frequency Analysis**: Counting occurrences in strings, lists. O(n) time complexity, O(n) space complexity.
    - **Best Practices**: Use for tallying elements and counting frequencies.
    - **Efficiency**: Most efficient for counting elements in a dataset. Less efficient when dealing with large datasets with high element diversity.
    - **Edge Cases**: Large texts or lists with many unique elements.
    - **Packages to Import**: `from collections import Counter`
    <details>
      <summary>Frequency Analysis Example</summary>

      ```python
      from collections import Counter

      text = "hello world"
      count = Counter(text)
      print(count)  # Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})


      # Regular Implementation
      text = "hello world"
      count = Counter(text)
      print(count)  # Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

      # Best Practices Implementation: Using Counter with defaultdict for missing values
      from collections import defaultdict, Counter

      text = "hello world"
      count = Counter(text)
      default_count = defaultdict(int, count)
      print(default_count['h'])  # Output: 1
      print(default_count['z'])  # Output: 0
      ```

      **Worst-Case Example**: Large texts with many unique characters.
      ```python
      large_text = "a" * 1000000
      count = Counter(large_text)
      print(count)  # Output: Counter({'a': 1000000})
      ```
    </details>
  - **Best Practices**: Use `Counter` for tallying elements; supports most common operations directly.
    - **Packages to Import**: `from collections import Counter`
    <details>
      <summary>Best Practices Example</summary>

      ```python
      elements = [1, 2, 2, 3, 3, 3]
      counter = Counter(elements)
      print(counter)  # Output: Counter({3: 3, 2: 2, 1: 1})
      ```
    </details>

  - **Thread-Safe Implementation**: Using threading.Lock
    - **Packages to Import**: collections, threading 
    <details>
      <summary>Thread-Safe Implementation Example</summary>

      ```python
      from collections import Counter
      from threading import Lock, Thread
      import time

      lock = Lock()
      shared_counter = Counter()

      def update_counter(values):
          with lock:
              time.sleep(0.1)  # Simulate I/O-bound task
              shared_counter.update(values)

      threads = [Thread(target=update_counter, args=([1, 2, 3, 1],)) for _ in range(3)]
      for t in threads:
          t.start()
      for t in threads:
          t.join()

      print("Final Counter:", shared_counter)  # Output: Final Counter: Counter({1: 6, 2: 3, 3: 3})
      ```
    </details>


### 2.3 defaultdict
- **Usage**: Dictionary with default values for non-existing keys.
- **Common Algorithms**:
  - **Grouping**: Aggregating data under a common key. O(n) time complexity, O(n) space complexity.
    - **Best Practices**: Simplifies code by avoiding key existence checks.
    - **Efficiency**: Most efficient for grouping data under common keys. Less efficient for large datasets with sparse keys.
    - **Edge Cases**: Large lists of key-value pairs.
    - **Packages to Import**: `from collections import defaultdict`
    <details>
      <summary>Grouping Example</summary>

      ```python
      from collections import defaultdict

      def group_by_key(pairs):
          d = defaultdict(list)
          for key, value in pairs:
              d[key].append(value)
          return dict(d)

      # Regular Implementation
      pairs = [('a', 1), ('b', 2), ('a', 3)]
      grouped = group_by_key(pairs)
      print(grouped)  # Output: {'a': [1, 3], 'b': [2]}

      # Best Practices Implementation: Using defaultdict with default factory for missing keys
      from collections import defaultdict

      def group_by_key_optimized(pairs):
          d = defaultdict(list)
          for key, value in pairs:
              d[key].append(value)
          return d

      pairs = [('a', 1), ('b', 2), ('a', 3)]
      grouped = group_by_key_optimized(pairs)
      print(grouped['a'])  # Output: [1, 3]
      print(grouped['b'])  # Output: [2]
      print(grouped['c'])  # Output: []
      ```

      **Worst-Case Example**: Large lists of key-value pairs with many unique keys.
      ```python
      pairs = [(i % 1000, i) for i in range(1000000)]
      grouped = group_by_key(pairs)
      print(len(grouped))  # Output: 1000
      ```
    </details>
  - **Best Practices**: Simplifies code by avoiding key existence checks.
    - **Packages to Import**: `from collections import defaultdict`
    <details>
      <summary>Best Practices Example</summary>

      ```python
      word_lengths = defaultdict(int)
      for word in ["hello", "world"]:
          word_lengths[word] += len(word)

      print(word_lengths)  # Output: defaultdict(<class 'int'>, {'hello': 5, 'world': 5})
      ```
    </details>

  - **Thread-Safe Implementation**: Using threading.Lock
    - **Packages to Import**: collections, threading 
    <details>
      <summary>Thread-Safe Implementation Example</summary>

      ```python
      from collections import defaultdict
      from threading import Lock, Thread
      import time

      lock = Lock()
      shared_defaultdict = defaultdict(int)

      def increment_key(key):
          with lock:
              time.sleep(0.1)  # Simulate I/O-bound task
              shared_defaultdict[key] += 1

      threads = [Thread(target=increment_key, args=('a',)) for _ in range(5)]
      for t in threads:
          t.start()
      for t in threads:
          t.join()

      print("Final defaultdict:", dict(shared_defaultdict))  # Output: Final defaultdict: {'a': 5}
      ```
    </details>


### 2.4 OrderedDict
- **Usage**: Dictionary that remembers the order in which items were inserted.
- **Common Algorithms**:
  - **Maintaining Order**: Useful in applications where the order of items matters. O(n) time complexity for most operations, O(n) space complexity.
    - **Best Practices**: Use when insertion order needs to be maintained.
    - **Efficiency**: Most efficient for maintaining order of items. Less efficient when order is not important.
    - **Edge Cases**: Large dictionaries with many insertions and deletions.
    - **Packages to Import**: `from collections import OrderedDict`
    <details>
      <summary>Maintaining Order Example</summary>

      ```python
      from collections import OrderedDict

      d = OrderedDict()
      d['one'] = 1
      d['two'] = 2
      d['three'] = 3
      print(d)  # Output: OrderedDict([('one', 1), ('two', 2), ('three', 3)])

      # Regular Implementation
      d = OrderedDict()
      d['one'] = 1
      d['two'] = 2
      d['three'] = 3
      print(d)  # Output: OrderedDict([('one', 1), ('two', 2), ('three', 3)])

      # Best Practices Implementation: Using OrderedDict for ordered traversal
      d = OrderedDict()
      d['one'] = 1
      d['two'] = 2
      d['three'] = 3
      for key in d:
          print(key, d[key])

      # Output:
      # one 1
      # two 2
      # three 3
      ```

      **Worst-Case Example**: Large OrderedDict with many insertions and deletions.
      ```python
      large_d = OrderedDict()
      for i in range(1000000):
          large_d[i] = i

      print(large_d[999999])  # Output: 999999
      ```
    </details>
  - **Best Practices**: Use when insertion order needs to be maintained.
    - **Packages to Import**: `from collections import OrderedDict`
    <details>
      <summary>Best Practices Example</summary>

      ```python
      d = OrderedDict([('one', 1), ('two', 2), ('three', 3)])

      print(d)  # Output: OrderedDict([('one', 1), ('two', 2), ('three', 3)])
      ```
    </details>

  - **Thread-Safe Implementation**: Using threading.Lock
    - **Packages to Import**: collections, threading 
    <details>
      <summary>Thread-Safe Implementation Example</summary>

      ```python
      from collections import OrderedDict
      from threading import Lock, Thread
      import time

      lock = Lock()
      shared_ordered_dict = OrderedDict()

      def update_ordered_dict(key, value):
          with lock:
              time.sleep(0.1)  # Simulate I/O-bound task
              shared_ordered_dict[key] = value

      threads = [Thread(target=update_ordered_dict, args=(chr(97 + i), i)) for i in range(5)]
      for t in threads:
          t.start()
      for t in threads:
          t.join()

      print("Final OrderedDict:", shared_ordered_dict)  # Output: Final OrderedDict: OrderedDict([('a', 0), ('b', 1), ...])
      ```
    </details>


### 2.5 Sliding Window
- **Description**: A technique used to reduce the complexity of nested loops by using a fixed-size window that slides over the data structure.
- **Common Algorithms**:
  - **Maximum in Sliding Window**: Find the maximum value in each sliding window of size k in the array. O(n) time complexity, O(k) space complexity.
    - **Best Practices**: Use for problems involving a moving window of elements.
    - **Efficiency**: Most efficient for operations requiring quick access to both ends of the deque. Less efficient when random access is required.
    - **Edge Cases**: Large sliding windows with frequent updates.
    - **Packages to Import**: `from collections import deque`
    <details>
      <summary>max_sliding_window</summary>

      ```python
      from collections import deque

      def max_sliding_window(nums, k):
          dq = deque()
          result = []
          for i, num in enumerate(nums):
              if dq and dq[0] == i - k:
                  dq.popleft()
              while dq and nums[dq[-1]] < num:
                  dq.pop()
              dq.append(i)
              if i >= k - 1:
                  result.append(nums[dq[0]])
          return result

      # Example Implementation
      nums = [1, 3, -1, -3, 5, 3, 6, 7]
      k = 3
      max_values = max_sliding_window(nums, k)
      print(max_values)  # Output: [3, 3, 5, 5, 6, 7]
      ```

      **Worst-Case Example**: Large sliding windows with frequent maximum updates.
      ```python
      nums = [i for i in range(100000)]
      k = 50000
      max_values = max_sliding_window(nums, k)
      ```
    </details>

  - **Minimum in Sliding Window**: Find the minimum value in each sliding window of size k in the array. O(n) time complexity, O(k) space complexity.
    - **Best Practices**: Use for problems involving a moving window of elements.
    - **Efficiency**: Most efficient for operations requiring quick access to both ends of the deque. Less efficient when random access is required.
    - **Edge Cases**: Large sliding windows with frequent updates.
    - **Packages to Import**: `from collections import deque`
    <details>
      <summary>min_sliding_window</summary>

      ```python
      from collections import deque

      def min_in_sliding_window(arr, k):
          """
          Finds the minimum value in each sliding window of size k.
          :param arr: List[int], the input array
          :param k: int, the size of the sliding window
          :return: List[int], the minimums in each window
          """
          n = len(arr)
          if n == 0 or k == 0:
              return []
          if k > n:
              raise ValueError("Window size k cannot be greater than the array size.")
          
          dq = deque()  # To store indices of elements
          result = []

          for i in range(n):
              # Remove indices of elements not in the current window
              if dq and dq[0] < i - k + 1:
                  dq.popleft()

              # Remove elements larger than the current one (they won't be needed)
              while dq and arr[dq[-1]] > arr[i]:
                  dq.pop()

              # Add the current element's index to the deque
              dq.append(i)

              # Append the minimum for the current window to the result
              if i >= k - 1:
                  result.append(arr[dq[0]])

          return result

      # Example Usage
      array = [10, 4, 2, 7, 8, 3, 6, 1]
      window_size = 3
      print("Minimum in Sliding Window:", min_in_sliding_window(array, window_size)) # Minimum in Sliding Window: [2, 2, 2, 3, 3, 1]
      ```

  - **Sum of a Subarray**: Calculate the sum of all subarrays of size 𝑘k in a given array using the sliding window technique. O(n) time complexity, O(k) space complexity.
    - **Best Practices**: Use for problems involving a moving window of elements.
    - **Efficiency**: Most efficient for operations requiring quick access to both ends of the deque. Less efficient when random access is required.
    - **Edge Cases**: Large sliding windows with frequent updates.
    - **Packages to Import**: `from collections import deque` or regular array
    <details>
      <summary>sum_of_subarray with array</summary>

      ```python
        def sum_of_subarray(array, k):
            if k > len(array):
                raise ValueError("Window size k cannot be larger than the array size.")
            
            result = []
            window_sum = sum(array[:k])  # Initial window sum
            result.append(window_sum)

            for i in range(k, len(array)):
                window_sum += array[i] - array[i - k]
                result.append(window_sum)

            return result

        # Example usage
        array = [1, 2, 3, 4, 5]
        k = 3
        print("Sum of Subarray:", sum_of_subarray(array, k)) # Sum of Subarray: [6, 9, 12]

      ```
    </details> 
    <details>
      <summary>sum_of_subarray with deque</summary>

      ```python
      from collections import deque

      def sum_of_subarray_with_deque(array, k):
          if k > len(array):
              raise ValueError("Window size k cannot be larger than the array size.")
          
          result = []
          window_sum = 0
          dq = deque()

          for i in range(len(array)):
              window_sum += array[i]
              dq.append(array[i])

              # Maintain the size of the deque
              if len(dq) > k:
                  window_sum -= dq.popleft()
              
              if len(dq) == k:
                  result.append(window_sum)

          return result

      # Example usage
      array = [1, 2, 3, 4, 5]
      k = 3
      print("Sum of Subarray with Deque:", sum_of_subarray_with_deque(array, k))  # Sum of Subarray with Deque: [6, 9, 12]

      ```
    </details>    

  - **Longest Substring Without Repeating Characters**: Find the length of the longest substring without repeating characters using a sliding window. O(n) time complexity, O(k) space complexity.
    - **Best Practices**: Use for problems involving a moving window of elements.
    - **Efficiency**: Most efficient for operations requiring quick access to both ends of the deque. Less efficient when random access is required.
    - **Edge Cases**: Large sliding windows with frequent updates.
    - **Packages to Import**: `from collections import deque` or regular array
    <details>
      <summary>longest_substring_without_repeating with array</summary>

      ```python
      def longest_substring_without_repeating(s):
          char_index_map = {}
          start = 0
          max_length = 0

          for end in range(len(s)):
              if s[end] in char_index_map:
                  start = max(start, char_index_map[s[end]] + 1)  # Move start if duplicate found
              char_index_map[s[end]] = end  # Update character index
              max_length = max(max_length, end - start + 1)

          return max_length

      # Example usage
      s = "abcabcbb"
      print("Longest Substring Without Repeating Characters:", longest_substring_without_repeating(s)) # Longest Substring Without Repeating Characters: 3

      ```
    </details> 
    <details>
      <summary>longest_substring_without_repeating with deque</summary>

      ```python
      from collections import deque

      def longest_substring_without_repeating_deque(s):
          char_set = set()
          dq = deque()
          max_length = 0

          for char in s:
              while char in char_set:
                  char_set.remove(dq.popleft())  # Remove from the front of deque
              dq.append(char)
              char_set.add(char)
              max_length = max(max_length, len(dq))

          return max_length

      # Example usage
      s = "abcabcbb"
      print("Longest Substring Without Repeating Characters (Deque):", longest_substring_without_repeating_deque(s)) # Longest Substring Without Repeating Characters (Deque): 3

      ```
    </details>    

  - **Subarray with a Specific Condition (Sum ≥ Target)**: Find the length of the smallest subarray with a sum greater than or equal to the target using a sliding window. O(n) time complexity, O(k) space complexity.
    - **Best Practices**: Use for problems involving a moving window of elements.
    - **Efficiency**: Most efficient for operations requiring quick access to both ends of the deque. Less efficient when random access is required.
    - **Edge Cases**: Large sliding windows with frequent updates.
    - **Packages to Import**: `from collections import deque` or regular array
    <details>
      <summary>min_subarray_length_with_sum with array</summary>

      ```python
      def min_subarray_length_with_sum(array, target):
          start = 0
          current_sum = 0
          min_length = float('inf')

          for end in range(len(array)):
              current_sum += array[end]

              while current_sum >= target:
                  min_length = min(min_length, end - start + 1)
                  current_sum -= array[start]
                  start += 1

          return min_length if min_length != float('inf') else 0

      # Example usage
      array = [2, 3, 1, 2, 4, 3]
      target = 7
      print("Minimum Subarray Length with Sum ≥ Target:", min_subarray_length_with_sum(array, target))

      ```
    </details> 
    <details>
      <summary>min_subarray_length_with_sum with deque</summary>

      ```python
      def min_subarray_length_with_sum_deque(array, target):
          dq = deque()
          current_sum = 0
          min_length = float('inf')

          for num in array:
              dq.append(num)
              current_sum += num

              while current_sum >= target:
                  min_length = min(min_length, len(dq))
                  current_sum -= dq.popleft()

          return min_length if min_length != float('inf') else 0

      # Example usage
      array = [2, 3, 1, 2, 4, 3]
      target = 7
      print("Minimum Subarray Length with Sum ≥ Target (Deque):", min_subarray_length_with_sum_deque(array, target))

      ```
    </details>    



  - **Best Practices**: Use `deque` for queue-like operations to avoid O(n) operations of lists.
    - **Packages to Import**: `from collections import deque`
    - **Efficiency**: 
         Key Advantages of Using deque - Efficient Sliding Window Updates:
         - deque.popleft() is 𝑂(1) which is faster than shifting all elements in a list.
         - Ideal for scenarios where the window frequently updates by adding/removing elements.
         - Dynamic Window Management:
            Deques are particularly helpful when the size of the window is not fixed or depends on the conditions (e.g., sum or non-repetition constraints).
         - Optimized for Real-Time Processing:
            Especially useful for streams of data where you process elements as they arrive.
    <details>
      <summary>Best Practices Example</summary>

      ```python
      dq = deque([1, 2, 3])
      dq.appendleft(0)
      dq.append(4)
      print(dq)  # Output: deque([0, 1, 2, 3, 4])
      ```
    </details>    

  - **Thread-Safe Implementation**: Using threading.Lock
    - **Packages to Import**: collections, threading 
    <details>
      <summary>Thread-Safe Implementation Example</summary>

      ```python
      from collections import deque
      from threading import Lock, Thread
      import time

      lock = Lock()
      shared_window = deque(maxlen=3)

      def slide_window(value):
          with lock:
              time.sleep(0.1)  # Simulate I/O-bound task
              shared_window.append(value)

      threads = [Thread(target=slide_window, args=(i,)) for i in range(5)]
      for t in threads:
          t.start()
      for t in threads:
          t.join()

      print("Final Sliding Window:", shared_window)  # Output: Final Sliding Window: deque([2, 3, 4], maxlen=3)
      ```
    </details>


## 3. Array Module

### 3.1 array
- **Usage**: Compact, fixed-type arrays.
- **Common Algorithms**:
  - **Numeric Operations**: Efficient storage and manipulation of numeric data. O(n) time complexity for traversal, O(1) space complexity.
    - **Best Practices**: Use for memory-efficient storage of numeric data.
    - **Efficiency**: Most efficient for fixed-type numeric data. Less efficient for mixed-type data.
    - **Edge Cases**: Large arrays with frequent updates.
    - **Packages to Import**: `import array`
    <details>
      <summary>Numeric Operations Example</summary>

      ```python
      import array

      arr = array.array('i', [1, 2, 3, 4])
      arr.append(5)
      print(arr)  # Output: array('i', [1, 2, 3, 4, 5])

      # Regular Implementation
      arr = array.array('i', [1, 2, 3, 4])
      arr.append(5)
      print(arr)  # Output: array('i', [1, 2, 3, 4, 5])

      # Best Practices Implementation: Using a pre-allocated array for large data
      arr = array.array('i', [0] * 1000000)
      for i in range(1000000):
          arr[i] = i

      print(arr[-1])  # Output: 999999
      ```

      **Worst-Case Example**: Large arrays with frequent updates.
      ```python
      large_array = array.array('i', range(1000000))
      large_array.append(1000000)
      print(large_arr[-1])  # Output: 1000000
      ```
    </details>
  - **Best Practices**: Use when memory efficiency and fixed-type array constraints are necessary.
    - **Packages to Import**: `import array`
    <details>
      <summary>Best Practices Example</summary>

      ```python
      float_array = array.array('f', [1.0, 2.0, 3.0])
      print(float_array)  # Output: array('f', [1.0, 2.0, 3.0])
      ```
    </details>

  - **Thread-Safe Implementation**: Using threading.Lock
    - **Packages to Import**: from multiprocessing import Array, Process 
    <details>
      <summary>Thread-Safe Implementation Example</summary>

      ```python
      from multiprocessing import Array, Process
      import time

      shared_array = Array('i', [0, 0, 0, 0, 0])  # Shared integer array

      def update_array(index, value):
          time.sleep(0.1)  # Simulating I/O-bound task
          shared_array[index] = value

      processes = [Process(target=update_array, args=(i, i * 10)) for i in range(5)]

      for p in processes:
          p.start()
      for p in processes:
          p.join()

      print("Final Array:", shared_array[:])  # Output: [0, 10, 20, 30, 40]
      ```
    </details>


## 4. NumPy Arrays

- **Usage**: Multi-dimensional arrays for numerical computations.
- **Common Algorithms**:
  - **Matrix Operations**: Linear algebra, element-wise operations. O(n^2) time complexity for matrix multiplication, O(n^2) space complexity.
    - **Best Practices**: Utilize broadcasting and vectorized operations for performance.
    - **Efficiency**: Most efficient for large-scale numerical computations. Less efficient for small datasets.
    - **Edge Cases**: Large arrays with complex operations.
    - **Packages to Import**: `import numpy as np`
    <details>
      <summary>Matrix Operations Example</summary>

      ```python
      import numpy as np

      a = np.array([1, 2, 3])
      b = np.array([4, 5, 6])
      dot_product = np.dot(a, b)
      print(dot_product)  # Output: 32

      # Regular Implementation
      a = np.array([1, 2, 3])
      b = np.array([4, 5, 6])
      dot_product = np.dot(a, b)
      print(dot_product)  # Output: 32

      # Best Practices Implementation: Using broadcasting and vectorized operations
      a = np.array([[1, 2], [3, 4]])
      b = np.array([[5, 6], [7, 8]])
      sum_matrix = a + b  # Broadcasting and vectorized operation

      print(sum_matrix)  # Output: [[ 6  8]
                         #          [10 12]]
      ```

      **Worst-Case Example**: Large arrays with complex matrix operations.
      ```python
      a = np.random.rand(1000, 1000)
      b = np.random.rand(1000, 1000)
      result = np.dot(a, b)

      # Expected Output:
      # result: A 1000x1000 matrix with computed dot product values
      # Each element in this 1000x1000 matrix is the sum of products of corresponding elements
      # from the rows of matrix `a` and the columns of matrix `b`.

      # Printing the result will display a large 1000x1000 matrix
      print(result)  # Output: A large 1000x1000 matrix
      ```
    </details>
  - **Best Practices**: Utilize broadcasting and vectorized operations for performance.
    - **Packages to Import**: `import numpy as np`
    <details>
      <summary>Best Practices Example</summary>

      ```python
      a = np.array([[1, 2], [3, 4]])
      b = np.array([[5, 6], [7, 8]])
      sum_matrix = a + b  # Broadcasting and vectorized operation

      # Expected Output:
      # sum_matrix: A 2x2 matrix where each element is the sum of corresponding elements from matrices `a` and `b`
      # [[1 + 5, 2 + 6],
      #  [3 + 7, 4 + 8]]
      # Resulting in:
      # [[ 6,  8],
      #  [10, 12]]
      ```
    </details>

  - **Thread-Safe Implementation**: Using threading.Lock
    - **Packages to Import**: import numpy as np, from multiprocessing import Process, Manager
    <details>
      <summary>Thread-Safe Implementation Example</summary>

      ```python
      import numpy as np
      from multiprocessing import Process, Manager

      def update_array(shared_data, index, value):
          shared_data[index] = value

      if __name__ == "__main__":
          with Manager() as manager:
              shared_data = manager.list([0, 0, 0, 0, 0])  # Shared memory list
              processes = [Process(target=update_array, args=(shared_data, i, i * 10)) for i in range(5)]

              for p in processes:
                  p.start()
              for p in processes:
                  p.join()

              print("Final Numpy-like Array:", list(shared_data))  # Output: [0, 10, 20, 30, 40]
      ```
    </details>


## 5. Pandas DataFrames

- **Usage**: Tabular data structure, similar to SQL tables or Excel spreadsheets.
- **Common Algorithms**:
  - **Data Analysis**: Aggregation, filtering, merging, group-by operations. O(n) time complexity, O(n) space complexity.
    - **Best Practices**: Use for data manipulation and analysis, especially with large datasets.
    - **Efficiency**: Most efficient for large-scale data analysis. Less efficient for small datasets or simple data structures.
    - **Edge Cases**: Large dataframes with complex operations.
    - **Packages to Import**: `import pandas as pd`
    <details>
      <summary>Data Analysis Example</summary>

      ```python
      import pandas as pd

      data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}
      df = pd.DataFrame(data)
      grouped = df.groupby('age').size()

      # Expected Output:
      # A Pandas Series with the count of occurrences of each age
      # age
      # 25    1
      # 30    1
      # 35    1
      # dtype: int64

      print(grouped)  # Output:
                      # age
                      # 25    1
                      # 30    1
                      # 35    1
                      # dtype: int64

      # Regular Implementation
      data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}
      df = pd.DataFrame(data)
      grouped = df.groupby('age').size()

      print(grouped)  # Output:
                      # age
                      # 25    1
                      # 30    1
                      # 35    1
                      # dtype: int64

      # Best Practices Implementation: Using vectorized operations for efficiency
      df['age_squared'] = df['age'] ** 2

      print(df)  # Output:
           #       name  age  age_squared
           # 0    Alice   25          625
           # 1      Bob   30          900
           # 2  Charlie   35         1225
      ```

      **Worst-Case Example**: Large dataframes with complex group-by operations.
      ```python
      # Define a dictionary with 1,000,000 'name' entries all set to 'Alice' and 'age' entries all set to 25
      data = {'name': ['Alice']*1000000, 'age': [25]*1000000}
      
      # Create a DataFrame from the dictionary
      df = pd.DataFrame(data)
      
      # Group by the 'age' column and count the size of each group
      grouped = df.groupby('age').size()

      print(grouped)  # Output:
                      # age
                      # 25    1000000
                      # dtype: int64
      ```
    </details>
  - **Best Practices**: Leverage built-in functions and avoid loops for data manipulation.
    - **Packages to Import**: `import pandas as pd`
    <details>
      <summary>Best Practices Example</summary>

      ```python
      df['age_squared'] = df['age'].apply(lambda x: x**2)

      # Expected Output: DataFrame with a new column 'age_squared'
      print(df.head())  # Output: First 5 rows of the DataFrame
                        #       name  age  age_squared
                        # 0    Alice   25          625
                        # 1    Alice   25          625
                        # 2    Alice   25          625
                        # 3    Alice   25          625
                        # 4    Alice   25          625
      ```
    </details>

  - **Thread-Safe Implementation**: Using threading.Lock
    - **Packages to Import**: import numpy as np, from multiprocessing import Process, Manager
    <details>
      <summary>Thread-Safe Implementation Example</summary>

      ```python
      import pandas as pd
      from threading import Lock, Thread
      import time

      lock = Lock()
      df = pd.DataFrame({"A": [0, 0], "B": [0, 0]})

      def update_row(index, a, b):
          with lock:
              time.sleep(0.1)  # Simulate I/O-bound task
              df.loc[index] = [a, b]

      threads = [Thread(target=update_row, args=(i, i + 1, (i + 1) * 2)) for i in range(2)]
      for t in threads:
          t.start()
      for t in threads:
          t.join()

      print("Final DataFrame:")
      print(df)
      # Output:
      #    A   B
      # 0  1   2
      # 1  2   4
      ```
    </details>


## 6. SortedList
- **Description**: A list that maintains its elements in sorted order.
- **Common Algorithms**:
  - **Insertion**: Maintains order while inserting. O(log n) time complexity.
  - **Deletion**: Maintains order while deleting. O(log n) time complexity.
- **Best Practices**: Use for maintaining a sorted sequence of elements.
- **Efficiency**: Most efficient for maintaining sorted order in dynamic sequences.
- **Edge Cases**: Large lists with frequent insertions and deletions.
- **Packages to Import**: `from sortedcontainers import SortedList`
<details>
  <summary>SortedList Example</summary>

  ```python
  from sortedcontainers import SortedList

  sl = SortedList([3, 1, 4, 1, 5, 9, 2, 6])
  sl.add(7)
  print(sl)  # Output: SortedList([1, 1, 2, 3, 4, 5, 6, 7, 9])
  ```
</details>

## 7. heappush
- **Description**: Pushes an element onto the heap, maintaining the heap invariant.
- **Common Algorithms**:
  - **Insertion**: Adds an element while maintaining the heap property. O(log n) time complexity.
- **Best Practices**: Use for priority queue implementations.
- **Efficiency**: Most efficient for maintaining priority queues.
- **Edge Cases**: Large heaps with frequent insertions.
- **Packages to Import**: `import heapq`
<details>
  <summary>heappush Example</summary>

  ```python
  import heapq

  heap = []
  heapq.heappush(heap, 3)
  heapq.heappush(heap, 1)
  heapq.heappush(heap, 4)
  print(heap)  # Output: [1, 3, 4]
  ```
</details>

## 8. heappop
- **Description**: Pops the smallest element from the heap, maintaining the heap invariant.
- **Common Algorithms**:
  - **Deletion**: Removes the smallest element while maintaining the heap property. O(log n) time complexity.
- **Best Practices**: Use for priority queue implementations.
- **Efficiency**: Most efficient for maintaining priority queues.
- **Edge Cases**: Large heaps with frequent deletions.
- **Packages to Import**: `import heapq`
<details>
  <summary>heappop Example</summary>

  ```python
  import heapq

  heap = [1, 3, 4]
  smallest = heapq.heappop(heap)
  print(smallest)  # Output: 1
  print(heap)  # Output: [3, 4]
  ```
</details>

## 9. itertools Module
- **Description**: Provides functions that create iterators for efficient looping.
- **Common Algorithms**:
  - **Permutations**: Generates permutations of a sequence. O(n!) time complexity.
  - **Combinations**: Generates combinations of a sequence. O(n!) time complexity.
- **Best Practices**: Use for combinatoric and permutation generation.
- **Efficiency**: Most efficient for generating combinations and permutations.
- **Edge Cases**: Large sequences leading to large numbers of combinations or permutations.
- **Packages to Import**: `import itertools`
<details>
  <summary>itertools Example</summary>

  ```python
  import itertools

  perms = list(itertools.permutations([1, 2, 3]))
  print(perms)  # Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
  ```
</details>

## 10. functools Module
- **Description**: Provides higher-order functions and operations on callable objects.
- **Common Algorithms**:
  - **Memoization**: Caches the results of function calls. O(1) average time complexity for cached results.
- **Best Practices**: Use for memoization and function tools.
- **Efficiency**: Most efficient for reducing redundant calculations.
- **Edge Cases**: Functions with large input spaces leading to high memory usage.
- **Packages to Import**: `from functools import lru_cache`
<details>
  <summary>functools Example</summary>

  ```python
  from functools import lru_cache

  @lru_cache(maxsize=None)
  def fibonacci(n):
      if n < 2:
          return n
      return fibonacci(n-1) + fibonacci(n-2)

  print(fibonacci(10))  # Output: 55
  ```
</details>


## 11. Custom Data Structures

### 11.1 Linked Lists
- **Usage**: Dynamic data structure with efficient insertions/deletions.
- **Common Algorithms**:
  - **Traversal**: Iterating over elements. O(n) time complexity, O(1) space complexity.
    - **Best Practices**: Use when frequent insertions/deletions are required.
    - **Efficiency**: Most efficient for operations involving frequent insertions and deletions. Less efficient for random access.
    - **Edge Cases**: Large linked lists with frequent updates.
    - **Packages to Import**: None
    <details>
      <summary>Traversal Example</summary>

      ```python
      class Node:
          def __init__(self, data=None):
              self.data = data
              self.next = None

      class LinkedList:
          def __init__(self):
              self.head = None

          def append(self, data):
              new_node = Node(data)
              if not self.head:
                  self.head = new_node
                  return
              last = self.head
              while last.next:
                  last = last.next
              last.next = new_node

          def print_list(self):
              curr = self.head
              while curr:
                  print(curr.data)
                  curr = curr.next

      # Regular Implementation
      ll = LinkedList()
      for i in range(10):
          ll.append(i)
      ll.print_list()

      # Best Practices Implementation: Using a helper method for appending
      class LinkedListOptimized:
          def __init__(self):
              self.head = None

          def append(self, data):
              new_node = Node(data)
              if not self.head:
                  self.head = new_node
                  return
              last = self.head
              while last.next:
                  last = self.next
              last.next = new_node

          def print_list(self):
              curr = self.head
              while curr:
                  print(curr.data)
                  curr = curr.next

          def append_values(self, values):
              for value in values:
                  self.append(value)

      ll = LinkedListOptimized()
      ll.append_values(range(10))
      ll.print_list()
      ```

      **Worst-Case Example**: Large linked lists with frequent updates.
      ```python
      ll = LinkedList()
      for i in range(100000):
          ll.append(i)
      ll.print_list()
      ```
    </details>
  - **Best Practices**: Use when frequent insertions/deletions are required; implement using classes.
  - **Thread-Safe Implementation**: Using threading.Lock
    - **Packages to Import**: import numpy as np, from multiprocessing import Process, Manager
    <details>
      <summary>Thread-Safe Implementation Example</summary>

      ```python
      from threading import Lock, Thread
      import time

      class Node:
          def __init__(self, data):
              self.data = data
              self.next = None

      class ThreadSafeLinkedList:
          def __init__(self):
              self.head = None
              self.lock = Lock()

          def append(self, data):
              with self.lock:
                  time.sleep(0.1)  # Simulating I/O-bound task
                  new_node = Node(data)
                  if not self.head:
                      self.head = new_node
                  else:
                      current = self.head
                      while current.next:
                          current = current.next
                      current.next = new_node

          def print_list(self):
              current = self.head
              while current:
                  print(current.data, end=" -> ")
                  current = current.next
              print("None")

      linked_list = ThreadSafeLinkedList()

      def add_elements(values):
          for value in values:
              linked_list.append(value)

      threads = [Thread(target=add_elements, args=([i * 10, i * 10 + 5],)) for i in range(3)]
      for t in threads:
          t.start()
      for t in threads:
          t.join()

      print("Final Linked List:")
      linked_list.print_list()
      # Output: Final Linked List: 0 -> 5 -> 10 -> 15 -> 20 -> 25 -> None
      ```
    </details>


### 6.2 Stacks
- **Usage**: LIFO (Last In, First Out) structure.
- **Common Algorithms**:
  - **Expression Evaluation**: Parsing expressions, backtracking. O(n) time complexity, O(n) space complexity.
    - **Best Practices**: Use for operations requiring LIFO structure, such as expression evaluation and backtracking.
    - **Efficiency**: Most efficient for LIFO operations. Less efficient for random access.
    - **Edge Cases**: Large stacks with frequent push/pop operations.
    - **Packages to Import**: None
    <details>
      <summary>Expression Evaluation Example</summary>

      ```python
      class Stack:
          def __init__(self):
              self.items = []

          def push(self, item):
              self.items.append(item)

          def pop(self):
              return self.items.pop()

          def is_empty(self):
              return len(self.items) == 0

          def peek(self):
              return self.items[-1] if not self.is_empty() else None

      # Regular Implementation
      stack = Stack()
      for i in range(10):
          stack.push(i)
      while not stack.is_empty():
          stack.pop()

      # Best Practices Implementation: Using a pre-allocated list for large stacks
      class StackOptimized:
          def __init__(self, max_size):
              self.items = [None] * max_size
              self.top = -1

          def push(self, item):
              self.top += 1
              self.items[self.top] = item

          def pop(self):
              item = self.items[self.top]
              self.top -= 1
              return item

          def is_empty(self):
              return self.top == -1

          def peek(self):
              return self.items[self.top] if not self.is_empty() else None

      stack = StackOptimized(100000)
      for i in range(100000):
          stack.push(i)
      while not stack.is_empty():
          stack.pop()
      ```

      **Worst-Case Example**: Large stacks with frequent push/pop operations.
      ```python
      stack = Stack()
      for i in range(100000):
          stack.push(i)
      while not stack.is_empty():
          stack.pop()
      ```
    </details>
  - **Best Practices**: Use lists or `deque` for stack operations.

### 6.3 Queues
- **Usage**: FIFO (First In, First Out) structure.
- **Common Algorithms**:
  - **BFS (Breadth-First Search)**: Tree/graph traversal. O(n + m) time complexity, O(n) space complexity.
    - **Best Practices**: Use for BFS and other operations requiring FIFO structure.
    - **Efficiency**: Most efficient for FIFO operations. Less efficient for random access.
    - **Edge Cases**: Large queues with frequent enqueue/dequeue operations.
    - **Packages to Import**: `from collections import deque`
    <details>
      <summary>BFS Example</summary>

      ```python
      from collections import deque

      def bfs(graph, start):
          visited = set()
          queue = deque([start])

          while queue:
              vertex = queue.popleft()
              if vertex not in visited:
                  visited.add(vertex)
                  queue.extend(set(graph[vertex]) - visited)
          return visited

      # Regular Implementation
      graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
      visited_nodes = bfs(graph, 2)

      # Best Practices Implementation: Using a deque for efficient FIFO operations
      def bfs_optimized(graph, start):
          visited = set()
          queue = deque([start])
          while queue:
              vertex = queue.popleft()
              if vertex not in visited:
                  visited.add(vertex)
                  queue.extend(set(graph[vertex]) - visited)
          return visited

      graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
      visited_nodes = bfs_optimized(graph, 2)
      ```

      **Worst-Case Example**: Large graphs with many nodes and edges.
      ```python
      graph = {i: [i+1] for i in range(100000)}
      visited_nodes = bfs(graph, 0)
      ```
    </details>
  - **Best Practices**: Use `deque` for queue operations to ensure O(1) performance.

### 6.4 Priority Queues
- **Usage**: Elements with priorities, typically implemented with heaps.
- **Common Algorithms**:
  - **Dijkstra's Algorithm**: Shortest path in graphs. O((n + m) log n) time complexity, O(n) space complexity.
    - **Best Practices**: Use for shortest path algorithms and task scheduling.
    - **Efficiency**: Most efficient for operations involving priorities. Less efficient for random access.
    - **Edge Cases**: Large priority queues with frequent push/pop operations.
    - **Packages to Import**: `import heapq`
    <details>
      <summary>Dijkstra's Algorithm Example</summary>

      ```python
      import heapq

      class PriorityQueue:
          def __init__(self):
              self.heap = []

          def push(self, item, priority):
              heapq.heappush(self.heap, (priority, item))

          def pop(self):
              return heapq.heappop(self.heap)[1]

          def is_empty(self):
              return len(self.heap) == 0

      # Regular Implementation
      pq = PriorityQueue()
      for i in range(10):
          pq.push(i, i)
      while not pq.is_empty():
          pq.pop()

      # Best Practices Implementation: Using a min-heap for priority queue operations
      import heapq

      class MinHeap:
          def __init__(self):
              self.heap = []

          def push(self, item):
              heapq.heappush(self.heap, item)

          def pop(self):
              return heapq.heappop(self.heap)

          def is_empty(self):
              return len(self.heap) == 0

      pq = MinHeap()
      for i in range(100000):
          pq.push(i)
      while not pq.is_empty():
          pq.pop()
      ```

      **Worst-Case Example**: Large priority queues with frequent push/pop operations.
      ```python
      pq = PriorityQueue()
      for i in range(100000):
          pq.push(i, i)
      while not pq.is_empty():
          pq.pop()
      ```
    </details>
  - **Best Practices**: Use `heapq` module for priority queue operations.
  - **Thread-Safe Implementation**: Using threading.Lock
    - **Packages to Import**: import numpy as np, from multiprocessing import Process, Manager
    <details>
      <summary>Thread-Safe Implementation Example</summary>

      ```python
      import queue
      from threading import Thread
      import time

      pq = queue.PriorityQueue()

      def add_to_heap(value):
          time.sleep(0.1)  # Simulating I/O-bound task
          pq.put(value)

      def remove_from_heap():
          time.sleep(0.1)  # Simulating I/O-bound task
          if not pq.empty():
              print(pq.get())

      threads = [Thread(target=add_to_heap, args=(i,)) for i in range(5)] + [Thread(target=remove_from_heap) for _ in range(5)]
      for t in threads:
          t.start()
      for t in threads:
          t.join()

      # Output (order depends on PriorityQueue behavior):
      # 0
      # 1
      # 2
      # 3
      # 4
      ```
    </details>


## 7. Graphs

- **Usage**: Nodes connected by edges.
- **Common Algorithms**:
  - **DFS (Depth-First Search), BFS, Dijkstra's, A***: Various traversal and pathfinding algorithms.
    - **DFS**: Depth-first search is a graph traversal algorithm that explores as far down a branch as possible before backtracking. Time complexity O(n + m), space complexity O(n).
      - **Best Practices**: Use for exploring all possible paths, detecting cycles, and solving problems like maze traversal.
      - **Efficiency**: Most efficient for problems requiring full exploration of the graph. Less efficient for finding shortest paths in unweighted graphs.
      - **Edge Cases**: Graphs with long branches and few nodes.
      - **Packages to Import**: None
      <details>
        <summary>DFS Example</summary>

        ```python
        def dfs(graph, start):
            visited = set()
            stack = [start]

            while stack:
                vertex = stack.pop()
                if vertex not in visited:
                    visited.add(vertex)
                    stack.extend(set(graph[vertex]) - visited)
            return visited

        # Regular Implementation
        graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
        visited_nodes = dfs(graph, 2)

        # Best Practices Implementation: Using a recursive DFS with memoization
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs_recursive(graph, start, visited=None):
            if visited is None:
                visited = set()
            visited.add(start)
            for neighbor in graph[start]:
                if neighbor not in visited:
                    dfs_recursive(graph, neighbor, visited)
            return visited

        graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
        visited_nodes = dfs_recursive(frozenset(graph.items()), 2)
        ```

        **Worst-Case Example**: Graphs with long branches and few nodes.
        ```python
        graph = {i: [i+1] for i in range(100000)}
        visited_nodes = dfs(graph, 0)
        ```
      </details>

    - **BFS**: Breadth-first search is a graph traversal algorithm that explores all neighbors at the present depth before moving on to nodes at the next depth level. Time complexity O(n + m), space complexity O(n).
      - **Best Practices**: Use for finding the shortest path in unweighted graphs and for level-order traversal.
      - **Efficiency**: Most efficient for finding shortest paths in unweighted graphs. Less efficient for deep graphs with many branches.
      - **Edge Cases**: Deep graphs with many branches.
      - **Packages to Import**: `from collections import deque`
      <details>
        <summary>BFS Example</summary>

        ```python
        from collections import deque

        def bfs(graph, start):
            visited = set()
            queue = deque([start])

            while queue:
                vertex = queue.popleft()
                if vertex not in visited:
                    visited.add(vertex)
                    queue.extend(set(graph[vertex]) - visited)
            return visited

        # Regular Implementation
        graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
        visited_nodes = bfs(graph, 2)

        # Best Practices Implementation: Using a BFS with early stopping for shortest path
        def bfs_shortest_path(graph, start, goal):
            visited = set()
            queue = deque([(start, [start])])

            while queue:
                vertex, path = queue.popleft()
                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        if neighbor == goal:
                            return path + [neighbor]
                        visited.add(neighbor)
                        queue.append((neighbor, path + [neighbor]))
            return None

        graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
        shortest_path = bfs_shortest_path(graph, 2, 3)
        ```

        **Worst-Case Example**: Deep graphs with many branches.
        ```python
        graph = {i: [i+1] for i in range(100000)}
        visited_nodes = bfs(graph, 0)
        ```
      </details>

    - **Dijkstra's**: Dijkstra's algorithm finds the shortest paths from the source node to all other nodes in a weighted graph. Time complexity O((n + m) log n), space complexity O(n).
      - **Best Practices**: Use for finding the shortest path in weighted graphs.
      - **Efficiency**: Most efficient for graphs with non-negative weights. Less efficient for graphs with many edges and negative weights.
      - **Edge Cases**: Graphs with many edges and negative weights.
      - **Packages to Import**: `import heapq`
      <details>
        <summary>Dijkstra's Algorithm Example</summary>

        ```python
        import heapq

        def dijkstra(graph, start):
            pq = []
            heapq.heappush(pq, (0, start))
            distances = {start: 0}

            while pq:
                (current_distance, current_vertex) = heapq.heappop(pq)
                for neighbor, weight in graph[current_vertex].items():
                    distance = current_distance + weight
                    if distance < distances.get(neighbor, float('inf')):
                        distances[neighbor] = distance
                        heapq.heappush(pq, (distance, neighbor))
            return distances

        # Regular Implementation
        graph = {0: {1: 1, 2: 4}, 1: {2: 2, 3: 5}, 2: {3: 1}, 3: {}}
        distances = dijkstra(graph, 0)

        # Best Practices Implementation: Using a priority queue for efficient distance updates
        def dijkstra_optimized(graph, start):
            pq = []
            heapq.heappush(pq, (0, start))
            distances = {start: 0}

            while pq:
                (current_distance, current_vertex) = heapq.heappop(pq)
                for neighbor, weight in graph[current_vertex].items():
                    distance = current_distance + weight
                    if distance < distances.get(neighbor, float('inf')):
                        distances[neighbor] = distance
                        heapq.heappush(pq, (distance, neighbor))
            return distances

        graph = {0: {1: 1, 2: 4}, 1: {2: 2, 3: 5}, 2: {3: 1}, 3: {}}
        distances = dijkstra_optimized(graph, 0)
        ```

        **Worst-Case Example**: Graphs with many edges and negative weights.
        ```python
        graph = {i: {i+1: 1} for i in range(100000)}
        distances = dijkstra(graph, 0)
        ```
      </details>

    - **A***: A* algorithm is an informed search algorithm used for pathfinding and graph traversal, which uses heuristics to improve the performance of Dijkstra's algorithm. Time complexity O((n + m) log n), space complexity O(n).
      - **Best Practices**: Use for finding the shortest path in graphs where an accurate heuristic is available.
      - **Efficiency**: Most efficient for graphs with a good heuristic function. Less efficient when the heuristic is inaccurate.
      - **Edge Cases**: Graphs with inaccurate heuristics.
      - **Packages to Import**: None
      <details>
        <summary>A* Algorithm Example</summary>

        ```python
        def a_star(graph, start, goal, h):
            open_set = set([start])
            came_from = {}

            g_score = {start: 0}
            f_score = {start: h(start)}

            while open_set:
                current = min(open_set, key=lambda x: f_score.get(x, float('inf')))
                if current == goal:
                    return reconstruct_path(came_from, current)

                open_set.remove(current)
                for neighbor in graph[current]:
                    tentative_g_score = g_score[current] + graph[current][neighbor]
                    if tentative_g_score < g_score.get(neighbor, float('inf')):
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = g_score[neighbor] + h(neighbor)
                        open_set.add(neighbor)
            return None

        def reconstruct_path(came_from, current):
            total_path = [current]
            while current in came_from:
                current = came_from[current]
                total_path.append(current)
            return total_path[::-1]

        # Regular Implementation
        graph = {0: {1: 1, 2: 4}, 1: {2: 2, 3: 5}, 2: {3: 1}, 3: {}}
        h = lambda x: 0  # Heuristic function
        path = a_star(graph, 0, 3, h)

        # Best Practices Implementation: Using a more accurate heuristic
        def a_star_optimized(graph, start, goal, h):
            open_set = set([start])
            came_from = {}

            g_score = {start: 0}
            f_score = {start: h(start)}

            while open_set:
                current = min(open_set, key=lambda x: f_score.get(x, float('inf')))
                if current == goal:
                    return reconstruct_path(came_from, current)

                open_set.remove(current)
                for neighbor in graph[current]:
                    tentative_g_score = g_score[current] + graph[current][neighbor]
                    if tentative_g_score < g_score.get(neighbor, float('inf')):
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = g_score[neighbor] + h(neighbor)
                        open_set.add(neighbor)
            return None

        graph = {0: {1: 1, 2: 4}, 1: {2: 2, 3: 5}, 2: {3: 1}, 3: {}}
        h = lambda x: abs(x - 3)  # Heuristic function
        path = a_star_optimized(graph, 0, 3, h)
        ```

        **Worst-Case Example**: Graphs with inaccurate heuristics.
        ```python
        graph = {i: {i+1: 1} for i in range(100000)}
        h = lambda x: 0  # Heuristic function
        path = a_star(graph, 0, 99999, h)
        ```
      </details>
  - **Best Practices**: Use adjacency lists for sparse graphs; adjacency matrices for dense graphs.
  - **Thread-Safe Implementation**: Using threading.Lock
    - **Packages to Import**: import numpy as np, from multiprocessing import Process, Manager
    <details>
      <summary>Thread-Safe Implementation Example</summary>

      ```python
      from threading import Lock, Thread
      import time

      lock = Lock()
      graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A"], "D": ["B"]}

      def add_edge(node, neighbor):
          with lock:
              time.sleep(0.1)  # Simulating I/O-bound task
              if node in graph:
                  graph[node].append(neighbor)
              else:
                  graph[node] = [neighbor]

      threads = [Thread(target=add_edge, args=("A", "D")), Thread(target=add_edge, args=("C", "E"))]
      for t in threads:
          t.start()
      for t in threads:
          t.join()

      print("Final Graph:", graph)
      # Output: {'A': ['B', 'C', 'D'], 'B': ['A', 'D'], 'C': ['A', 'E'], 'D': ['B']}
      ```
    </details>


## Best Practices for Algorithms

### Sorting
- **Packages to Import**: None

#### Quick Sort
- **Description**: A fast, divide-and-conquer algorithm that selects a pivot element and partitions the array into subarrays.
- **Best Practices**: Use for general-purpose sorting, especially when average-case performance is more important than worst-case performance.
- **Efficiency**: Most efficient when the pivot divides the list into balanced subarrays. Less efficient when the pivot results in highly unbalanced partitions.
- **Edge Cases**: When the list is already sorted or contains many duplicate elements, leading to unbalanced partitions.
- **Examples**:
  <details>
    <summary>Quick Sort Example</summary>

    ```python
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

    # Regular Implementation
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sorted_arr = quick_sort(arr)

    # Best Practices Implementation: Using a cached version for repeated sorting
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def quick_sort_cached(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort_cached(tuple(left)) + tuple(middle) + quick_sort_cached(tuple(right))

    arr = tuple([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    sorted_arr = quick_sort_cached(arr)
    ```

    **Worst-Case Example**: When the list is already sorted in ascending or descending order.
    ```python
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sorted_arr = quick_sort(arr)
    ```
  </details>

#### Merge Sort
- **Description**: A stable, divide-and-conquer algorithm that divides the array into halves, sorts each half, and merges them.
- **Best Practices**: Use when a stable sort is required, and when working with large data sets that don't fit in memory (external sorting).
- **Efficiency**: Most efficient for large datasets due to its stable time complexity. Less efficient due to higher space complexity.
- **Edge Cases**: Lists with a large number of elements.
- **Examples**:
  <details>
    <summary>Merge Sort Example</summary>

    ```python
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
    
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # Regular Implementation
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = merge_sort(arr)

    # Best Practices Implementation: Using a cached version for repeated sorting
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def merge_sort_cached(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_cached(tuple(arr[:mid]))
        right = merge_sort_cached(tuple(arr[mid:]))
        return merge(left, right)

    arr = tuple([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    sorted_arr = merge_sort_cached(arr)
    ```

    **Worst-Case Example**: Sorting large lists with merge sort.
    ```python
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = merge_sort(arr)
    ```
  </details>

#### Tim Sort
- **Description**: A hybrid sorting algorithm derived from merge sort and insertion sort, used by Python's built-in `sorted()` function.
- **Best Practices**: Use for general-purpose sorting, especially when stability and performance are crucial.
- **Efficiency**: Most efficient for real-world data, which often contains runs of ordered elements. Less efficient in scenarios with highly random data.
- **Edge Cases**: Lists with a mix of ordered and unordered segments.
- **Examples**:
  <details>
    <summary>Tim Sort Example</summary>

    ```python
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = sorted(arr)  # Uses Tim Sort internally

    # Regular Implementation
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = sorted(arr)

    # Best Practices Implementation: Sorting large datasets with multiple runs
    large_arr = [i % 10 for i in range(1000000)]
    sorted_large_arr = sorted(large_arr)
    ```

    **Worst-Case Example**: Highly random or pathological data sequences.
    ```python
    arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    sorted_arr = sorted(arr)
    ```
  </details>

### Searching
- **Packages to Import**: None

#### Linear Search
- **Description**: A simple search algorithm that checks each element until the target is found.
- **Best Practices**: Use for small or unsorted datasets.
- **Efficiency**: Most efficient for small datasets. Less efficient for large datasets.
- **Edge Cases**: When the target element is not in the list or at the end of the list.
- **Examples**:
  <details>
    <summary>Linear Search Example</summary>

    ```python
    def linear_search(arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

    # Regular Implementation
    arr = [1, 2, 3, 4, 5]
    index = linear_search(arr, 6)

    # Best Practices Implementation: Implementing a linear search with early stopping
    def linear_search_early_stop(arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
            if arr[i] > target:
                return -1
        return -1

    arr = [1, 2, 3, 4, 5]
    index = linear_search_early_stop(arr, 6)
    ```

    **Worst-Case Example**: Target element not present in the list.
    ```python
    arr = [1, 2, 3, 4, 5]
    index = linear_search(arr, 6)
    ```
  </details>

#### Binary Search
- **Description**: An efficient search algorithm that works on sorted arrays by repeatedly dividing the search interval in half.
- **Best Practices**: Use for large, sorted datasets.
- **Efficiency**: Most efficient for large, sorted datasets. Less efficient for unsorted datasets.
- **Edge Cases**: When the target element is not in the list.
- **Examples**:
  <details>
    <summary>Binary Search Example</summary>

    ```python
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    # Regular Implementation
    arr = [1, 2, 3, 4, 5]
    index = binary_search(arr, 6)

    # Best Practices Implementation: Using a recursive binary search with memoization
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def binary_search_recursive(arr, left, right, target):
        if right >= left:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                return binary_search_recursive(arr, left, mid - 1, target)
            else:
                return binary_search_recursive(arr, mid + 1, right, target)
        else:
            return -1

    arr = tuple([1, 2, 3, 4, 5])
    index = binary_search_recursive(arr, 0, len(arr) - 1, 6)
    ```

    **Worst-Case Example**: Target element not present in the list.
    ```python
    arr = [1, 2, 3, 4, 5]
    index = binary_search(arr, 6)
    ```
  </details>

### Graph Traversal
- **Packages to Import**: `from collections import deque`

#### BFS (Breadth-First Search)
- **Description**: A graph traversal algorithm that explores all neighbors at the present depth before moving on to nodes at the next depth level.
- **Best Practices**: Use for finding the shortest path in unweighted graphs and for level-order traversal.
- **Efficiency**: Most efficient for finding shortest paths in unweighted graphs. Less efficient for deep graphs with many branches.
- **Edge Cases**: Deep graphs with many branches.
- **Examples**:
  <details>
    <summary>BFS Example</summary>

    ```python
    from collections import deque

    def bfs(graph, start):
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(set(graph[vertex]) - visited)
        return visited

    # Regular Implementation
    graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
    visited_nodes = bfs(graph, 2)

    # Best Practices Implementation: Using a BFS with early stopping for shortest path
    def bfs_shortest_path(graph, start, goal):
        visited = set()
        queue = deque([(start, [start])])

        while queue:
            vertex, path = queue.popleft()
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    if neighbor == goal:
                        return path + [neighbor]
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None

    graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
    shortest_path = bfs_shortest_path(graph, 2, 3)
    ```

    **Worst-Case Example**: Deep graphs with many branches.
    ```python
    graph = {i: [i+1] for i in range(100000)}
    visited_nodes = bfs(graph, 0)
    ```
  </details>

#### DFS (Depth-First Search)
- **Description**: A graph traversal algorithm that explores as far down a branch as possible before backtracking.
- **Best Practices**: Use for exploring all possible paths, detecting cycles, and solving problems like maze traversal.
- **Efficiency**: Most efficient for problems requiring full exploration of the graph. Less efficient for finding shortest paths in unweighted graphs.
- **Edge Cases**: Graphs with long branches and few nodes.
- **Examples**:
  <details>
    <summary>DFS Example</summary>

    ```python
    def dfs(graph, start):
        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(set(graph[vertex]) - visited)
        return visited

    # Regular Implementation
    graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
    visited_nodes = dfs(graph, 2)

    # Best Practices Implementation: Using a recursive DFS with memoization
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dfs_recursive(graph, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs_recursive(graph, neighbor, visited)
        return visited

    graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
    visited_nodes = dfs_recursive(frozenset(graph.items()), 2)
    ```

    **Worst-Case Example**: Graphs with long branches and few nodes.
    ```python
    graph = {i: [i+1] for i in range(100000)}
    visited_nodes = dfs(graph, 0)
    ```
  </details>

### Dynamic Programming
- **Packages to Import**: None

#### Memoization
- **Description**: An optimization technique that stores the results of expensive function calls and returns the cached result when the same inputs occur again.
- **Best Practices**: Use for problems with overlapping subproblems to avoid redundant calculations.
- **Efficiency**: Most efficient for problems with overlapping subproblems. Less efficient when there are no overlapping subproblems.
- **Edge Cases**: Large inputs with many overlapping subproblems.
- **Examples**:
  <details>
    <summary>Memoization Example</summary>

    ```python
    def fib_memo(n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 2:
            return 1
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        return memo[n]

    # Regular Implementation
    fib_value = fib_memo(1000)

    # Best Practices Implementation: Using functools.lru_cache for memoization
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def fib_memo_lru(n):
        if n <= 2:
            return 1
        return fib_memo_lru(n-1) + fib_memo_lru(n-2)

    fib_value = fib_memo_lru(1000)
    ```

    **Worst-Case Example**: Calculating large Fibonacci numbers without memoization.
    ```python
    def fib(n):
        if n <= 2:
            return 1
        return fib(n-1) + fib(n-2)

    fib_value = fib(30)
    ```
  </details>

#### Tabulation
- **Description**: An optimization technique that builds a table in a bottom-up manner and solves subproblems before solving the main problem.
- **Best Practices**: Use for problems with overlapping subproblems and when a bottom-up approach is feasible.
- **Efficiency**: Most efficient for problems with overlapping subproblems. Less efficient when there are no overlapping subproblems.
- **Edge Cases**: Large tables leading to high memory usage.
- **Examples**:
  <details>
    <summary>Tabulation Example</summary>

    ```python
    def fib_tab(n):
        if n <= 2:
            return 1
        fib_table = [0] * (n + 1)
        fib_table[1] = fib_table[2] = 1
        for i in range(3, n + 1):
            fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
        return fib_table[n]

    # Regular Implementation
    fib_value = fib_tab(1000)

    # Best Practices Implementation: Using a pre-allocated list for large tables
    def fib_tab_optimized(n):
        if n <= 2:
            return 1
        fib_table = [1] * (n + 1)
        for i in range(3, n + 1):
            fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
        return fib_table[n]

    fib_value = fib_tab_optimized(1000)
    ```

    **Worst-Case Example**: Calculating large Fibonacci numbers with tabulation.
    ```python
    fib_value = fib_tab(1000)
    ```
  </details>

### Divide and Conquer
- **Packages to Import**: None

#### Merge Sort
- **Description**: A stable, divide-and-conquer algorithm that divides the array into halves, sorts each half, and merges them.
- **Best Practices**: Use when a stable sort is required, and when working with large data sets that don't fit in memory (external sorting).
- **Efficiency**: Most efficient for large datasets due to its stable time complexity. Less efficient due to higher space complexity.
- **Edge Cases**: Lists with a large number of elements.
- **Examples**:
  <details>
    <summary>Merge Sort Example</summary>

    ```python
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
    
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # Regular Implementation
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = merge_sort(arr)

    # Best Practices Implementation: Using a cached version for repeated sorting
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def merge_sort_cached(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_cached(tuple(arr[:mid]))
        right = merge_sort_cached(tuple(arr[mid:]))
        return merge(left, right)

    arr = tuple([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    sorted_arr = merge_sort_cached(arr)
    ```

    **Worst-Case Example**: Sorting large lists with merge sort.
    ```python
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = merge_sort(arr)
    ```
  </details>

#### Quick Sort
- **Description**: A fast, divide-and-conquer algorithm that selects a pivot element and partitions the array into subarrays.
- **Best Practices**: Use for general-purpose sorting, especially when average-case performance is more important than worst-case performance.
- **Efficiency**: Most efficient when the pivot divides the list into balanced subarrays. Less efficient when the pivot results in highly unbalanced partitions.
- **Edge Cases**: When the list is already sorted or contains many duplicate elements, leading to unbalanced partitions.
- **Examples**:
  <details>
    <summary>Quick Sort Example</summary>

    ```python
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

    # Regular Implementation
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sorted_arr = quick_sort(arr)

    # Best Practices Implementation: Using a cached version for repeated sorting
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def quick_sort_cached(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort_cached(tuple(left)) + tuple(middle) + quick_sort_cached(tuple(right))

    arr = tuple([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    sorted_arr = quick_sort_cached(arr)
    ```

    **Worst-Case Example**: When the list is already sorted in ascending or descending order.
    ```python
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sorted_arr = quick_sort(arr)
    ```
  </details>


# Summary of Differences for Python Data Types

| Feature               | List                       ****         | SortedList (sortedcontainers)               | Dictionary                                  | Set                                    | Tuple                                | array (array module)                | deque                              | Counter                            | defaultdict                        | OrderedDict                        | NumPy Arrays                       | Pandas DataFrames                  | Stack                              | Queue                              | Linked List                        | HashMap                            | HashSet                            | Tree                                | Graph                              |
|-----------------------|-------------------------------------|---------------------------------------------|---------------------------------------------|----------------------------------------|--------------------------------------|-------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|-------------------------------------|------------------------------------|
| **Type Flexibility**  | Can store different types           | Homogeneous (one type)                      | Keys must be immutable; values can be any type | Can store different types               | Can store different types             | Homogeneous (one type)              | Can store different types           | Can store different types           | Can store different types           | Can store different types           | Homogeneous (one type)             | Columns can store different types  | Can store different types          | Can store different types          | Can store different types           | Keys must be immutable; values can vary | Unique elements only               | Can store different types          | Can store different types          |
| **Order**             | Ordered                             | Ordered                                     | Unordered                                   | Unordered                              | Ordered                              | Ordered                             | Ordered                            | Unordered                          | Unordered                           | Ordered                            | Ordered                            | Ordered                            | Ordered                            | Ordered                            | Ordered                             | Unordered                           | Unordered                          | Depends on implementation          | Unordered                          |
| **Mutability**        | Mutable                             | Mutable                                     | Mutable                                     | Mutable                                | Immutable                            | Mutable                             | Mutable                            | Mutable                            | Mutable                             | Mutable                            | Mutable                            | Mutable                            | Mutable                            | Mutable                            | Mutable                             | Mutable                             | Mutable                           | Mutable                             | Mutable                            |
| **Duplicates**        | Allows duplicates                   | Allows duplicates                           | Keys must be unique; values can duplicate   | No duplicates allowed                  | Allows duplicates                    | Allows duplicates                   | Allows duplicates                   | Allows duplicates                   | Allows duplicates                   | Keys must be unique; values can duplicate | Allows duplicates                 | Allows duplicates                  | Allows duplicates                  | Allows duplicates                  | Allows duplicates                   | Keys unique; values can duplicate  | No duplicates allowed              | Allows duplicates                  | Allows duplicates                  |
| **Memory Efficiency** | Less memory efficient               | Less memory efficient                       | Less memory efficient                       | Less memory efficient                  | More memory efficient                | More memory efficient               | Less memory efficient               | Less memory efficient               | Less memory efficient               | Less memory efficient               | Highly memory efficient            | Less memory efficient              | Less memory efficient              | Less memory efficient              | Moderate efficiency                 | Moderate efficiency                 | Less memory efficient              | Less memory efficient               | Depends on graph representation    |
| **Performance**       | Slower for numerical operations     | Efficient for maintaining sorted order      | Average O(1) for insert, lookup, delete     | Average O(1) for insert, lookup, delete | Faster access for fixed collections   | Faster for numerical operations      | Fast append and pop operations      | Fast tally operations               | Fast key-value pair operations      | Fast key-value pair operations      | Optimized for numerical operations | Optimized for data manipulation    | Fast push/pop                      | Fast enqueue/dequeue               | O(1) append; O(n) traversal         | O(1) average                       | O(1) average                       | Depends on tree type (e.g., O(log n) for balanced trees) | O(1)-O(E) for adjacency list ops   |
| **Functionality**     | General-purpose                     | Sorted collections                          | Efficient key-value pair operations         | Efficient membership tests             | Fixed collection of elements         | Basic numerical operations           | Double-ended queue operations       | Counting elements                   | Default values for missing keys     | Remembers the order of keys         | Extensive mathematical operations  | Data analysis and manipulation     | Stack operations                   | Queue operations                   | Traversal, dynamic insertions       | Fast key-value lookups             | Membership tests                   | Traversals, searching               | Pathfinding, traversal             |
| **Usage**             | General data storage                | Efficiently maintain a sorted list          | Fast lookup, insertion, deletion of key-value pairs | Removing duplicates, membership testing | Read-only collections, function returns | Efficient numerical data storage    | Efficient appending and popping     | Tallying elements                   | Grouping data with default values   | Fast iteration and reordering       | Scientific computing, large datasets | Tabular data analysis and manipulation | Use for LIFO operations            | Use for FIFO operations            | Use for dynamically sized collections | Use for fast lookups               | Use for collections with unique elements | Use for representing hierarchical relationships | Use for complex relational data    |
| **Typical Methods**   | append, insert, remove, sort, reverse | add, remove, bisect_left, bisect_right      | get, setdefault, keys, values, items        | add, remove, union, intersection        | count, index                         | append, remove, pop, extend          | append, appendleft, pop, popleft    | update, elements, most_common       | __missing__, setdefault             | move_to_end                         | reshape, slice, aggregate           | groupby, merge, pivot              | push, pop                          | enqueue, dequeue                   | append, remove, display             | get, setdefault, keys, items       | add, remove, clear                 | add_child, remove_child            | add_edge, remove_edge              |
| **Best Practices**    | Use for ordered collections of mixed data types, avoid excessive appending | Use for maintaining sorted order efficiently | Use for fast key-value access, ensure keys are immutable | Use for unique collections, membership tests | Use for fixed collections, return multiple values from functions | Use for numerical data when memory efficiency is needed | Use for queue operations where both ends are accessed frequently | Use for counting items, tracking occurrences | Use when default values are needed for missing keys | Use when key order is important | Use for numerical computations that require efficient memory use | Use for large-scale data analysis and manipulation | Use for LIFO operations            | Use for FIFO operations            | Use for dynamically sized collections | Use for fast lookups               | Use for collections with unique elements | Use for representing hierarchical relationships | Use for complex relational data    |
| **Efficiency**        | General-purpose, less efficient for numerical ops | Efficient for maintaining sorted order      | Most efficient for operations involving key-value pairs, less efficient with many collisions | Efficient for uniqueness and membership, less efficient for large data with many updates | Highly efficient for fixed collections, better memory use | Highly efficient for numerical operations | Efficient for double-ended queue operations | Efficient for counting, less so for other operations | Efficient for handling missing keys, less so for other operations | Efficient for maintaining order, less so for other operations | Highly efficient for numerical computations | Highly efficient for data manipulation | Efficient for LIFO use            | Efficient for FIFO use             | Moderate efficiency                 | Most efficient for key-based access | Efficient for membership testing    | Efficient with balanced trees       | Depends on graph representation    |
| **Edge Cases**        | Large lists with frequent insertions/deletions | Large sorted lists with frequent updates    | Large dictionaries with many collisions     | Large sets with many updates           | Large tuples are memory efficient but immutable | Large arrays can still be memory efficient but lack flexibility | Large deques with frequent appends/pops can still be efficient | Large Counters with many distinct items | Large defaultdicts with many missing keys | Large OrderedDicts with many updates can become less efficient | Large NumPy arrays are highly efficient, but lack flexibility | Large DataFrames can become memory intensive | Large stacks with many pushes/pops | Large queues with many enqueues    | Large lists can become slower for insertions | Large maps with high collision rates | Large sets with many updates        | Deep trees may lead to stack overflow | Highly connected graphs can be memory intensive |

### Examples

<details>
<summary>Python Code Example</summary>

```python
# List
my_list = [1, 2, 3, "a", [4, 5, 6]]
my_list.append(7)
print(my_list)  # Output: [1, 2, 3, 'a', [4, 5, 6], 7]
# Time Complexity: O(1) for append operation.
# Space Complexity: O(n), where n is the number of elements in the list.

# SortedList (sortedcontainers)
from sortedcontainers import SortedList
my_sorted_list = SortedList([4, 1, 7, 3])
my_sorted_list.add(2)
print(my_sorted_list)  # Output: SortedList([1, 2, 3, 4, 7])
# Time Complexity: O(log n) for insertion.
# Space Complexity: O(n), where n is the number of elements in the list.

# Dictionary (HashMap in Python)
my_dict = {"key1": "value1", "key2": "value2"}
my_dict["key3"] = "value3"
print(my_dict)  # Output: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# Time Complexity: O(1) average for insert and lookup.
# Space Complexity: O(n), where n is the number of key-value pairs.

# Set (HashSet in Python)
my_set = {1, 2, 3, 3, 4}
my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}
# Time Complexity: O(1) for add operation.
# Space Complexity: O(n), where n is the number of unique elements.

# Tuple
my_tuple = (1, 2, 3, "a", [4, 5, 6])
print(my_tuple)  # Output: (1, 2, 3, 'a', [4, 5, 6])
# Time Complexity: O(1) for access.
# Space Complexity: O(n), where n is the number of elements in the tuple.

# array (array module)
import array
my_array = array.array('i', [1, 2, 3, 4])
my_array.append(5)
print(my_array)  # Output: array('i', [1, 2, 3, 4, 5])
# Time Complexity: O(1) for append operation.
# Space Complexity: O(n), where n is the number of elements.

# deque
from collections import deque
my_deque = deque([1, 2, 3, 4])
my_deque.append(5)
my_deque.appendleft(0)
print(my_deque)  # Output: deque([0, 1, 2, 3, 4, 5])
# Time Complexity: O(1) for append and appendleft.
# Space Complexity: O(n), where n is the number of elements.

# Counter
from collections import Counter
my_counter = Counter('abracadabra')
print(my_counter)  # Output: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
# Time Complexity: O(n), where n is the length of the input.
# Space Complexity: O(k), where k is the number of unique elements.

# defaultdict
from collections import defaultdict
my_defaultdict = defaultdict(int)
my_defaultdict['a'] += 1
print(my_defaultdict)  # Output: defaultdict(<class 'int'>, {'a': 1})
# Time Complexity: O(1) for setting/accessing keys.
# Space Complexity: O(n), where n is the number of unique keys.

# OrderedDict
from collections import OrderedDict
my_ordered_dict = OrderedDict()
my_ordered_dict['a'] = 1
my_ordered_dict['b'] = 2
print(my_ordered_dict)  # Output: OrderedDict([('a', 1), ('b', 2)])
# Time Complexity: O(1) for insert and lookup.
# Space Complexity: O(n), where n is the number of key-value pairs.

# NumPy Arrays
import numpy as np
my_numpy_array = np.array([1, 2, 3, 4])
my_numpy_array = my_numpy_array + 1
print(my_numpy_array)  # Output: [2 3 4 5]
# Time Complexity: O(n) for element-wise operations.
# Space Complexity: O(n), where n is the number of elements.

# Pandas DataFrames
import pandas as pd
data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)
# Output:
#       name  age
# 0    Alice   25
# 1      Bob   30
# 2  Charlie   35
# Time Complexity: O(n) for creating DataFrame, where n is the number of rows.
# Space Complexity: O(n), where n is the number of rows.

# Stack
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # Output: [1, 2, 3]
stack.pop()
print(stack)  # Output: [1, 2]
# Time Complexity: O(1) for push and pop.
# Space Complexity: O(n), where n is the number of elements.

# Queue
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # Output: deque([1, 2, 3])
queue.popleft()
print(queue)  # Output: deque([2, 3])
# Time Complexity: O(1) for enqueue and dequeue.
# Space Complexity: O(n), where n is the number of elements.

# Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # Output: 1 -> 2 -> 3 -> None
# Time Complexity: O(1) for append; O(n) for traversal.
# Space Complexity: O(n), where n is the number of nodes.

# HashMap (Dictionary in Python)
my_hashmap = {"a": 1, "b": 2, "c": 3}
my_hashmap["d"] = 4
print(my_hashmap)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Time Complexity: O(1) average for insert and lookup.
# Space Complexity: O(n), where n is the number of key-value pairs.

# HashSet (Set in Python)
my_hashset = {1, 2, 3, 4, 5}
my_hashset.add(6)
print(my_hashset)  # Output: {1, 2, 3, 4, 5, 6}
# Time Complexity: O(1) for add operation.
# Space Complexity: O(n), where n is the number of unique elements.

# Tree (Binary Tree Example)
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

inorder_traversal(root)  # Output: 4 2 5 1 3
# Time Complexity: O(n), where n is the number of nodes.
# Space Complexity: O(h), where h is the height of the tree due to recursion stack.

# Graph
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

bfs(graph, "A")  # Output: A B C D E F
# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
# Space Complexity: O(V), where V is the number of vertices.

</details>