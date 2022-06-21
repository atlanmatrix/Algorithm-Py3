from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_node_lst = []
        curr = head
        while curr:
            curr_val = curr.val
            if curr_val in visited_node_lst:
                return True

            visited_node_lst.append(curr_val)
            curr = curr.next

        return False

