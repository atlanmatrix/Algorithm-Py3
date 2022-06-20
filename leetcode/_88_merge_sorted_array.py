

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = len(nums1) - 1
        idx1 = m - 1
        idx2 = n - 1

        while idx1 > -1 and idx2 > -1:
            if nums1[idx1] > nums2[idx2]:
                nums1[idx] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[idx] = nums2[idx2]
                idx2 -= 1
            idx -= 1
        if idx1 < 0:
            nums1[:idx + 1] = nums2[:idx2 + 1]


if __name__ == "__main__":
    s = Solution()
    l = [1,2,3,0,0,0]
    s.merge(l, m = 3, nums2 = [2,5,6], n = 3)
    print(l)

    l = [1]
    s.merge(l, m = 1, nums2 = [], n = 0)
    print(l)

    l = [0]
    s.merge(l, m = 0, nums2 = [1], n = 1)
    print(l)
