class bits:
    def __init__(self) -> None:
        pass

    @staticmethod
    def count_bits(x:int)->int:
        bits = 0
        while x:
            bits += x & 1
            x >>= 1
        return bits

    @staticmethod
    def count_set_bits(n:int)->int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

    @staticmethod
    def is_even(x:int)-> bool: return (x & 1) == 0
    @staticmethod
    def is_odd(x:int)->bool: return (x & 1) != 0
    @staticmethod
    def is_set(x:int, n:int)->bool: return (x & (1 << n)) == 1
    @staticmethod
    def is_clear(x:int, n:int)->bool: return (x & (1 << n)) == 0
    @staticmethod
    def get_bit(x:int, n:int)->int: return (x >> n) & 1
    @staticmethod
    def set_bit(x:int, n:int)->int: return x | (1 << n)
    @staticmethod
    def clear_bit(x:int, n:int)->int: return x & ~(1 << n)
    @staticmethod
    def toggle_bit(x:int, n:int)->int: return x ^ (1 << n)
    @staticmethod
    def clear_lowest_set_bit(x:int)->int: return x & (x - 1)
    @staticmethod
    def get_lowest_set_bit(x:int)->int: return x & ~(x - 1)
    @staticmethod
    def is_power_of_two(x:int)->bool: return x > 0 and x&(x-1) == 0

