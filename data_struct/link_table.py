class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None

l = range(9, 4, -1)

curr = lt = Node()
for i in l:
    curr.next = Node(i)
    curr = curr.next

curr = lt
while curr.next:
    print(curr.next.val)
    curr = curr.next

print('finished!')

