#!/usr/bin/env python3

import signal
import math
import heapq
from collections import deque, defaultdict, Counter
import itertools
from typing import NoReturn
# my libs
from rng import rng
from dbg import dbg
from bits import bits
from utils import log,timer,trace
from ListNode import ListNode
from TreeNode import TreeNode

MOD = 10**9 + 7
EPS = 1e-9


def solve()->None:

    return


def main()->None:
    def handler(signum, frame)->NoReturn:
        raise Exception("TLE: Test took too long!")

    signal.signal(signalnum=signal.SIGALRM, handler=handler)

    signal.alarm(2) # set timer to error if taking longer than 2 seconds

    solve()

    signal.alarm(0) # reset timer


if __name__ == "__main__":
    main()
