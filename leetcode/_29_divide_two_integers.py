import math


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        val = dividend / divisor
        if val > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if val < - 2 ** 31:
            return - 2 ** 31
        val = math.ceil(val) if val < 0 else math.floor(val)
        return val

