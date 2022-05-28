class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        if num == 0:
            return count
        while num > 1:
            if num % 2 == 0:
                count += 1
            else:
                count += 2
            num //= 2
        count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.numberOfSteps(14))
    print(s.numberOfSteps(8))
    print(s.numberOfSteps(123))
