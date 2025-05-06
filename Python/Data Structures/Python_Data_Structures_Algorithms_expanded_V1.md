# Python Data Structures, Algorithms, and Best Practices

## 1. Built-in Data Structures

### 1.1 Lists
- **Usage**: Ordered collection of items, supports indexing, slicing, and iteration.
- **Common Algorithms**:
  - **Sorting**:
    - **Quick Sort**: Efficient sorting algorithm with average case O(n log n) time complexity. It uses a divide-and-conquer strategy by selecting a pivot element and partitioning the array.
      ```python
      def quick_sort(arr):
          if len(arr) <= 1:
              return arr
          pivot = arr[len(arr) // 2]
          left = [x for x in arr if x < pivot]
          middle = [x for x in arr if x == pivot]
          right = [x for x in arr if x > pivot]
          return quick_sort(left) + middle + quick_sort(right)
      ```
    - **Merge Sort**: A stable, divide-and-conquer algorithm with O(n log n) time complexity, which splits the list into halves, sorts each half, and merges them.
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
              if left[i] < right[j]:
                  result.append(left[i])
                  i += 1
              else:
                  result.append(right[j])
                  j += 1
          result.extend(left[i:])
          result.extend(right[j:])
          return result
      ```
    - **Tim Sort**: Python’s built-in `sorted` function uses Tim Sort, which is a hybrid sorting algorithm derived from merge sort and insertion sort.
      ```python
      arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
      sorted_arr = sorted(arr)  # Uses Tim Sort internally
      ```

  - **Searching**:
    - **Linear Search**: Simple search algorithm with O(n) time complexity, iterates through each element until the target is found.
      ```python
      def linear_search(arr, target):
          for i in range(len(arr)):
              if arr[i] == target:
                  return i
          return -1
      ```
    - **Binary Search**: More efficient search algorithm with O(log n) time complexity, requires a sorted list.
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
      ```

  - **Best Practices**: Use list comprehensions for concise and readable code; avoid excessive appending in loops for large data to improve performance.
    ```python
    squares = [x**2 for x in range(10)]  # List comprehension for concise code
    ```

### 1.2 Tuples
- **Usage**: Immutable ordered collection of items.
- **Common Algorithms**:
  - **Hashing**: Often used as keys in dictionaries because they are immutable.
    ```python
    person_info = {("John", "Doe"): 12345, ("Jane", "Smith"): 67890}
    ```
  - **Best Practices**: Use for fixed collections of related items; prefer over lists for read-only purposes to ensure data integrity.
    ```python
    coordinates = (10, 20)  # Tuple for fixed coordinates
    ```

### 1.3 Dictionaries
- **Usage**: Key-value pairs, efficient lookup, insertion, and deletion.
- **Common Algorithms**:
  - **Hashing**: Dictionary operations (insert, lookup) typically O(1) due to hash tables.
    ```python
    phone_book = {"Alice": "123-456-7890", "Bob": "987-654-3210"}
    ```
  - **Best Practices**: Use dictionary comprehensions; ensure keys are immutable types.
    ```python
    squares = {x: x**2 for x in range(10)}  # Dictionary comprehension
    ```

### 1.4 Sets
- **Usage**: Unordered collection of unique items.
- **Common Algorithms**:
  - **Set Operations**: Union, Intersection, Difference (all O(1) average case).
    ```python
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    union = set_a | set_b  # Union
    intersection = set_a & set_b  # Intersection
    difference = set_a - set_b  # Difference
    ```
  - **Best Practices**: Use sets to eliminate duplicates and perform membership tests efficiently.
    ```python
    unique_numbers = set([1, 2, 2, 3, 4])  # Set to eliminate duplicates
    ```

## 2. Collections Module

