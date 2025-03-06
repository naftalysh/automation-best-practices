# Snippet 1
# Summary: Quick Sort Example
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


# Snippet 2
# Summary: Merge Sort Example
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
        if left[i] < right[j]:
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


# Snippet 3
# Summary: Tim Sort Example
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


# Snippet 4
# Summary: Linear Search Example
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


# Snippet 5
# Summary: Binary Search Example
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


# Snippet 6
# Summary: Best Practices Example
squares = [x**2 for x in range(10)]  # List comprehension for concise code
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Snippet 7
# Summary: Thread-Safe Implementation Example
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


# Snippet 8
# Summary: Hashing Example
person_info = {("John", "Doe"): 12345, ("Jane", "Smith"): 67890}

# Regular Implementation
person_info = {("John", "Doe"): 12345, ("Jane", "Smith"): 67890}
print(person_info)  # Output: {('John', 'Doe'): 12345, ('Jane', 'Smith'): 67890}

# Best Practices Implementation: Using a namedtuple for readability
from collections import namedtuple

Person = namedtuple('Person', ['first_name', 'last_name'])
person_info = {Person("John", "Doe"): 12345, Person("Jane", "Smith"): 67890}
print(person_info)  # Output: {Person(first_name='John', last_name='Doe'): 12345, Person(first_name='Jane', last_name='Smith'): 67890}


# Snippet 9
# Summary: Best Practices Example
coordinates = (10, 20)  # Tuple for fixed coordinates
print(coordinates)  # Output: (10, 20)


# Snippet 10
# Summary: Thread-Safe Implementation Example
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



# Snippet 11
# Summary: Hashing Example
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


# Snippet 12
# Summary: Best Practices Example
squares = {x: x**2 for x in range(10)}  # Dictionary comprehension
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


# Snippet 13
# Summary: Thread-Safe Implementation Example
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


# Snippet 14
# Summary: Set Operations Example
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


# Snippet 15
# Summary: Best Practices Example
unique_numbers = set([1, 2, 2, 3, 4])  # Set to eliminate duplicates
print(unique_numbers)  # Output: {1, 2, 3, 4}


# Snippet 16
# Summary: Thread-Safe Implementation Example
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


# Snippet 17
# Summary: max_sliding_window
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


# Snippet 18
# Summary: Best Practices Example
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)  # Output: deque([0, 1, 2, 3, 4])


# Snippet 19
# Summary: Frequency Analysis Example
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


# Snippet 20
# Summary: Best Practices Example
elements = [1, 2, 2, 3, 3, 3]
counter = Counter(elements)
print(counter)  # Output: Counter({3: 3, 2: 2, 1: 1})


# Snippet 21
# Summary: Thread-Safe Implementation Example
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


# Snippet 22
# Summary: Grouping Example
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


# Snippet 23
# Summary: Best Practices Example
word_lengths = defaultdict(int)
for word in ["hello", "world"]:
    word_lengths[word] += len(word)

print(word_lengths)  # Output: defaultdict(<class 'int'>, {'hello': 5, 'world': 5})


# Snippet 24
# Summary: Thread-Safe Implementation Example
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


# Snippet 25
# Summary: Maintaining Order Example
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


# Snippet 26
# Summary: Best Practices Example
d = OrderedDict([('one', 1), ('two', 2), ('three', 3)])

print(d)  # Output: OrderedDict([('one', 1), ('two', 2), ('three', 3)])


# Snippet 27
# Summary: Thread-Safe Implementation Example
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


# Snippet 28
# Summary: max_sliding_window
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


# Snippet 29
# Summary: min_sliding_window
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


# Snippet 30
# Summary: sum_of_subarray with array
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



# Snippet 31
# Summary: sum_of_subarray with deque
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



# Snippet 32
# Summary: longest_substring_without_repeating with array
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



# Snippet 33
# Summary: longest_substring_without_repeating with deque
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



