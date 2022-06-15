from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        p = [1]
        for i in range(numRows):
            res.append(p.copy())
            p = [0] + p + [0]
            tmp = []
            for i in range(len(p) - 1):
                tmp.append(p[i] + p[i + 1])
            p = tmp
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))
