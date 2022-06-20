from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = 0
        for idx, item in enumerate(nums):
            step = max(step, idx + item)
            if step >= len(nums) - 1:
                return True
            if step == idx:
                return False
        return False