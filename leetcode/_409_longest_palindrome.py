from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = defaultdict(int)

        for char in s:
            counter[char] += 1

        has_odd = False
        final_sum = 0
        print(counter)
        for char in counter:
            if counter[char] % 2 == 0:
                final_sum += counter[char]
            else:
                final_sum += counter[char]
                if not has_odd:
                    has_odd = True
                else:
                    final_sum -= 1
        return final_sum


if __name__ == '__main__':
    s = Solution()
    # print(s.longestPalindrome('abccccdd'))
    print(s.longestPalindrome("adam"))
