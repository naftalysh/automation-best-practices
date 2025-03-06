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

## 1. Built-in Data Structures

### 1.1 Lists
- **Usage**: Ordered collection of items, supports indexing, slicing, and iteration.
- **Common Algorithms**:
  - **Sorting**:
    - **Quick Sort**: A fast, divide-and-conquer algorithm that selects a pivot element and partitions the array into subarrays. Average case O(n log n), worst case O(n^2), space complexity O(log n).
      <details>
        <summary>Quick Sort Implementation</summary>

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

        **Worst-Case Example**:
        ```python
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted_arr = quick_sort(arr)
        ```
      </details>

    - **Merge Sort**: A stable, divide-and-conquer algorithm that divides the array into halves, sorts each half, and merges them. Time complexity O(n log n), space complexity O(n).
      <details>
        <summary>Merge Sort Implementation</summary>

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

        **Worst-Case Example**:
        ```python
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_arr = merge_sort(arr)
        ```
      </details>

    - **Tim Sort**: A hybrid sorting algorithm derived from merge sort and insertion sort, used by Python's built-in `sorted()` function. Time complexity O(n log n), space complexity O(n).
      <details>
        <summary>Tim Sort Implementation</summary>

        ```python
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_arr = sorted(arr)  # Uses Tim Sort internally
        ```

        **Worst-Case Example**:
        ```python
        arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        sorted_arr = sorted(arr)
        ```
      </details>

  - **Searching**:
    - **Linear Search**: A simple search algorithm that checks each element until the target is found. Time complexity O(n), space complexity O(1).
      <details>
        <summary>Linear Search Implementation</summary>

        ```python
        def linear_search(arr, target):
            for i in range(len(arr)):
                if arr[i] == target:
                    return i
            return -1
        ```

        **Worst-Case Example**:
        ```python
        arr = [1, 2, 3, 4, 5]
        index = linear_search(arr, 6)
        ```
      </details>

    - **Binary Search**: An efficient search algorithm that works on sorted arrays by repeatedly dividing the search interval in half. Time complexity O(log n), space complexity O(1).
      <details>
        <summary>Binary Search Implementation</summary>

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

        **Worst-Case Example**:
        ```python
        arr = [1, 2, 3, 4, 5]
        index = binary_search(arr, 6)
        ```
      </details>

  - **Best Practices**: Use list comprehensions for concise and readable code; avoid excessive appending in loops for large data to improve performance.
    <details>
      <summary>Best Practices Example</summary>

      ```python
      squares = [x**2 for x in range(10)]  # List comprehension for concise code
      ```
    </details>

### 1.2 Tuples
- **Usage**: Immutable ordered collection of items.
- **Common Algorithms**:
  - **Hashing**: Often used as keys in dictionaries because they are immutable. O(1) average, O(n) worst-case time complexity for lookup, O(1) space complexity.
    <details>
      <summary>Hashing Example</summary>

      ```python
      person_info = {("John", "Doe"): 12345, ("Jane", "Smith"): 67890}
      ```

      **Worst-Case Example**:
      ```python
      large_tuple = tuple(range(1000000))
      person_info = {large_tuple: 12345}
      ```
    </details>
  - **Best Practices**: Use for fixed collections of related items; prefer over lists for read-only purposes to ensure data integrity.
    <details>
      <summary>Best Practices Example</summary>

      ```python
      coordinates = (10, 20)  # Tuple for fixed coordinates
      ```
    </details>

### 1.3 Dictionaries
- **Usage**: Key-value pairs, efficient lookup, insertion, and deletion.
- **Common Algorithms**:
  - **Hashing**: Dictionary operations (insert, lookup) typically O(1) average case due to hash tables, O(n) worst-case time complexity, O(n) space complexity.
    <details>
      <summary>Hashing Example</summary>

      ```python
      phone_book = {"Alice": "123-456-7890", "Bob": "987-654-3210"}
      ```

      **Worst-Case Example**:
      ```python
      large_dict = {i: i for i in range(1000000)}
      value = large_dict[999999]
      ```
    </details>
  - **Best Practices**: Use dictionary comprehensions; ensure keys are immutable types.
    <details>
      <summary>Best Practices Example</summary>

      ```python
      squares = {x: x**2 for x in range(10)}  # Dictionary comprehension
      ```
    </details>

### 1.4 Sets
- **Usage**: Unordered collection of unique items.
- **Common Algorithms**:
  - **Set Operations**: Union, Intersection, Difference (all O(1) average case, O(n) worst-case time complexity, O(n) space complexity).
    <details>
      <summary>Set Operations Example</summary>

      ```python
      set_a = {1, 2, 3, 4}
      set_b = {3, 4, 5, 6}
      union = set_a | set_b  # Union
      intersection = set_a & set_b  # Intersection
      difference = set_a - set_b  # Difference
      ```

      **Worst-Case Example**:
      ```python
      large_set_a = set(range(1000000))
      large_set_b = set(range(500000, 1500000))
      union = large_set_a | large_set_b
      ```
    </details>
  - **Best Practices**: Use sets to eliminate duplicates and perform membership tests efficiently.
    <details>
      <summary>Best Practices Example</summary>

      ```python
      unique_numbers = set([1, 2, 2, 3, 4])  # Set to eliminate duplicates
      ```
    </details>

