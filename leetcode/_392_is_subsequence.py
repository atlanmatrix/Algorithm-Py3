class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(c in t for c in s)

    def isSubsequence2(self, s: str, t: str) -> bool:
        while True:
            if not s:
                return True
            if not t and s:
                return False
            for i in range(len(t)):
                if t[i] == s[0]:
                    s = s[1:]
                    t = t[i + 1:]
                    break
            else:
                return False
