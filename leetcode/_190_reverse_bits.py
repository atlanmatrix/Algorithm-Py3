class Solution:
    def reverseBits(self, n: int) -> int:
        sum = 0
        for _ in range(32):
            sum *= 2
            sum += n & 1
            n >>= 1

        return sum


if __name__ == "__main__":
    s = Solution()
    print(s.reverseBits(0b00000010100101000001111010011100))
    print(s.reverseBits(0b11111111111111111111111111111101))
