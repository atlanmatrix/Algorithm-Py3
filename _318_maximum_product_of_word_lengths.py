import string
import functools
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # convert letters to number(binary form)
        char_bin_map = {
            char: 1 << idx
            for idx, char in enumerate(string.ascii_lowercase)
        }

        def str_2_bin(s):
            bin_val = 0
            for char in s:
                bin_val |= char_bin_map[char]
            return bin_val

        max_val = 0
        new_words = [str_2_bin(word) for word in words]

        for i in range(len(new_words)):
            for j in range(i + 1, len(new_words)):
                # if string a do not share the same letters with string b
                # a & b will equals 0
                if not new_words[i] & new_words[j]:
                    max_val = max(max_val, len(words[i]) * len(words[j]))

        return max_val



    def maxProduct2(self, words: List[str]) -> int:
        max_val = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if len(set(words[i])) + len(set(words[j])) == len(set(words[i]) | set(words[j])):
                    max_val = max(max_val, len(words[i]) * len(words[j]))

        return max_val


if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
    print(s.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))
    print(s.maxProduct(["a","aa","aaa","aaaa"]))
