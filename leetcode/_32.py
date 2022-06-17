class Solution:
    def longestValidParentheses(self, s: str) -> int:
        curr = 0
        stack = []
        res_stack = []

        for char in s:
            if char == ')':
                if not stack:
                    res_stack.append(-1)
                    continue
                stack.pop()
                curr += 2
            else:
                stack.append('(')

            if not stack:
                res_stack.append(curr)

        res_stack.append(curr)
        ano_max = 0
        prev = None
        for i in res_stack:
            if prev is None:
                prev = i
            else:
                if i > 0 and prev > 0:
                    prev += i
                else:
                    prev = i
            # print(prev)
            ano_max = max(prev, ano_max)
        return ano_max


if __name__ == "__main__":
    s = Solution()
    print(s.longestValidParentheses("(()(((()"))
    print(s.longestValidParentheses("(()"))
    print(s.longestValidParentheses(")()())"))
    print(s.longestValidParentheses(""))
    print(s.longestValidParentheses("()(()"))
