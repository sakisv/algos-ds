from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    value: str
    next: Node | None = None


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def enqueue(self, value: str):
        n = Node(value)
        self.length += 1
        if self.head is None:
            self.head = n
            self.tail = n
            return

        self.tail.next = n
        self.tail = n
        return

    def dequeue(self) -> str | None:
        if self.head is None:
            raise Exception

        head = self.head
        self.head = self.head.next

        self.length -= 1
        return head.value

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
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    assert "a-b-c" == q.print(), q.print()

    assert "a" == q.dequeue()
    assert "b-c" == q.print(), q.print()
    assert "b" == q.peek(), q.print()


if __name__ == "__main__":
    main()
