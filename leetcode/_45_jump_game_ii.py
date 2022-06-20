from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        for idx, item in enumerate(nums[1:], 1):
            nums[idx] = idx + item if idx + item > nums[idx - 1] else nums[idx - 1]

        r, step = nums[0], 1
        while r < len(nums) - 1:
            r, step = nums[r], step + 1
        return step


if __name__ == "__main__":
    s = Solution()
    print(s.jump([1,2]))
    print(s.jump([2,3,0,1,4]))
