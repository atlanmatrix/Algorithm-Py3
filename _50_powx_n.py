class Solution:
    def myPow(self, x: float, n: int) -> float:
        sum = 1.0
        if n > 0:
            if x == 0:
                return 0
            if x == 1:
                return 1
            if x == -1:
                return 1 if n % 2 == 0 else -1
            
            while n:
                sum *= x
                if 0 < sum < 0.000000000001:
                    return sum
                n -= 1
        elif n == 0:
            pass
        else:
            if x == 0:
                return 0
            if x == 1:
                return 1
            if x == -1:
                return 1 if n % 2 == 0 else -1
            
            while n:
                sum /= x
                if 0 < sum < 0.000000000001:
                    return sum
                n += 1

        return sum