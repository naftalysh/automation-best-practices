# Ensure inputs are lists with exactly three elements
assert (
    isinstance(a, list) and len(a) == 3
), "Input 'a' must be a list with exactly 3 elements"
assert (
    isinstance(b, list) and len(b) == 3
), "Input 'b' must be a list with exactly 3 elements"

# Add assertions for value range
assert all(1 <= x <= 100 for x in a), "All elements must satisfy 1 <= a[i] <= 100"
assert all(1 <= x <= 100 for x in b), "All elements must satisfy 1 <= b[i] <= 100"
