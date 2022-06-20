from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row_size, col_size = len(grid), len(grid[0])
        res = [[0 for _ in range(col_size)] for _ in range(row_size)]
        res[0][0] = grid[0][0]
        for col_idx in range(1, col_size):
            res[0][col_idx] = res[0][col_idx - 1] + grid[0][col_idx]
        for row_idx in range(1, row_size):
            res[row_idx][0] = res[row_idx - 1][0] + grid[row_idx][0]
        for i in range(1, row_size):
            for j in range(1, col_size):
                res[i][j] = min(res[i - 1][j], res[i][j - 1]) + grid[i][j]
        return res[-1][-1]


if __name__ == "__main__":
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    print(s.minPathSum([[1,2,3],[4,5,6]]))
