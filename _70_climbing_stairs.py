class Solution:
    cached = {
        1: 1,
        2: 2
    }

    def climbStairs(self, n: int) -> int:
        if n not in self.cached:
            self.cached[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.cached[n]


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(2))
    print(s.climbStairs(3))
