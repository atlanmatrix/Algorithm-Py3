from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row_size = len(grid)
        col_size = len(grid[0])

        def out_of_range(x, y):
            if x < 0 or y < 0 or x >= row_size or y >= col_size:
               return False

            return True

        def water_flow(x, y):
            if not out_of_range(x, y):
                return 1
            if grid[x][y] == 0:
                return 1
            return 0

        perimeter = 0
        for i in range(row_size):
            for j in range(col_size):
                if grid[i][j] == 1:
                    perimeter += water_flow(i - 1, j)
                    perimeter += water_flow(i + 1, j)
                    perimeter += water_flow(i, j - 1)
                    perimeter += water_flow(i, j + 1)
                    grid[i][j] = 2
                    # print(i, j, perimeter)
        return perimeter


if __name__ == "__main__":
    s = Solution()
    print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
    print(s.islandPerimeter([[1]]))
    print(s.islandPerimeter([[1,0]]))
