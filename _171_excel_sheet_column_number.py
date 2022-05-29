class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        sum = 0
        for char in columnTitle:
            sum *= 26
            sum += ord(char) - 64
        return sum


if __name__ == "__main__":
    s = Solution()
    print(s.titleToNumber('A'))
    print(s.titleToNumber('AB'))
    print(s.titleToNumber('ZY'))
