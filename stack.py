from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    value: str
    next: Node | None = None


class Stack:
    def __init__(self):
        self.length = 0
        self.head = None

    def push(self, value: str) -> None:
        n = Node(value)
        self.length += 1
        if self.head is None:
            self.head = n
            return

        n.next = self.head
        self.head = n
        return

    def pop(self) -> str | None:
        if self.head is None:
            raise Exception

        self.length -= 1
        h = self.head
        self.head = self.head.next
        return h.value

    def peek(self) -> str | None:
        if self.head is None:
            raise Exception

        return self.head.value

    def print(self) -> str:
        if self.length == 0:
            return ""

        cur = self.head
        s = []
        while cur != None:
            s.append(cur.value)
            cur = cur.next

        return "-".join(s)


def main():
    q = Stack()
    q.push("a")
    q.push("b")
    q.push("c")
    assert "c-b-a" == q.print(), q.print()

    assert "c" == q.pop()
    assert "b-a" == q.print(), q.print()
    assert "b" == q.peek(), q.print()


if __name__ == "__main__":
    main()
