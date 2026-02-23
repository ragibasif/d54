#!/usr/bin/env python3

import signal
import math
import heapq
from collections import deque, defaultdict, Counter
import itertools
from functools import cache
# my libs
from rng import rng
from utils import log,timer,trace # timer and trace are decorators

MOD = 10**9 + 7
EPS = 1e-9

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"

def _listnode(head:ListNode=None)->str:
    if not head:
        return "None"
    res = []
    curr = head
    seen = set()
    bound = 25

    while curr:
        node_id = id(curr)
        if node_id in seen:
            res.append(f"Cycle({curr.val})")
            break

        seen.add(node_id)
        res.append(str(curr.val))
        curr = curr.next

        if len(res) >= bound:
            res.append("...")
            break

    if not curr and len(res) < bound + 1:
        res.append("None")

    res = " -> ".join(res)
    return f"{res}"


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        left_val = self.left.val if self.left else "null"
        right_val = self.right.val if self.right else "null"
        return f"TreeNode({self.val}, L:{left_val}, R:{right_val})"

def _treenode(root:TreeNode=None)->str:

    if not root:
        return "None"
    lines = []

    def _build(node, prefix="", is_left=True, is_root=True):
        if node is None:
            label = "(L)" if is_left else "(R)"
            # Using \-- for bottom (left) and /-- for top (right)
            connector = "\\-- " if is_left else "/-- "
            lines.append(f"{prefix}{connector}{label} [N]")
            return

        if node.right or node.left:
            _build(
                node.right,
                prefix + ("|       " if is_left and not is_root else "        "),
                False,
                False,
            )

        if is_root:
            connector = "ROOT--- "
        else:
            label = "(L)" if is_left else "(R)"
            connector = "\\-- " if is_left else "/-- "
            connector += label + " "

        lines.append(f"{prefix}{connector}{node.val}")

        if node.left or node.right:
            _build(
                node.left,
                prefix + ("        " if is_left or is_root else "|       "),
                True,
                False,
            )

    _build(root)
    return "\n" + "\n".join(lines) + "\n"

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b): return a * b // gcd(a, b)

def count_bits(x):
    bits = 0
    while x:
        bits += x & 1
        x >>= 1
    return bits

def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def is_even(x): return (x & 1) == 0
def is_odd(x): return (x & 1) != 0
def is_set(x, n): return (x & (1 << n)) == 1
def is_clear(x, n): return (x & (1 << n)) == 0
def get_bit(x, n): return (x >> n) & 1
def set_bit(x, n): return x | (1 << n)
def clear_bit(x, n): return x & ~(1 << n)
def toggle_bit(x, n): return x ^ (1 << n)
def clear_lowest_set_bit(x): return x & (x - 1)
def get_lowest_set_bit(x): return x & ~(x - 1)
def is_power_of_two(x): return x > 0 and clear_lowest_set_bit(x) == 0


def _bits(val,length=8):
    return f"{val:0>{length}b} ({val})"

def _matrix(grid, path=None):
    if not grid or not grid[0]: return ""

    path_set = set(path) if path else set()
    R, C = len(grid), len(grid[0])

    all_vals = []
    for row in grid:
        for val in row:
            all_vals.append(str(val))

    max_data_w = max(len(s) for s in all_vals)
    max_col_idx_w = len(str(C-1))
    cell_w = max(max_data_w, max_col_idx_w)
    full_cell_w = cell_w + 2
    row_idx_w = len(str(R-1))

    buf = []
    header_padding = " " * (row_idx_w + 3)
    header = header_padding + " ".join(str(c).center(full_cell_w) for c in range(C))
    buf.append(header)

    buf.append(" " * (row_idx_w + 2) + "-" * (len(header) - row_idx_w - 2))
    for r, row in enumerate(grid):
        line = []
        for c, val in enumerate(row):
            char = str(val)
            display = char.center(cell_w)
            if (r, c) in path_set:
                line.append(f"[{display}]")
            else:
                line.append(f" {display} ")
        buf.append(f"{str(r).rjust(row_idx_w)} | {' '.join(line)}")
    return "\n" + "\n".join(buf) + "\n"

@timer
@trace
@cache
def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def solve():

    return


def main():
    flag = False

    def handler(signum, frame):
        raise Exception("TLE: Test took too long!")

    signal.signal(signal.SIGALRM, handler)

    if flag:
        t = int(input())
        for _ in range(t):
            signal.alarm(2)
            solve()
            signal.alarm(0)
    else:
        signal.alarm(2)
        solve()
        signal.alarm(0)


if __name__ == "__main__":
    main()
