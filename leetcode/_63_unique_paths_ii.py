from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        res_lst = [[1 for _ in range(n)] for _ in range(m)]

        is_zero = False
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                is_zero = True
            if is_zero:
                res_lst[i][0] = 0
        is_zero = False
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                is_zero = True
            if is_zero:
                res_lst[0][i] = 0
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    res_lst[i][j] = 0
                else:
                    res_lst[i][j] = res_lst[i - 1][j] + res_lst[i][j - 1]

        return res_lst[-1][-1]


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePathsWithObstacles([[1]]))
