from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res_lst = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                res = nums[i] + nums[l] + nums[r]
                if res < 0:
                    l += 1
                elif res > 0:
                    r -= 1
                else:
                    res_lst.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

        return res_lst


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))
    print(s.threeSum([0, 0, 0]))
    print(s.threeSum([0]))
    print(s.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))
