import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        c = collections.Counter(s)
        res_lst = sorted(c.values(), reverse=True)

        del_count = 0
        curr = res_lst[0]
        for i in res_lst[1:]:
            if curr == 0:
                del_count += i
            elif i >= curr:
                delta = i - curr + 1
                del_count += delta
                curr -= 1
            else:
                curr = i
        return del_count


if __name__ == "__main__":
    s = Solution()
    print(s.minDeletions('"abcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwz"'))
    # print(s.minDeletions('aaabbbcc'))
    # print(s.minDeletions('ceabaacb'))
