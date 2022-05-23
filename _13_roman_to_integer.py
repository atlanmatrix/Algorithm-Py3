class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        sum = 0

        symbol_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        while i < len(s) - 1:
            if symbol_int_map[s[i]] < symbol_int_map[s[i+1]]:
                sum -= symbol_int_map[s[i]]
            else:
                sum += symbol_int_map[s[i]]
            i += 1
        sum += symbol_int_map[s[i]]
        return sum


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt('III'))
    print(s.romanToInt('LVIII'))
    print(s.romanToInt('MCMXCIV'))
