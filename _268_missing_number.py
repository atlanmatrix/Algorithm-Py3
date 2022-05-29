from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (int(n * (n + 1) / 2) - sum(nums))

    def missingNumber2(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.missingNumber([3,0,1]))
    print(s.missingNumber([0,1]))
    print(s.missingNumber([9,6,4,2,3,5,7,0,1]))
