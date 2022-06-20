import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(math.factorial(m + n - 2) / (math.factorial(m - 1) * math.factorial(n - 1)))

    def uniquePaths3(self, m: int, n: int) -> int:
        res_lst = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                res_lst[i][j] = res_lst[i - 1][j] + res_lst[i][j - 1]
        return res_lst[-1][-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        i = j = 1
        d = {}
        def dfs(i, j):
            if i == m and j == n:
                return 1
            total = 0
            if i < m:
                if (i + 1, j) not in d:
                    d[(i + 1, j)] = dfs(i + 1, j)
                total += d[(i + 1, j)]
            if j < n:
                if (i, j + 1) not in d:
                    d[(i, j + 1)] = dfs(i, j + 1)
                total += d[(i, j + 1)]
            return total

        return dfs(i, j)


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(23, 12))
    print(s.uniquePaths(3, 2))
