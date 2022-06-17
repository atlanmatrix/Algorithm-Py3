import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_val = math.inf
        for val in prices:
            if val < min_val:
                min_val = val

            if val - min_val > profit:
                profit = val - min_val

        return profit


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))
