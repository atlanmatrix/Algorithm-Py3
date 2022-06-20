from typing import List, Union


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i - 1], 0)
        return max(nums)

    def maxSubArray2(self, nums: List[int]) -> int:
        max_sum = -1e8
        curr_sum = 0

        for i in nums:
            curr_sum += i
            if curr_sum > max_sum:
                max_sum = curr_sum

            if curr_sum < 0:
                curr_sum = 0
        return max_sum


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(s.maxSubArray([1]))
    print(s.maxSubArray([5,4,-1,7,8]))
    print(s.maxSubArray([-2, 1]))
