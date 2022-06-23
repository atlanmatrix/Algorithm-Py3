from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(lst, no, low, high):
            pi = partition(lst, low, high)

            if low < high:
                if pi < no - 1:
                    return quick_select(lst, no, pi + 1, high)
                elif pi > no - 1:
                    return quick_select(lst, no, low, pi - 1)
                else:
                    return lst[pi]
            else:
                return lst[no - 1]

        def partition(lst, low, high):
            pi = low
            pi_val = lst[pi]

            lst[pi], lst[high] = lst[high], lst[pi]

            for i in range(low, high):
                if lst[i] > pi_val:
                    lst[pi], lst[i] = lst[i], lst[pi]
                    pi += 1
            lst[pi], lst[high] = lst[high], lst[pi]

            return pi

        return quick_select(nums, k, 0, len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4], 2))
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))