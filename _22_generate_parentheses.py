from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s_l = []

        def dfs(s, rest_l, rest_r):
            if rest_l == 0 and rest_r == 0:
                s_l.append(s)

            if rest_l:
                dfs(s + '(', rest_l-1, rest_r)

            if rest_l < rest_r:
                dfs(s + ')', rest_l, rest_r-1)
        dfs('', n, n)

        return s_l

    def generateParenthesis2(self, n: int) -> List[str]:
        def generate(rest_l, rest_r):
            if rest_l == 0:
                if rest_r != 0:
                    return [')' + char for char in generate(rest_l, rest_r - 1)]
                else:
                    return ['']

            if rest_l == rest_r:
                return ['(' + char for char in generate(rest_l - 1, rest_r)]
            elif rest_l < rest_r:
                return ['(' + char for char in generate(rest_l - 1, rest_r)] + [')' + char for char in generate(rest_l, rest_r - 1)]
            else:
                pass

        return generate(n, n)


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
