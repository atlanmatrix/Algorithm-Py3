class Solution:
    def intToRoman(self, num: int) -> str:
        s = ''

        symbol_int_map = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1,
        }

        for k, v in symbol_int_map.items():
            n, num = divmod(num, v)
            s += n * k

        return s


if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(3))
    print(s.intToRoman(58))
    print(s.intToRoman(1994))
