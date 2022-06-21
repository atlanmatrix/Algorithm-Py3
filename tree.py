from typing import Optional, Any


class BNode:
    def __init__(self,
        val: Any = None,
        l_node: Optional['BNode'] = None,
        r_node: Optional['BNode'] = None) -> None:
        self.val = val
        self.l_node = l_node
        self.r_node = r_node


class BTree:
    def __init__(self, root_val: Any) -> None:
        root_node = BNode(root_val)
        self.root = root_node


def create_tree(node: BNode, depth: int) -> None:
    if depth == 0:
        return

    node.l_node = BNode(f'{node.val}-l')
    node.r_node = BNode(f'{node.val}-r')

    depth -= 1
    create_tree(node.l_node, depth)
    create_tree(node.r_node, depth)


def preorder_traversal(node: BNode):
    print(node.val, sep=' -> ')

    if node.l_node is not None:
        preorder_traversal(node.l_node)

    if node.r_node is not None:
        preorder_traversal(node.r_node)


def bfs_traversal(nodes: list[BNode]):
    curr = nodes.pop(0)
    print(curr.val)
    if curr.l_node is not None:
        nodes.append(curr.l_node)
    if curr.r_node is not None:
        nodes.append(curr.r_node)
    if len(nodes) > 0:
        bfs_traversal(nodes)


if __name__ == "__main__":
    tree = BTree('root')
    create_tree(tree.root, 3)
    print(tree)

    preorder_traversal(tree.root)
    print('-' * 40)
    bfs_traversal([tree.root])
