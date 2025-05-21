class MinHeap:
    def __init__(self):
        self.data = []


    def _parent_idx(self, index: int) -> int:
        return (index - 1) // 2

    def _left_child_idx(self, index: int) -> int:
        return (2 * index) + 1

    def _right_child_idx(self, index: int) -> int:
        return (2 * index) + 2

    def _swap(self, idx1, idx2):
        tmp = self.data[idx1]
        self.data[idx1] = self.data[idx2]
        self.data[idx2] = tmp

    def _heapify_up(self, idx: int):
        if idx == 0:
            return

        parent = self._parent_idx(idx)
        # this is a min heap, so if we're bigger than the parent element then
        # we don't bubble up
        if self.data[idx] > self.data[parent]:
            return
        self._swap(idx, parent)
        self._heapify_up(parent)


    def insert(self, item):
        length = len(self.data)
        self.data.insert(length, item)
        self._heapify_up(length)


    def _heapify_down(self, idx: int):
        idx_l = self._left_child_idx(idx)
        idx_r = self._right_child_idx(idx)

        # if we're at the end of the array
        if idx >= len(self.data):
            return

        # if there's no left child, we return
        if idx_l >= len(self.data):
            return

        # if there's no right child, there may still be a left one
        if idx_r >= len(self.data):
            if self.data[idx_l] < self.data[idx]:
                self._swap(idx, idx_l)
                return

        # if we're larger than our smallest child, swap and heapify down
        if self.data[idx_l] < self.data[idx_r] and self.data[idx_l] < self.data[idx]:
            self._swap(idx, idx_l)
            self._heapify_down(idx_l)

        elif self.data[idx_r] < self.data[idx_l] and self.data[idx_r] < self.data[idx]:
            self._swap(idx, idx_r)
            self._heapify_down(idx_r)

        # if the two children are the same, we try to go down the right one, to keep the tree full
        elif self.data[idx_r] == self.data[idx_l] and self.data[idx_r] < self.data[idx]:
            self._swap(idx, idx_r)
            self._heapify_down(idx_r)

    def delete(self) -> int:
        root = self.data.pop(0)
        # we pop the last element to **move** it to the start of the array
        last_item = self.data.pop(len(self.data) - 1)
        self.data.insert(0, last_item)
        self._heapify_down(0)
        return root


if __name__ == "__main__":
    h = MinHeap()
    h.insert(10)
    h.insert(5)
    h.insert(6)
    h.insert(3)
    h.insert(11)

    assert h.data == [3, 5, 6, 10, 11], h.data

    h.delete()
    assert h.data == [5, 10, 6, 11], h.data

    h.delete()
    assert h.data == [6, 10, 11], h.data
