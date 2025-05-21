from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None



def compare(n1: Node, n2: Node) -> bool:
    # structural comparison, we're both at the bottom
    if n1 is None and n2 is None:
        return True

    # structural comparison, one node is None, the other isn't
    if n1 is None or n2 is None:
        return False

    # value comparison
    if n1.value != n2.value:
        return False

    same_left = compare(n1.left, n2.left)
    same_right = compare(n1.right, n2.right)
    return same_left and  same_right


if __name__ == "__main__":
    # create 3 trees that look like this:
    #    a = b =  5                   c =  5
    #           /   \                    /   \
    #         8      10                8      10
    #       /   \   /   \            /   \   /
    #      9     7 5     4          9     7 5
    a = Node(value=5, left=Node(value=8, left=Node(value=9), right=Node(value=7)), right=Node(value=10, left=Node(value=5), right=Node(value=4)))
    b = Node(value=5, left=Node(value=8, left=Node(value=9), right=Node(value=7)), right=Node(value=10, left=Node(value=5), right=Node(value=4)))
    c = Node(value=5, left=Node(value=8, left=Node(value=9), right=Node(value=7)), right=Node(value=10, left=Node(value=5)))

    assert compare(a, b) is True
    assert compare(a, c) is False
