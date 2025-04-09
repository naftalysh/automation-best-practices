Q1: What is GIL?
Q2: differenct between generator and iterator?
Q3: What is a predicate?


### **Q1: What is GIL (Global Interpreter Lock)?**
The **Global Interpreter Lock (GIL)** is a mutex (lock) that protects access to Python objects and prevents multiple native threads from executing Python bytecodes simultaneously. This means that even if a Python program is multi-threaded, only **one thread can execute Python code at a time** in CPython (the most common Python interpreter).

**Why does Python have a GIL?**
- Python's memory management (specifically reference counting in CPython) is not thread-safe. The GIL ensures only one thread modifies reference counts at a time.
- It simplifies memory management but limits true parallel execution for CPU-bound tasks.

**How to overcome the GIL?**
- Use **multiprocessing** instead of threading for CPU-bound tasks.
- Use external libraries like **NumPy**, **Numba**, or **Cython**, which release the GIL for performance optimization.
- Use **Jython** or **IronPython**, which don’t have a GIL.

---

### **Q2: Difference between Generator and Iterator?**
Both **generators** and **iterators** are used to produce sequences of values lazily (on demand) but have key differences:

| Feature      | Iterator | Generator |
|-------------|---------|-----------|
| Definition  | An object that implements `__iter__()` and `__next__()` methods | A function that contains `yield` instead of `return` |
| How it's created? | By defining a class with `__iter__()` and `__next__()` | By defining a function using `yield` |
| Memory Usage | Stores all elements in memory | Produces values lazily, consuming less memory |
| State Retention | Does not retain state between calls | Retains state between `yield` calls |
| Example | ``` class MyIterator: def __init__(self, n): self.n = n self.current = 0 def __iter__(self): return self def __next__(self): if self.current < self.n: self.current += 1 return self.current else: raise StopIteration ``` | ``` def my_generator(n): for i in range(n): yield i gen = my_generator(5) ``` |

**Use case difference:**
- **Use an iterator** when you need full control over iteration logic.
- **Use a generator** when working with large data sets where memory efficiency matters.

---

### **Q3: What is a Predicate?**
A **predicate** is a function that **returns a boolean value** (`True` or `False`) based on a given input. It is commonly used in filtering, searching, and decision-making.

**Examples of Predicates:**
1. A simple predicate function:
   ```python
   def is_even(n):
       return n % 2 == 0
   print(is_even(4))  # True
   print(is_even(7))  # False
   ```

2. Using predicates with `filter()`:
   ```python
   numbers = [1, 2, 3, 4, 5, 6]
   evens = list(filter(is_even, numbers))
   print(evens)  # [2, 4, 6]
   ```

3. Predicate as a lambda function:
   ```python
   words = ["apple", "banana", "cherry"]
   starts_with_b = list(filter(lambda word: word.startswith('b'), words))
   print(starts_with_b)  # ['banana']
   ```

**Common Use Cases:**
- Filtering collections (`filter()`)
- Condition checking in loops or list comprehensions
- Functional programming (e.g., predicates in `any()`, `all()`, `sorted()` with `key`)

---

Would you like further examples or a deeper explanation of any of these topics? 🚀