from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence

@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None



def _pre_walk(node: Node, path: Sequence[int]) -> Sequence[int]:
    if node is None:
        return path

    path.append(node.value)
    _pre_walk(node.left, path)
    _pre_walk(node.right, path)

    return path

def pre_order_traversal(root: Node) -> Sequence[int]:
    return _pre_walk(root, [])


def _in_walk(node: Node, path: Sequence[int]) -> Sequence[int]:
    if node is None:
        return path

    _in_walk(node.left, path)
    path.append(node.value)
    _in_walk(node.right, path)

    return path

def in_order_traversal(root: Node) -> Sequence[int]:
    return _in_walk(root, [])


def _post_walk(node: Node, path: Sequence[int]) -> Sequence[int]:
    if node is None:
        return path

    _post_walk(node.left, path)
    _post_walk(node.right, path)
    path.append(node.value)

    return path

def post_order_traversal(root: Node) -> Sequence[int]:
    return _post_walk(root, [])


if __name__ == "__main__":
    # create a tree that looks like this:
    #             5
    #           /   \
    #         8      10
    #       /   \   /   \
    #      9     7 5     4
    root = Node(value=5, left=Node(value=8, left=Node(value=9), right=Node(value=7)), right=Node(value=10, left=Node(value=5), right=Node(value=4)))

    assert [5, 8, 9, 7, 10, 5, 4] == pre_order_traversal(root)
    assert [9, 8, 7, 5, 5, 10, 4] == in_order_traversal(root)
    assert [9, 7, 8, 5, 4, 10, 5] == post_order_traversal(root)
