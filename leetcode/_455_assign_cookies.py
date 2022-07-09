from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort(reverse=True)

        content_num = 0
        for i in g:
            while s:
                if s.pop() < i:
                    continue
                else:
                    content_num += 1
                    break
            else:
                return content_num
        return content_num


if __name__ == '__main__':
    s = Solution()
    print(s.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))

