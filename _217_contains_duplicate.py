from typing import List


class Solution:
    # Also, use Counter, use sorted and find duplicate item are good ideas
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i in d:
                return True
            d[i] = [i]
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1,2,3,1]))
    print(s.containsDuplicate([1,2,3,4]))
    print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
