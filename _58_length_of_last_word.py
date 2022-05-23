class Solution:
    def lengthOfLastWord2(self, s: str) -> int:
        return len(s.strip().split()[:-1])

    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if count > 0:
                    break
                else:
                    continue

            count += 1

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))
    print(s.lengthOfLastWord("   fly me   to   the moon  "))
    print(s.lengthOfLastWord("luffy is still joyboy"))
