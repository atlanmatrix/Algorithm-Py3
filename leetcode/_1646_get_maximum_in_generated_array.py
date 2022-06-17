class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        res_lst = [0, 1] + [0 for _ in range(n - 1)]
        max_val = -1
        for i in range(2, n + 1):
            if i % 2 == 0:
                res_lst[i] = res_lst[i // 2]
            else:
                res_lst[i] = res_lst[((i - 1) // 2) + 1] + res_lst[((i - 1) // 2)]
            max_val = max(max_val, res_lst[i])

        return max_val


if __name__ == "__main__":
    s = Solution()
    # print(s.getMaximumGenerated(7))
    # print(s.getMaximumGenerated(2))
    # print(s.getMaximumGenerated(3))
    print(s.getMaximumGenerated(15))