## 2. Collections Module

### 2.1 deque (Double-ended queue)
- **Usage**: Supports O(1) append and pop operations from both ends.
- **Common Algorithms**:
  - **Sliding Window**: Useful in problems involving a moving window of elements. O(n) time complexity, O(k) space complexity.
    <details>
      <summary>Sliding Window Example</summary>

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

      **Worst-Case Example**:
      ```python
      nums = [i for i in range(100000)]
      k = 50000
      max_values = max_sliding_window(nums, k)
      ```
    </details>
  - **Best Practices**: Use `deque` for queue-like operations to avoid O(n) operations of lists.
    <details>
      <summary>Best Practices Example</summary>

      ```python
      dq = deque([1, 2, 3])
      dq.appendleft(0)
      dq.append(4)
      ```
    </details>

### 2.2 Counter
- **Usage**: Count the frequency of elements.
- **Common Algorithms**:
  - **Frequency Analysis**: Counting occurrences in strings, lists. O(n) time complexity, O(n) space complexity.
    <details>
      <summary>Frequency Analysis Example</summary>

      ```python
      from collections import Counter

      text = "hello world"
      count = Counter(text)
      ```

      **Worst-Case Example**:
      ```python
      large_text = "a" * 1000000
      count = Counter(large_text)
      ```
    </details>
  - **Best Practices**: Use `Counter` for tallying elements; supports most common operations directly.
    <details>
      <summary>Best Practices Example</summary>

      ```python
      elements = [1, 2, 2, 3, 3, 3]
      counter = Counter(elements)
      ```
    </details>

### 2.3 defaultdict
- **Usage**: Dictionary with default values for non-existing keys.
- **Common Algorithms**:
  - **Grouping**: Aggregating data under a common key. O(n) time complexity, O(n) space complexity.
    <details>
      <summary>Grouping Example</summary>

      ```python
      from collections import defaultdict

      def group_by_key(pairs):
          d = defaultdict(list)
          for key, value in pairs:
              d[key].append(value)
          return dict(d)
      ```

      **Worst-Case Example**:
      ```python
      pairs = [(i % 1000, i) for i in range(1000000)]
      grouped = group_by_key(pairs)
      ```
    </details>
  - **Best Practices**: Simplifies code by avoiding key existence checks.
    <details>
      <summary>Best Practices Example</summary>

      ```python
      word_lengths = defaultdict(int)
      for word in ["hello", "world"]:
          word_lengths[word] += len(word)
      ```
    </details>

## 3. Array Module

### 3.1 array
- **Usage**: Compact, fixed-type arrays.
- **Common Algorithms**:
  - **Numeric Operations**: Efficient storage and manipulation of numeric data. O(n) time complexity for traversal, O(1) space complexity.
    <details>
      <summary>Numeric Operations Example</summary>

      ```python
      import array

      arr = array.array('i', [1, 2, 3, 4])
      arr.append(5)
      ```

      **Worst-Case Example**:
      ```python
      large_array = array.array('i', range(1000000))
      large_array.append(1000000)
      ```
    </details>
  - **Best Practices**: Use when memory efficiency and fixed-type array constraints are necessary.
    <details>
      <summary>Best Practices Example</summary>

      ```python
      float_array = array.array('f', [1.0, 2.0, 3.0])
      ```
    </details>

## 4. NumPy Arrays

- **Usage**: Multi-dimensional arrays for numerical computations.
- **Common Algorithms**:
  - **Matrix Operations**: Linear algebra, element-wise operations. O(n^2) time complexity for matrix multiplication, O(n^2) space complexity.
    <details>
      <summary>Matrix Operations Example</summary>

      ```python
      import numpy as np

      a = np.array([1, 2, 3])
      b = np.array([4, 5, 6])
      dot_product = np.dot(a, b)
      ```

      **Worst-Case Example**:
      ```python
      a = np.ones((1000, 1000))
      b = np.ones((1000, 1000))
      result = np.dot(a, b)
      ```
    </details>
  - **Best Practices**: Utilize broadcasting and vectorized operations for performance.
    <details>
      <summary>Best Practices Example</summary>

      ```python
      a = np.array([[1, 2], [3, 4]])
      b = np.array([[5, 6], [7, 8]])
      sum_matrix = a + b  # Broadcasting and vectorized operation
      ```
    </details>

## 5. Pandas DataFrames

- **Usage**: Tabular data structure, similar to SQL tables or Excel spreadsheets.
- **Common Algorithms**:
  - **Data Analysis**: Aggregation, filtering, merging, group-by operations. O(n) time complexity, O(n) space complexity.
    <details>
      <summary>Data Analysis Example</summary>

      ```python
      import pandas as pd

      data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}
      df = pd.DataFrame(data)
      grouped = df.groupby('age').size()
      ```

      **Worst-Case Example**:
      ```python
      data = {'name': ['Alice']*1000000, 'age': [25]*1000000}
      df = pd.DataFrame(data)
      grouped = df.groupby('age').size()
      ```
    </details>
  - **Best Practices**: Leverage built-in functions and avoid loops for data manipulation.
    <details>
      <summary>Best Practices Example</summary>

      ```python
      df['age_squared'] = df['age'].apply(lambda x: x**2)
      ```
    </details>

