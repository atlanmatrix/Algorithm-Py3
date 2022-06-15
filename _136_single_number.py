import collections
from typing import List
from functools import reduce
from operator import xor


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)

    def singleNumber2(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common()[-1][0]

    def singleNumber3(self, nums: List[int]) -> int:
        l = {}
        for i in nums:
            if i in l:
                del l[i]
            else:
                l[i] = None
        return list(l)[0]


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2,2,1]))
    print(s.singleNumber([4,1,2,1,2]))
    print(s.singleNumber([1]))
