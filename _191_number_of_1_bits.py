class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.hammingWeight(0b00000000000000000000000000001011))