## 6. Custom Data Structures

### 6.1 Linked Lists
- **Usage**: Dynamic data structure with efficient insertions/deletions.
- **Common Algorithms**:
  - **Traversal**: Iterating over elements. O(n) time complexity, O(1) space complexity.
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
      ```

      **Worst-Case Example**:
      ```python
      ll = LinkedList()
      for i in range(100000):
          ll.append(i)
      ll.print_list()
      ```
    </details>
  - **Best Practices**: Use when frequent insertions/deletions are required; implement using classes.

### 6.2 Stacks
- **Usage**: LIFO (Last In, First Out) structure.
- **Common Algorithms**:
  - **Expression Evaluation**: Parsing expressions, backtracking. O(n) time complexity, O(n) space complexity.
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
      ```

      **Worst-Case Example**:
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
    <details>
      <summary>BFS Example</summary>

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

      **Worst-Case Example**:
      ```python
      q = Queue()
      for i in range(100000):
          q.enqueue(i)
      while not q.is_empty():
          q.dequeue()
      ```
    </details>
  - **Best Practices**: Use `deque` for queue operations to ensure O(1) performance.

### 6.4 Priority Queues
- **Usage**: Elements with priorities, typically implemented with heaps.
- **Common Algorithms**:
  - **Dijkstra's Algorithm**: Shortest path in graphs. O((n + m) log n) time complexity, O(n) space complexity.
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
      ```

      **Worst-Case Example**:
      ```python
      pq = PriorityQueue()
      for i in range(100000):
          pq.push(i, i)
      while not pq.is_empty():
          pq.pop()
      ```
    </details>
  - **Best Practices**: Use `heapq` module for priority queue operations.

## 7. Graphs

- **Usage**: Nodes connected by edges.
- **Common Algorithms**:
  - **DFS (Depth-First Search), BFS, Dijkstra's, A***: Various traversal and pathfinding algorithms.
    - **DFS**: O(n + m) time complexity, O(n) space complexity.
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
        ```

        **Worst-Case Example**:
        ```python
        graph = {i: [i+1] for i in range(100000)}
        visited_nodes = dfs(graph, 0)
        ```
      </details>

    - **BFS**: O(n + m) time complexity, O(n) space complexity.
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
        ```

        **Worst-Case Example**:
        ```python
        graph = {i: [i+1] for i in range(100000)}
        visited_nodes = bfs(graph, 0)
        ```
      </details>

    - **Dijkstra's**: O((n + m) log n) time complexity, O(n) space complexity.
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
        ```

        **Worst-Case Example**:
        ```python
        graph = {i: {i+1: 1} for i in range(100000)}
        distances = dijkstra(graph, 0)
        ```
      </details>

    - **A***: O((n + m) log n) time complexity, O(n) space complexity.
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
        ```

        **Worst-Case Example**:
        ```python
        graph = {i: {i+1: 1} for i in range(100000)}
        h = lambda x: 0  # Heuristic function
        path = a_star(graph, 0, 99999, h)
        ```
      </details>
  - **Best Practices**: Use adjacency lists for sparse graphs; adjacency matrices for dense graphs.

## Best Practices for Algorithms

- **Sorting**: Choose the appropriate algorithm based on input size and characteristics (e.g., Timsort for general purpose, Quick Sort for smaller arrays).
  <details>
    <summary>Sorting Example</summary>

    ```python
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = sorted(arr)  # Uses Tim Sort internally
    ```

    **Worst-Case Example**:
    ```python
    arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    sorted_arr = sorted(arr)
    ```
  </details>

- **Searching**: Use binary search for sorted data; hash tables for fast lookups.
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
    ```

    **Worst-Case Example**:
    ```python
    arr = [1, 2, 3, 4, 5]
    index = binary_search(arr, 6)
    ```
  </details>

- **Graph Traversal**: Use BFS for shortest paths in unweighted graphs; DFS for connected components and cycles detection.
  <details>
    <summary>Graph Traversal Example</summary>

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

    **Worst-Case Example**:
    ```python
    graph = {i: [i+1] for i in range(100000)}
    visited_nodes = bfs(graph, 0)
    ```
  </details>

- **Dynamic Programming**: Use memoization for recursive solutions; tabulation for iterative solutions.
  <details>
    <summary>Dynamic Programming Example</summary>

    ```python
    def fib_memo(n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 2:
            return 1
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
        return memo[n]
    ```

    **Worst-Case Example**:
    ```python
    fib_value = fib_memo(1000)
    ```
  </details>

- **Divide and Conquer**: Apply to problems that can be broken into independent subproblems (e.g., Merge Sort, Quick Sort).
  <details>
    <summary>Divide and Conquer Example</summary>

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

    **Worst-Case Example**:
    ```python
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = merge_sort(arr)
    ```
  </details>
