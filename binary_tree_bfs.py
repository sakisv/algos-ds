from __future__ import annotations
from dataclasses import dataclass
#from typing import Sequence

@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None


def bfs(root: Node, needle: int) -> bool:
    queue = [root]

    while queue:
        item = queue.pop(0)

        if item.value == needle:
            return True

        if item.left:
            queue.append(item.left)
        if item.right:
            queue.append(item.right)

    return False

if __name__ == "__main__":
    # create a tree that looks like this:
    #             5
    #           /   \
    #         8      10
    #       /   \   /   \
    #      9     7 5     4
    root = Node(value=5, left=Node(value=8, left=Node(value=9), right=Node(value=7)), right=Node(value=10, left=Node(value=5), right=Node(value=4)))

    assert bfs(root, 4) is True
    assert bfs(root, 123) is False
