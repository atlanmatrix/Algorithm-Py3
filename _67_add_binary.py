class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = ''
        tmp = '0'


        if len(a) > len(b):
            b = '0' * abs(len(a) - len(b)) + b
        else:
            a = '0' * abs(len(a) - len(b)) + a

        for i in range(len(a)):
            if a[-i - 1] == b[-i - 1] == '0':
                s = tmp + s
                tmp = '0'
            elif a[-i - 1] == b[-i - 1] == '1':
                s = tmp + s
                tmp = '1'
            else:
                if tmp == '0':
                    s = '1' + s
                else:
                    s = '0' + s
        if tmp == '1':
            s = '1' + s
        return s


if __name__ == "__main__":
    s = Solution()
    print(s.addBinary('11', '1'))
    print(s.addBinary('1010', '1011'))
