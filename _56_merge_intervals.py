from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_lst = []
        intervals.sort(key=lambda x: x[0])

        start, end = intervals.pop(0)
        while len(intervals):
            curr = intervals.pop(0)
            if curr[0] <= end:
                if curr[1] > end:
                    end = curr[1]
            else:
                merged_lst.append([start, end])
                start, end = curr
        merged_lst.append([start, end])

        return merged_lst

    def merge_2(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_lst = []
        intervals.sort(key=lambda x: x[0])

        ele = intervals.pop(0)
        for interval in intervals:
            if interval[0] <= ele[1]:
                ele[1] = max(interval[1], ele[1])
            else:
                merged_lst.append(ele)
                ele = interval
        merged_lst.append(ele)

        return merged_lst


if __name__ == "__main__":
    from time import time
    from copy import deepcopy

    test_data_lst = [
        [[1,3],[2,6],[8,10],[15,18]],
        [[1,4],[4,5]]
    ]

    for test_data in deepcopy(test_data_lst):
        st_ts = time()
        res = Solution().merge(test_data)
        print(f'{(time() - st_ts) * 1000}ms')
        print(res)

    for test_data in deepcopy(test_data_lst):
        st_ts = time()
        res = Solution().merge_2(test_data)
        print(f'{(time() - st_ts) * 1000}ms')
        print(res)
