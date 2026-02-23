import time
import logging
import inspect
import re
from functools import wraps

logging.basicConfig(level=logging.DEBUG, format="[%(filename)s:%(lineno)d] %(message)s")
logger = logging.getLogger(name=__name__)


def log(*args)->None:
    frame = inspect.currentframe().f_back
    var_names = inspect.getframeinfo(frame).code_context[0].strip()

    # Extract variable names from the log() call

    match = re.search(r"log\((.*)\)", var_names)
    if match:
        names = [n.strip() for n in match.group(1).split(",")]
        for name, value in zip(names, args):
            logger.debug(f"{name} = {value}")
    else:
        for i, value in enumerate(args):
            logger.debug(f"arg{i} = {value}")




def trace(func):
    """Decorator to trace recursive functions."""
    level = 0

    @wraps(wrapped=func)
    def wrapper(*args, **kwargs):
        nonlocal level
        indent = "  | " * level
        arg_str = ", ".join(map(repr, args))
        print(f"{indent}+-- {func.__name__}({arg_str})")
        level += 1
        res = func(*args, **kwargs)
        level -= 1
        print(f"{indent}+-- return {repr(res)}")
        return res

    return wrapper


def timer(func):
    """Decorator to time functions."""

    @wraps(wrapped=func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = end - start
        print(f"[{func.__name__}] {duration:.4f}s ({duration * 1000:.2f}ms)")
        return result

    return wrapper



