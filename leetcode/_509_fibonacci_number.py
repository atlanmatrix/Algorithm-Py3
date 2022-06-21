class Solution:
    note = {
        0: 0,
        1: 1
    }
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        a, b = 0, 1
        while n > 1:
            a, b = b, a + b
            n -= 1

        return b

    def fib2(self, n: int) -> int:
        if n < 2:
            return self.note[n]

        if n - 1 not in self.note:
            fn_1 = self.fib(n - 2) + self.fib(n - 3)
            self.note[n - 1] = fn_1
        return self.note[n - 1] + self.note[n - 2]
