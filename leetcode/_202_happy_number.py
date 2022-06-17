class Solution:
    def isHappy(self, n: int) -> bool:
        included_lst = []
        while n != 1:
            sum = 0
            while n > 0:
                n, i = divmod(n, 10)
                sum += pow(i, 2)
            n = sum
            if n in included_lst:
                return False
            included_lst.append(n)
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isHappy(19))
    print(s.isHappy(2))
