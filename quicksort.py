import random
from typing import List


def qs(arr: List[int], left: int, right: int) -> List[int] | None:
    if left >= right:
        return

    pivotIdx = partition(arr, left, right)

    qs(arr, left, pivotIdx - 1)
    qs(arr, pivotIdx + 1, right)
    return arr


def partition(arr: List[int], left: int, right: int) -> int:
    p = arr[right]
    idx: int = left - 1

    for i in range(left, right):
        # if an element is lower or equal to the pivot
        # then swap it to then idx position
        if arr[i] <= p:
            idx += 1
            tmp = arr[idx]
            arr[idx] = arr[i]
            arr[i] = tmp

    # once all the lower elements have been swapped
    # then we can put our pivot to the next position
    idx += 1
    arr[right] = arr[idx]
    arr[idx] = p

    return idx


def main():
    arr = [5, 20, 6, 1, 12, 2, 10, 11, -4, 3]
    s = qs(arr, 0, len(arr) - 1)
    assert [-4, 1, 2, 3, 5, 6, 10, 11, 12, 20] == s, s
    ls = random.choices([x for x in range(25_000)], k=20_000)
    ls = qs(ls, 0, len(ls) - 1)
    assert all(ls[i] <= ls[i + 1] for i in range(len(ls) - 1))


if __name__ == "__main__":
    main()
