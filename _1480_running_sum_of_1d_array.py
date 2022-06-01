from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        return [s := s + v for v in nums]


if __name__ == "__main__":
    s = Solution()
    print(s.runningSum([1,2,3,4]))
    print(s.runningSum([1,1,1,1,1]))
    print(s.runningSum([3,1,2,10,1]))
