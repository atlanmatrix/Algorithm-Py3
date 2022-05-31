import string
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def dfs(d):
            if not d:
                return []
            return [c + s for c in m[d[0]] for s in dfs(d[1:]) or ['']]

        return dfs(digits)

    def letterCombinations2(self, digits: str) -> List[str]:
        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = ['']
        for digit in digits:
            if digit in m:
                res = [s + char for s in res for char in m[digit]]
        return res if res != [''] else []


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations('23'))
    print(s.letterCombinations(''))
    print(s.letterCombinations('2'))
