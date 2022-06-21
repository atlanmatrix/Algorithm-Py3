class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_valid_char(char):
            return '0' <= char <= '9' or 'a' <= char <= 'z' or 'A' <= char <= 'Z'

        s = ''.join([char.lower() for char in s if is_valid_char(char)])
        return s == s[::-1]

    def isPalindrome2(self, s: str) -> bool:
        def is_valid_char(char):
            return '0' <= char <= '9' or 'a' <= char <= 'z'

        st = 0
        ed = len(s) - 1
        while st < ed:
            st_v = s[st].lower()
            ed_v = s[ed].lower()
            while not is_valid_char(st_v):
                st += 1
                st_v = s[st].lower()
                if st >= ed:
                    break

            while not is_valid_char(ed_v):
                ed -= 1
                ed_v = s[ed].lower()
                if st >= ed:
                    break

            if st < ed and st_v != ed_v:
                return False

            st += 1
            ed -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))
    print(s.isPalindrome(""))
    print(s.isPalindrome(".,"))
