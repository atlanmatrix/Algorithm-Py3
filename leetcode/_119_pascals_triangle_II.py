from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        p = [1]
        for i in range(rowIndex):
            p = [0] + p + [0]
            tmp = []
            for i in range(len(p) - 1):
                tmp.append(p[i] + p[i + 1])
            p = tmp
        return p

if __name__ == "__main__":
    s = Solution()
    print(s.getRow(3))
