class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len(set([s[i: i + k] for i in range(len(s) - k + 1)])) == 2 ** k

    def hasAllCodes2(self, s: str, k: int) -> bool:
        for i in range(2 ** k):
            sub_s = str(bin(i))[2:].zfill(k)
            if sub_s not in s:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    # print(s.hasAllCodes('00110110', 2))
    # print(s.hasAllCodes('0110', 1))
    print(s.hasAllCodes('00110', 2))
    # print(s.hasAllCodes('00000000010011101', 4))
