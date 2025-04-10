from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    value: str
    next: Node | None = None


class List:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length: int = 0

    def prepend(self, value):
        n = Node(value)
        if self.length == 0:
            self.length += 1
            self.head = n
            self.tail = n
            return

        self.length += 1
        n.next = self.head
        self.head = n

        return None

    def insert_at(self, index: int, value: str):
        if index > self.length:
            raise Exception

        n = Node(value)
        if index == 0:
            next = self.head
            self.head = n
            self.head.next = next
            self.length += 1
            return

        i: int = 0
        cur: Node | None = self.head
        while cur != None and i != self.length:
            if i == (index - 1):
                break
            cur = cur.next
            i += 1

        next = cur.next
        cur.next = n
        cur.next.next = next
        self.length += 1

    def append(self, value: str) -> None:
        n = Node(value)
        if self.length == 0:
            self.length += 1
            self.head = n
            self.tail = n
            return

        self.length += 1
        self.tail.next = n
        self.tail = n

        return None

    def pop(self) -> Node | None:
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return

        i: int = 0
        cur: Node | None = self.head
        while cur != None and i != self.length:
            if i == (self.length - 1 - 1):
                break
            cur = cur.next
            i += 1

        cur.next = None
        cur_tail = self.tail
        self.tail = cur
        self.length -= 1
        return cur_tail

    def delete_at(self, index: int) -> Node | None:
        if index > self.length:
            raise Exception

        if index == 0:
            to_delete = self.head
            self.head = self.head.next
            self.length -= 1
            return to_delete

        before_index = self.head
        i = 0
        while before_index != None and i != self.length:
            if i == index - 1:
                to_delete = before_index.next
                before_index.next = before_index.next.next
                self.length -= 1
                return to_delete
            else:
                before_index = before_index.next
                i += 1

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
    l1 = List()
    l1.append("1")
    assert "1" == l1.print(), l1.print()

    l2 = List()
    l2.append("1")
    l2.append("2")
    l2.append("3")
    assert "1-2-3" == l2.print(), l2.print()

    l3 = List()
    l3.prepend("1")
    l3.prepend("2")
    l3.prepend("3")
    assert "3-2-1" == l3.print(), l3.print()

    l4 = List()
    l4.append("1")
    l4.append("3")
    assert "1-3" == l4.print()
    l4.insert_at(1, "2")
    assert "1-2-3" == l4.print(), l4.print()
    l4.insert_at(0, "0")
    assert "0-1-2-3" == l4.print(), l4.print()
    l4.insert_at(4, "4")
    assert "0-1-2-3-4" == l4.print(), l4.print()

    l5 = List()
    l5.append("1")
    l5.append("2")
    l5.append("3")
    l5.pop()
    assert "1-2" == l5.print(), l5.print()
    l5.pop()
    assert "1" == l5.print(), l5.print()
    l5.pop()
    assert "" == l5.print(), l5.print()

    l6 = List()
    l6.append("1")
    l6.append("2")
    l6.append("3")
    l6.delete_at(2)
    assert "1-2" == l6.print(), l6.print()
    l6.delete_at(1)
    assert "1" == l6.print(), l6.print()
    l6.delete_at(0)
    assert "" == l6.print(), l6.print()


if __name__ == "__main__":
    main()