# Snippet 34
# Summary: min_subarray_length_with_sum with array
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



# Snippet 35
# Summary: min_subarray_length_with_sum with deque
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



# Snippet 36
# Summary: Best Practices Example
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)  # Output: deque([0, 1, 2, 3, 4])


# Snippet 37
# Summary: Thread-Safe Implementation Example
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


# Snippet 38
# Summary: Numeric Operations Example
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


# Snippet 39
# Summary: Best Practices Example
float_array = array.array('f', [1.0, 2.0, 3.0])
print(float_array)  # Output: array('f', [1.0, 2.0, 3.0])


# Snippet 40
# Summary: Thread-Safe Implementation Example
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


# Snippet 41
# Summary: Matrix Operations Example
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


# Snippet 42
# Summary: Best Practices Example
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


# Snippet 43
# Summary: Thread-Safe Implementation Example
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


# Snippet 44
# Summary: Data Analysis Example
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


# Snippet 45
# Summary: Best Practices Example
df['age_squared'] = df['age'].apply(lambda x: x**2)

# Expected Output: DataFrame with a new column 'age_squared'
print(df.head())  # Output: First 5 rows of the DataFrame
                  #       name  age  age_squared
                  # 0    Alice   25          625
                  # 1    Alice   25          625
                  # 2    Alice   25          625
                  # 3    Alice   25          625
                  # 4    Alice   25          625


# Snippet 46
# Summary: Thread-Safe Implementation Example
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


# Snippet 47
# Summary: SortedList Example
from sortedcontainers import SortedList

sl = SortedList([3, 1, 4, 1, 5, 9, 2, 6])
sl.add(7)
print(sl)  # Output: SortedList([1, 1, 2, 3, 4, 5, 6, 7, 9])


# Snippet 48
# Summary: heappush Example
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
print(heap)  # Output: [1, 3, 4]


# Snippet 49
# Summary: heappop Example
import heapq

heap = [1, 3, 4]
smallest = heapq.heappop(heap)
print(smallest)  # Output: 1
print(heap)  # Output: [3, 4]


# Snippet 50
# Summary: itertools Example
import itertools

perms = list(itertools.permutations([1, 2, 3]))
print(perms)  # Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]


# Snippet 51
# Summary: functools Example
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Output: 55


# Snippet 52
# Summary: Traversal Example
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


# Snippet 53
# Summary: Thread-Safe Implementation Example
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


# Snippet 54
# Summary: Expression Evaluation Example
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


# Snippet 55
# Summary: BFS Example
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


# Snippet 56
# Summary: Dijkstra's Algorithm Example
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


# Snippet 57
# Summary: Thread-Safe Implementation Example
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


# Snippet 58
# Summary: DFS Example
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


# Snippet 59
# Summary: BFS Example
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


# Snippet 60
# Summary: Dijkstra's Algorithm Example
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


# Snippet 61
# Summary: A* Algorithm Example
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


# Snippet 62
# Summary: Thread-Safe Implementation Example
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


# Snippet 63
# Summary: Quick Sort Example
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


# Snippet 64
# Summary: Merge Sort Example
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


# Snippet 65
# Summary: Tim Sort Example
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = sorted(arr)  # Uses Tim Sort internally

# Regular Implementation
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = sorted(arr)

# Best Practices Implementation: Sorting large datasets with multiple runs
large_arr = [i % 10 for i in range(1000000)]
sorted_large_arr = sorted(large_arr)


# Snippet 66
# Summary: Linear Search Example
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


# Snippet 67
# Summary: Binary Search Example
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


# Snippet 68
# Summary: BFS Example
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


# Snippet 69
# Summary: DFS Example
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


# Snippet 70
# Summary: Memoization Example
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


# Snippet 71
# Summary: Tabulation Example
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


# Snippet 72
# Summary: Merge Sort Example
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


# Snippet 73
# Summary: Quick Sort Example
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


