# d54

For educational and recreational purposes only.

## Python

- Strings are immutable and that's why they can be used as keys to dictionaries
- Use `''.join(list_of_strings)` instead of repeated `s += char` since that will create new copies of the string
- For local documentation: use `help()` in the shell
- Use `enumerate()` to loop over a list to get the index and the item
- Get the key and the value when looping over a dictionary with `.items()`
- With a dictionary, if the value doesn't exist `[]` will throw a `KeyError` whereas
  `get()` will default to `None`
- `.sort()` sorts a list in place and `sorted()` returns a sorted _copy_ (uses Timsort)
- Sets are mutable, to get an immutable set that can be used for keys in dicts,
  use `frozenset`
- Deque - when you need a queue or list you can push and pop from either side
- Default Python recursion depth is about 1024 frames
- Infinity: `float("inf")`, `float("-inf")`, `math.inf`, `-math.inf`
- `Counter`: frequency maps `collections.Counter(arr)`
- `deque`: O(1) append/pop from both ends (essential for BFS)
- `defaultdict`: avoids KeyError for graphs or counts `collections.defaultdict(list)`
- Python's `heapq` is a min-heap by default. To use a max-heap, multiply values by `-1`.
- Tuples: are immutable, they can be used as keys to hash map/set
- Reverse a string: `s[::-1]`
- ASCII Conversion: `ord('a')` → 97, `chr(97)` → 'a'
- Infinity: `float('inf')` and `float('-inf')` or `math.inf` and `-math.inf`
- Divmod: `q, r = divmod(10, 3)` (Returns 3,1)
- GCD: `math.gcd(a,b)`
- LCM: `math.lcm(a,b)`
- Fast Power/Mod: `pow(base, exp, mod)` is faster than `(base**exp) % mod`
- Fast Grid Initialization: `grid = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]`
- nCr: `math.comb(n,r)`
- nPr: `math.perm(n,r)`
- Combinations: `itertools.combinations([1,2,3], 2)` → (1,2), (1,3), (2,3)
- Permutations: `itertools.permutations([1,2,3])`
- Integer Square Root: `math.isqrt(n)` is faster than `int(n**0.5)`
- Reverse a list: `list[::-1]`
- `defaultdict` default infinity: `d = defaultdict(lambda: math.inf)`
- handle wraparounds with mod, for circular arrays the next element after `i` is always `(i+1)%n`
- recursive functions can benefit from the builtin `@cache` decorator in `functools`: `from functools import cache`

### Bit Manipulation

- Get i-th bit: `(x >> i) & 1`
- Set i-th bit: `x | (1 << i)`
- Clear i-th bit: `x & ~(1 << i)`
- Check if power of 2: `n > 0 and (n & (n - 1)) == 0`
- XOR Property: `a ^ a = 0`, `a ^ b = 1` if a != b
- Check if even number: `( n & 1 ) == 0`
- Check if odd number: `( n & 1 ) == 1`
- Clear the lowest set bit: `n & (n - 1)`
- Get the lowest set bit: `n & -n`

### Math

- Division is iterated subtraction.
- Multiplication is iterated addition.
- Exponentiation is iterated multiplication.
- Logarithms are iterated division.
- Sum of first `n` natural numbers: `( n * ( n + 1 ) ) // 2`
- Sum of first `n` odd natural numbers: `n * n`
- Sum of first `n` even natural numbers: `n * (n + 1)`
- Even number: `n = 2k`
- Odd number: `n = 2k + 1`

```python
def gcd(a:int, b:int)->int:
    while b:
        a, b = b, a % b
    return a

def lcm(a:int, b:int)->int: return a * b // gcd(a=a,b= b)
```

### NP-Complete

- NP-Complete Problems:
  - Traveling Salesperson Problem (TSP)
  - Longest Path Problem
  - Hamiltonian Path Problem
  - Graph Coloring Problem
  - The Knapsack Problem
  - Subset Sum Problem

### Two Pointers

- Input:
    - one or two arrays, strings, linked lists
    - sorted input
    - modify input in place
- Algorithm:
    - use `O(1)` extra memory
    - naive solution: `O(n²)` time
    - optimal solution: `O(n)` time
- Technique:
    - inward pointers
    - slow and fast pointers
    - parallel pointers
- Keywords:
    - palindrome
    - reverse
    - swap
    - merge
    - partition
- Bugs:
    - off by one errors

### 2D Arrays (Grids & Matrices)

```python

def in_bounds(row, col, ROWS, COLS):
    return 0 <= row  and row < ROWS and 0 <= col and col < COLS

# Directions

"""
4-dir adjacent: the + shape      →  (±1,0), (0,±1) -> one of dr or dc is 0
4-dir diagonal: the x shape      →  (±1,±1)        -> both dr and dc are nonzero
8-dir:          the 3x3 grid     →  all combos of {-1,0,1} × {-1,0,1} except (0,0)
Knight:         L = 2+1 squares  →  all combos of {±1,±2} × {±2,±1}  (|dr|+|dc|==3, dr≠dc)
King:           8-dir, 1 step
Queen:          8-dir, infinite steps (while in bounds)
Rook:           4-dir adjacent, infinite steps
Bishop:         4-dir diagonal, infinite steps
"""

# 4 Directions

adjacent = [(-1,0),(1,0),(0,-1),(0,1)] # +

diagonal = [(-1,-1),(-1,1),(1,-1),(1,1)] # x

# 8 Directions

dirs = [(-1,-1),(-1,0),(-1,1),
        ( 0,-1),        (0,1),
        ( 1,-1),( 1,0),( 1,1)]

# Or compact:
dirs = [(dr,dc) for dr in range(-1,2) for dc in range(-1,2) if (dr,dc) != (0,0)]

for dr, dc in dirs:
    nr, nc = r + dr, c + dc

# Knight

knight = [(-2,-1),(-2,1),(-1,-2),(-1,2),
          ( 1,-2),( 1,2),( 2,-1),( 2, 1)]

for (int dr = -2; dr <= 2; dr++)
    for (int dc = -2; dc <= 2; dc++)
        if (abs(dr) + abs(dc) == 3 && abs(dr) != abs(dc))
            // valid knight move

for dr, dc in knight:
    nr, nc = r + dr, c + dc

king = [(dr,dc) for dr in range(-1,2) for dc in range(-1,2) if (dr,dc) != (0,0)]

queen = [(dr,dc) for dr in range(-1,2) for dc in range(-1,2) if (dr,dc) != (0,0)]

for dr, dc in queen:
    nr, nc = r + dr, c + dc
    while 0 <= nr < ROWS and 0 <= nc < COLS:
        # process cell
        nr += dr
        nc += dc

```
- Vocabulary:
    - Transposition: the first row becomes the first column, the second row becomes the second column, and so on
    - Rotation: A transformation that turns the matrix 90 degrees, clockwise or counterclockwise
    - Horizontal reflection: the first column becomes the last column, the second column becomes second last, and so on.
    - Vertical reflection: The first row becomes the last row, the second row becomes the second last, and so on.
- Remember:
    - Check if row and col are in bounds after calculating the new row and column
- Bugs:
    - out-of-bounds errors
- Flattening:
    - mapping 2D to 1D: `[r, c] -> r * COLS + c`
    - mapping 1D to 2D: `i -> [i // COLS, i % COLS]`



