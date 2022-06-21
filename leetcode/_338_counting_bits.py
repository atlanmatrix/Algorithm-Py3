import math
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        note = {
            0: [0],
        }

        def dfs(k):
            if k in note:
                return note[k]

            note[k] = dfs(k - 1) + [x + 1 for x in dfs(k - 1)]
            return note[k]

        k = int(math.log2(n + 1)) + 1
        res = dfs(k)
        return res[:n + 1]



    def countBits2(self, n: int) -> List[int]:
        res = [0]

        while len(res) < n + 1:
            res += [x + 1 for x in res]
        return res[:n + 1]


if __name__ == "__main__":
    s = Solution()
    # print(s.countBits(32))
    # print(s.countBits(1))
    # print(s.countBits(2))
    # print(s.countBits(3))
    # print(s.countBits(4))
    # print(s.countBits(5))
    # print(s.countBits(6))
    # print(s.countBits(7))
    print(s.countBits2(8))
