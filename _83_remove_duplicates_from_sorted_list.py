from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = res_lst = ListNode(None)

        while head is not None:
            if head.val != curr.val:
                curr.next = ListNode()
                curr.next.val = head.val
                curr = curr.next
            head = head.next
        return res_lst.next


if __name__ == "__main__":
    l = [0,0,0,0,0]

    curr = head = ListNode()
    for i in l:
        curr.next = ListNode()
        curr = curr.next
        curr.val = i

    s = Solution()
    res = s.deleteDuplicates(head.next)

    while res is not None:
        print(res.val)
        res = res.next