### 2.1 deque (Double-ended queue)
- **Usage**: Supports O(1) append and pop operations from both ends.
- **Common Algorithms**:
  - **Sliding Window**: Useful in problems involving a moving window of elements.
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
    ```
  - **Best Practices**: Use `deque` for queue-like operations to avoid O(n) operations of lists.
    ```python
    dq = deque([1, 2, 3])
    dq.appendleft(0)
    dq.append(4)
    ```

### 2.2 Counter
- **Usage**: Count the frequency of elements.
- **Common Algorithms**:
  - **Frequency Analysis**: Counting occurrences in strings, lists.
    ```python
    from collections import Counter

    text = "hello world"
    count = Counter(text)
    ```
  - **Best Practices**: Use `Counter` for tallying elements; supports most common operations directly.
    ```python
    elements = [1, 2, 2, 3, 3, 3]
    counter = Counter(elements)
    ```

### 2.3 defaultdict
- **Usage**: Dictionary with default values for non-existing keys.
- **Common Algorithms**:
  - **Grouping**: Aggregating data under a common key.
    ```python
    from collections import defaultdict

    def group_by_key(pairs):
        d = defaultdict(list)
        for key, value in pairs:
            d[key].append(value)
        return dict(d)
    ```
  - **Best Practices**: Simplifies code by avoiding key existence checks.
    ```python
    word_lengths = defaultdict(int)
    for word in ["hello", "world"]:
        word_lengths[word] += len(word)
    ```

## 3. Array Module

### 3.1 array
- **Usage**: Compact, fixed-type arrays.
- **Common Algorithms**:
  - **Numeric Operations**: Efficient storage and manipulation of numeric data.
    ```python
    import array

    arr = array.array('i', [1, 2, 3, 4])
    arr.append(5)
    ```
  - **Best Practices**: Use when memory efficiency and fixed-type array constraints are necessary.
    ```python
    float_array = array.array('f', [1.0, 2.0, 3.0])
    ```

## 4. NumPy Arrays

- **Usage**: Multi-dimensional arrays for numerical computations.
- **Common Algorithms**:
  - **Matrix Operations**: Linear algebra, element-wise operations.
    ```python
    import numpy as np

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    dot_product = np.dot(a, b)
    ```
  - **Best Practices**: Utilize broadcasting and vectorized operations for performance.
    ```python
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    sum_matrix = a + b  # Broadcasting and vectorized operation
    ```

## 5. Pandas DataFrames

- **Usage**: Tabular data structure, similar to SQL tables or Excel spreadsheets.
- **Common Algorithms**:
  - **Data Analysis**: Aggregation, filtering, merging, group-by operations.
    ```python
    import pandas as pd

    data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}
    df = pd.DataFrame(data)
    grouped = df.groupby('age').size()
    ```
  - **Best Practices**: Leverage built-in functions and avoid loops for data manipulation.
    ```python
    df['age_squared'] = df['age'].apply(lambda x: x**2)
    ```

## 6. Custom Data Structures

### 6.1 Linked Lists
- **Usage**: Dynamic data structure with efficient insertions/deletions.
- **Common Algorithms**:
  - **Traversal**: Iterating over elements.
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
    ```
  - **Best Practices**: Use when frequent insertions/deletions are required; implement using classes.

### 6.2 Stacks
- **Usage**: LIFO (Last In, First Out) structure.
- **Common Algorithms**:
  - **Expression Evaluation**: Parsing expressions, backtracking.
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
    ```
  - **Best Practices**: Use lists or `deque` for stack operations.

### 6.3 Queues
- **Usage**: FIFO (First In, First Out) structure.
- **Common Algorithms**:
  - **BFS (Breadth-First Search)**: Tree/graph traversal.
    ```python
    class Queue:
        def __init__(self):
            self.items = []

        def enqueue(self, item):
            self.items.insert(0, item)

        def dequeue(self):
            return self.items.pop()

        def is_empty(self):
            return len(self.items) == 0

        def size(self):
            return len(self.items)
    ```
  - **Best Practices**: Use `deque` for queue operations to ensure O(1) performance.

### 6.4 Priority Queues
- **Usage**: Elements with priorities, typically implemented with heaps.
- **Common Algorithms**:
  - **Dijkstra's Algorithm**: Shortest path in graphs.
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
    ```
  - **Best Practices**: Use `heapq` module for priority queue operations.

## 7. Graphs

- **Usage**: Nodes connected by edges.
- **Common Algorithms**:
  - **DFS (Depth-First Search), BFS, Dijkstra's, A***: Various traversal and pathfinding algorithms.
    - **DFS**:
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
      ```
    - **BFS**:
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
      ```
    - **Dijkstra's**:
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
      ```
    - **A***:
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
      ```
  - **Best Practices**: Use adjacency lists for sparse graphs; adjacency matrices for dense graphs.

## Best Practices for Algorithms

- **Sorting**: Choose the appropriate algorithm based on input size and characteristics (e.g., Timsort for general purpose, Quick Sort for smaller arrays).
  ```python
  arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
  sorted_arr = sorted(arr)  # Uses Tim Sort internally
