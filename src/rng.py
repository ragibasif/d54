import random
import string
import re

class rng:
    def __init__(self, seed=69):
        self.rng = random.Random(seed)

    def integers(self, n, a, b):
        return [self.rng.randint(a, b) for _ in range(n)]

    def floats(self, n, a, b):
        return [self.rng.uniform(a, b) for _ in range(n)]

    def permutation(self, n):
        seq = list(range(1, n + 1))
        self.rng.shuffle(seq)
        return seq

    def matrix(self, n, m=None, a=1, b=10):
        m = m or n
        return [[self.rng.randint(a, b) for _ in range(m)] for _ in range(n)]

    def matrix_zero_diagonal(self, n, a=1, b=10):
        return [
            [0 if r == c else self.rng.randint(a, b) for c in range(n)]
            for r in range(n)
        ]

    def symmetric_matrix(self, n, a=1, b=10):
        matrix = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(r + 1):
                value = self.rng.randint(a, b)
                matrix[r][c] = matrix[c][r] = value
        return matrix

    def tree(self, n, depth: str = "shallow") -> list[tuple[int, int]]:
        """Generate random tree on n vertices (0 to n-1).
        depth: 'shallow' (default), 'deep', or 'path'
        """
        if n <= 1:
            return []
        if depth == "path":
            alpha = 0
        elif depth == "deep":
            alpha = 3
        else:
            alpha = n
        return [(self.rng.randint(max(0, i - alpha), i), i + 1) for i in range(n - 1)]

    def graph(self, n, connected=False) -> set[tuple[int, int]]:
        """Generate random graph on n vertices (0 to n-1).
        If connected=True, guarantees connectivity by including a random spanning tree.
        """
        graph = {(i, j) for i in range(n) for j in range(i) if self.rng.randint(0, 1)}
        if connected and n > 1:
            tree = {(min(u, v), max(u, v)) for u, v in self.tree(n)}
            graph |= tree
        return graph

    def string(self, n, charset="ABCabc123"):
        """Generate random string of length n from given charset."""
        return "".join(self.rng.choice(charset) for _ in range(n))

    def string_uppercase(self, n):
        return "".join(self.rng.choice(string.ascii_uppercase) for _ in range(n))

    def string_lowercase(self, n):
        return "".join(self.rng.choice(string.ascii_lowercase) for _ in range(n))

    def string_alphanumeric(self, n):
        return "".join(self.rng.choice(string.ascii_letters + string.digits) for _ in range(n))

    def string_regex(self, n, pattern):
        """Generate random string of length n matching regex pattern.
        Example: pattern = r'[A-Za-z0-9]'
        """
        regex = re.compile(pattern)
        charset = "".join(chr(c) for c in range(256) if regex.match(chr(c)))
        if not charset:
            raise ValueError(f"No characters match pattern: {pattern}")
        return "".join(self.rng.choice(charset) for _ in range(n))

    @staticmethod
    def format_matrix(matrix: list[list[int]], separator: str = " ") -> str:
        """Format matrix as string with rows on separate lines."""
        return "\n".join(separator.join(map(str, row)) for row in matrix)
